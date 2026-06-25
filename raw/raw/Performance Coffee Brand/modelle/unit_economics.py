#!/usr/bin/env python3
"""
Performance Coffee — Unit Economics / COGS-Rechner

Skeleton-Modell zur Schätzung der Wareneinsatzkosten (COGS) und Bruttomarge pro Portion.
Lädt Inhaltsstoffdaten aus inhaltsstoffe_db.csv; ergänzt Verpackung, Produktion
und Fulfillment, sobald Angebote vorliegen.

Nutzung:
    python3 modelle/unit_economics.py
    python3 modelle/unit_economics.py --format duo_pack --volume 1000

Benötigte Daten (TODO):
    - inhaltsstoffe_db.csv: Kosten_pro_kg_EUR für jeden Inhaltsstoff
    - PACKAGING_COST_EUR pro Format
    - MANUFACTURING_COST_EUR pro Einheit (CM-Angebot)
    - FULFILLMENT_COST_EUR pro Bestellung
    - TARGET_RRP_EUR für Margenberechnung
"""

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass, field
from pathlib import Path

MODELS_DIR = Path(__file__).parent
INGREDIENT_CSV = MODELS_DIR / "inhaltsstoffe_db.csv"

# --- Platzhalter-Konstanten (mit Angeboten ersetzen) ---

COFFEE_DOSE_GRAMS = 12.0  # g gemahlener Kaffee pro Portion (Power Blend)
SERVING_COFFEE_BEANS = ["Vietnam Robusta Da Lat", "Äthiopien Arabica Yirgacheffe"]

STACK_A_INGREDIENTS = [
    "L-Theanine",
    "L-Tyrosine",
    "B-Vitamin-Premix NRV",
]

PACKAGING_COST_EUR: dict[str, float] = {
    "duo_pack": 0.0,       # TODO: Außenbox + Kaffeetüte + Kapselblister
    "instant_stick": 0.0,  # TODO: Stickfolie + Karton
    "cold_brew_sachet": 0.0,
}

MANUFACTURING_COST_EUR: dict[str, float] = {
    "duo_pack": 0.0,       # TODO: CM-Co-Packing-Gebühr pro Einheit
    "instant_stick": 0.0,
    "cold_brew_sachet": 0.0,
}

FULFILLMENT_COST_EUR = 0.0   # TODO: Pick-Pack-Ship pro Bestellung (pro Einheit anteilen)
TARGET_RRP_EUR = 0.0         # TODO: Verkaufspreis pro Portion/Einheit

FORMAT_LABELS = {
    "duo_pack": "Duo-Pack (Kaffee + Kapsel)",
    "instant_stick": "Instant-Stick",
    "cold_brew_sachet": "Cold-Brew + Sachet",
}


@dataclass
class Ingredient:
    name: str
    category: str
    function: str
    dose_per_serving: float
    unit: str
    cost_per_kg_eur: float | None
    supplier_status: str
    regulatory_status: str
    notes: str

    def cost_per_serving_eur(self) -> float | None:
        """Berechnet Inhaltsstoffkosten für eine Portion.

        Konvertiert Dosis in kg für g/mg/µg-Einheiten. Gibt None zurück, wenn Kosten unbekannt.
        """
        if self.cost_per_kg_eur is None or self.cost_per_kg_eur == 0:
            if self.supplier_status in ("aus_kaffee",):
                return None  # separat über Kaffeebohnen
            return None

        dose = self.dose_per_serving
        unit = self.unit.lower()

        if unit == "kg":
            kg = dose
        elif unit == "g":
            kg = dose / 1000
        elif unit == "mg":
            kg = dose / 1_000_000
        elif unit in ("ug", "µg"):
            kg = dose / 1_000_000_000
        elif unit == "ml":
            kg = dose / 1000  # ~1 g/ml für Flüssigkeiten angenommen
        elif unit == "portion":
            return self.cost_per_kg_eur  # Premix pro Portion angeboten
        else:
            return None

        return kg * self.cost_per_kg_eur


@dataclass
class COGSBreakdown:
    ingredients_eur: float = 0.0
    coffee_eur: float = 0.0
    packaging_eur: float = 0.0
    manufacturing_eur: float = 0.0
    fulfillment_eur: float = 0.0
    missing_data: list[str] = field(default_factory=list)

    @property
    def total_eur(self) -> float:
        return (
            self.ingredients_eur
            + self.coffee_eur
            + self.packaging_eur
            + self.manufacturing_eur
            + self.fulfillment_eur
        )

    def gross_margin_pct(self, rrp: float) -> float | None:
        if rrp <= 0:
            return None
        return (rrp - self.total_eur) / rrp * 100


def load_ingredients(path: Path = INGREDIENT_CSV) -> dict[str, Ingredient]:
    """Lädt Inhaltsstoffdatenbank aus CSV (deutsche Spaltenköpfe)."""
    ingredients: dict[str, Ingredient] = {}
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            cost_raw = row.get("Kosten_pro_kg_EUR", "").strip()
            cost = float(cost_raw) if cost_raw else None
            ingredients[row["Name"]] = Ingredient(
                name=row["Name"],
                category=row["Kategorie"],
                function=row["Funktion"],
                dose_per_serving=float(row["Dosis_pro_Portion"]),
                unit=row["Einheit"],
                cost_per_kg_eur=cost,
                supplier_status=row["Lieferantenstatus"],
                regulatory_status=row["Regulatorik_Status"],
                notes=row["Notizen"],
            )
    return ingredients


def calculate_coffee_cost(
    ingredients: dict[str, Ingredient],
    dose_grams: float = COFFEE_DOSE_GRAMS,
    bean_names: list[str] | None = None,
) -> tuple[float, list[str]]:
    """Schätzt Kaffee-COGS aus Bohnenzeilen in inhaltsstoffe_db."""
    missing: list[str] = []
    total = 0.0
    beans = bean_names or SERVING_COFFEE_BEANS

    priced = [(name, ingredients[name]) for name in beans if name in ingredients]
    if not priced:
        missing.append("kaffeebohnen")
        return 0.0, missing

    blend_total = sum(ing.dose_per_serving for _, ing in priced)
    if blend_total <= 0:
        missing.append("kaffee_blend_dosen")
        return 0.0, missing

    for name, ing in priced:
        fraction = ing.dose_per_serving / blend_total
        serving_dose_g = dose_grams * fraction
        if ing.cost_per_kg_eur is None:
            missing.append(f"kaffee_kosten:{name}")
            continue
        total += (serving_dose_g / 1000) * ing.cost_per_kg_eur

    return total, missing


def calculate_ingredient_cost(
    ingredients: dict[str, Ingredient],
    stack: list[str] | None = None,
) -> tuple[float, list[str]]:
    """Summiert Supplement-Inhaltsstoffkosten für eine Portion (Standard: Stack A)."""
    missing: list[str] = []
    total = 0.0
    stack = stack or STACK_A_INGREDIENTS

    for name in stack:
        if name not in ingredients:
            missing.append(f"unbekannt:{name}")
            continue
        ing = ingredients[name]
        cost = ing.cost_per_serving_eur()
        if cost is None:
            missing.append(f"inhaltsstoff_kosten:{name}")
            continue
        total += cost

    return total, missing


def calculate_cogs(
    product_format: str = "duo_pack",
    stack: list[str] | None = None,
) -> COGSBreakdown:
    """Vollständige COGS-Aufschlüsselung für eine Einheit/Portion.

    Args:
        product_format: duo_pack | instant_stick | cold_brew_sachet
        stack: Inhaltsstoffnamen (Standard Stack A)

    Returns:
        COGSBreakdown mit Summen und Liste fehlender Datenfelder
    """
    ingredients = load_ingredients()
    breakdown = COGSBreakdown()

    ing_cost, ing_missing = calculate_ingredient_cost(ingredients, stack)
    breakdown.ingredients_eur = ing_cost
    breakdown.missing_data.extend(ing_missing)

    coffee_cost, coffee_missing = calculate_coffee_cost(ingredients)
    breakdown.coffee_eur = coffee_cost
    breakdown.missing_data.extend(coffee_missing)

    if product_format in PACKAGING_COST_EUR:
        pkg = PACKAGING_COST_EUR[product_format]
        if pkg <= 0:
            breakdown.missing_data.append(f"verpackung:{product_format}")
        breakdown.packaging_eur = pkg
    else:
        breakdown.missing_data.append(f"unbekanntes_format:{product_format}")

    if product_format in MANUFACTURING_COST_EUR:
        mfg = MANUFACTURING_COST_EUR[product_format]
        if mfg <= 0:
            breakdown.missing_data.append(f"produktion:{product_format}")
        breakdown.manufacturing_eur = mfg

    if FULFILLMENT_COST_EUR <= 0:
        breakdown.missing_data.append("fulfillment")
    breakdown.fulfillment_eur = FULFILLMENT_COST_EUR

    return breakdown


def break_even_units(fixed_costs_monthly: float, contribution_margin: float) -> float | None:
    """Einheiten pro Monat zur Deckung der Fixkosten.

    Args:
        fixed_costs_monthly: Shopify, Content, Ops-Overhead (EUR)
        contribution_margin: RRP − variable COGS pro Einheit (EUR)

    Returns:
        Break-even-Einheiten oder None, wenn Marge ≤ 0
    """
    if contribution_margin <= 0:
        return None
    return fixed_costs_monthly / contribution_margin


def print_report(
    product_format: str = "duo_pack",
    volume: int | None = None,
    fixed_costs: float = 0.0,
) -> None:
    """Gibt COGS-Szenario lesbar aus."""
    breakdown = calculate_cogs(product_format)
    format_label = FORMAT_LABELS.get(product_format, product_format)
    print("=" * 60)
    print("Performance Coffee — Unit Economics (COGS)")
    print("=" * 60)
    print(f"Format:     {format_label}")
    print(f"Stack:      {', '.join(STACK_A_INGREDIENTS)}")
    print(f"Kaffee:     {COFFEE_DOSE_GRAMS} g pro Portion")
    print()
    print("Kostenaufschlüsselung (EUR pro Portion):")
    print(f"  Inhaltsstoffe: {breakdown.ingredients_eur:>8.4f}")
    print(f"  Kaffee:        {breakdown.coffee_eur:>8.4f}")
    print(f"  Verpackung:    {breakdown.packaging_eur:>8.4f}")
    print(f"  Produktion:    {breakdown.manufacturing_eur:>8.4f}")
    print(f"  Fulfillment:   {breakdown.fulfillment_eur:>8.4f}")
    print(f"  {'—' * 28}")
    print(f"  COGS GESAMT:   {breakdown.total_eur:>8.4f}")

    if breakdown.missing_data:
        print()
        print("Fehlende Daten (inhaltsstoffe_db.csv oder Konstanten ergänzen):")
        for item in sorted(set(breakdown.missing_data)):
            print(f"  - {item}")

    if TARGET_RRP_EUR > 0:
        margin = breakdown.gross_margin_pct(TARGET_RRP_EUR)
        print()
        print(f"Ziel-RRP:        €{TARGET_RRP_EUR:.2f}")
        if margin is not None:
            print(f"Bruttomarge:     {margin:.1f} %")
            contrib = TARGET_RRP_EUR - breakdown.total_eur
            be = break_even_units(fixed_costs, contrib)
            if be is not None:
                print(
                    f"Break-even:      {be:,.0f} Einheiten/Monat "
                    f"(Fixkosten €{fixed_costs:,.0f})"
                )
    else:
        print()
        print("TODO: TARGET_RRP_EUR setzen für Margen- und Break-even-Analyse.")

    if volume:
        print()
        print(f"Chargenmenge:    {volume:,} Einheiten")
        print(f"Chargen-COGS:    €{breakdown.total_eur * volume:,.2f}")
        if breakdown.missing_data:
            print("  (unvollständig — Kostenwerte fehlen)")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Performance Coffee COGS-Rechner (Unit Economics)"
    )
    parser.add_argument(
        "--format",
        default="duo_pack",
        choices=["duo_pack", "instant_stick", "cold_brew_sachet"],
        help="Produktformat",
    )
    parser.add_argument(
        "--volume",
        type=int,
        default=None,
        help="Chargenmenge für Gesamt-COGS",
    )
    parser.add_argument(
        "--fixed-costs",
        type=float,
        default=0.0,
        help="Monatliche Fixkosten für Break-even (EUR)",
    )
    args = parser.parse_args()
    print_report(args.format, args.volume, args.fixed_costs)


if __name__ == "__main__":
    main()
