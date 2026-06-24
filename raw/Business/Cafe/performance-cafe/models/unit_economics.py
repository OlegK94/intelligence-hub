"""
Performance Café — Unit Economics Modell v2.0
=============================================
Stand: 2026-06-24 | Strategie: Performance-First (research/09_strategie_update.md)

3 SKUs:
  CORE        → Morning/Performance (MVP, Launch-SKU)
  PREWORKOUT  → Core + mehr Koffein/Cordyceps, ohne Ashwagandha
  LONGEVITY   → Core + NAC/Spermidine/Astaxanthin/Lion's Mane (Premium-Tier)

Alle Rohstoff-/Produktionswerte = Annahmen [A] bis CMO-Angebote vorliegen.
Ausführen: python3 models/unit_economics.py [--csv]
"""

import sys
import csv
import io


# ROHSTOFFE je SKU (€/Portion) — [A]

ROHSTOFFE_CORE = {
    "Kaffee (Freeze-Dried Light Roast 60/40 Robusta/Arabica)": 0.10,
    "L-Theanin 200mg":                                          0.03,
    "Cordyceps Militaris 500mg (Dual-Extract Fruchtkörper)":   0.16,
    "Rhodiola Rosea 200mg (3% Rosavin/1% Salidrosid)":        0.08,
    "L-Tyrosin 500mg":                                          0.04,
    "Alpha-GPC 300mg (50%-Form)":                               0.12,
    "Ashwagandha KSM-66 300mg":                                 0.11,
    "Taurin 1000mg":                                            0.03,
}

# Pre-Workout: Core − Ashwagandha + mehr Koffein/Cordyceps
ROHSTOFFE_PREWORKOUT = {
    k: v for k, v in ROHSTOFFE_CORE.items()
    if "Ashwagandha" not in k
}
ROHSTOFFE_PREWORKOUT["Kaffee (Freeze-Dried Light Roast, high-caf)"] = 0.13
ROHSTOFFE_PREWORKOUT["Cordyceps Militaris 500mg (Dual-Extract Fruchtkörper)"] = 0.22

# +Longevity: Core + Longevity-Layer
ROHSTOFFE_LONGEVITY = dict(ROHSTOFFE_CORE)
ROHSTOFFE_LONGEVITY.update({
    "NAC 600mg":                                                0.05,
    "Spermidine (Weizenkeimextrakt) 6mg":                     0.15,
    "Astaxanthin 4mg":                                          0.07,
    "Lion's Mane Dual Extract 500mg":                          0.20,
})

ALLE_SKUS = {
    "CORE":       ROHSTOFFE_CORE,
    "PREWORKOUT": ROHSTOFFE_PREWORKOUT,
    "LONGEVITY":  ROHSTOFFE_LONGEVITY,
}


# PRODUKTION & PACKAGING [A]

COGS_STRUKTUR = {
    "CMO Manufacturing (Sachet-Mischung + Fertigung)": 0.35,
    "Sachet Packaging (Stick-Pack + Schutzgas-Versiegelung)": 0.11,
    "Box Packaging (30er Outer Box, amortisiert)":     0.15,
    "Zertifizierung Kölner Liste (amortisiert)":        0.03,
    "Fulfillment DTC (Lager + Pick&Pack + Versand)":   0.40,
    "Retouren (~4% Rate, amortisiert)":                 0.07,
}

# LONGEVITY: NAC-Flavorist-Maskierung erhöht CMO-Kosten
COGS_DELTA_LONGEVITY = {
    "CMO Manufacturing (Sachet-Mischung + Fertigung)": 0.05,
}


# KANAL-KOSTEN

KANAL = {
    "DTC":     {"fee_pct": 0.025, "label": "DTC (Shopify)"},
    "Amazon":  {"fee_pct": 0.150, "label": "Amazon DE"},
    "Hyrox":   {"fee_pct": 0.000, "label": "Event/Pop-up (0% Fee)"},
}

SUBSCRIPTION_RABATT_PCT = 0.10


# PREISE (€/Portion, 30er Box)

PREISE = {
    "CORE":       {"Entry": 2.90, "Standard": 3.20, "Premium": 3.50},
    "PREWORKOUT": {"Entry": 2.90, "Standard": 3.20, "Premium": 3.50},
    "LONGEVITY":  {"Entry": 3.50, "Standard": 3.90, "Premium": 4.30},
}


# FIXKOSTEN (monatlich)

FIXKOSTEN = {
    "Pre-Launch (M1-M3)":  3_000,
    "Launch (M4-M9)":      5_500,
    "Scale (M10-M24)":     8_000,
}


# KERNFUNKTIONEN

def berechne_rohstoffe(sku: str) -> float:
    return sum(ALLE_SKUS[sku].values())


def berechne_cogs(sku: str) -> float:
    rohstoffe = berechne_rohstoffe(sku)
    prod = sum(COGS_STRUKTUR.values())
    if sku == "LONGEVITY":
        prod += sum(COGS_DELTA_LONGEVITY.values())
    return rohstoffe + prod


def berechne_unit_economics(sku: str, preis_tier: str, kanal_key: str = "DTC"):
    vk = PREISE[sku][preis_tier]
    cogs = berechne_cogs(sku)
    fee_pct = KANAL[kanal_key]["fee_pct"]
    kanal_kosten = vk * fee_pct
    cm = vk - cogs - kanal_kosten
    cm_pct = (cm / vk * 100) if vk else 0
    return {
        "SKU": sku, "Preis-Tier": preis_tier, "Kanal": kanal_key,
        "VK-Preis": vk, "Rohstoffe": berechne_rohstoffe(sku),
        "COGS": cogs, "Kanal-Kosten": kanal_kosten,
        "CM (€)": cm, "CM (%)": cm_pct,
        "COGS/VK (%)": (cogs / vk * 100) if vk else 0,
    }


def break_even(sku: str, preis_tier: str, kanal_key: str, fixkosten: float):
    ue = berechne_unit_economics(sku, preis_tier, kanal_key)
    cm = ue["CM (€)"]
    if cm <= 0:
        return {"Fehler": f"CM <= 0 ({cm:.2f}€)"}
    portionen = fixkosten / cm
    return {
        "Break-Even Portionen/Monat": round(portionen),
        "Break-Even Boxen/Monat":     round(portionen / 30),
        "Break-Even Umsatz/Monat":    round(portionen * ue["VK-Preis"], 0),
        "CM pro Portion":             cm,
    }


def ltv_cac(sku: str, preis_tier: str, kanal_key: str = "DTC",
            boxen_lifetime: int = 10, ziel_ratio: float = 3.0):
    cm = berechne_unit_economics(sku, preis_tier, kanal_key)["CM (€)"]
    ltv = cm * 30 * boxen_lifetime
    return ltv, ltv / ziel_ratio


def sensitivitaet(sku: str, preis_tier: str, kanal_key: str = "DTC"):
    basis = berechne_unit_economics(sku, preis_tier, kanal_key)
    vk_basis = basis["VK-Preis"]
    cogs_basis = basis["COGS"]
    fee = KANAL[kanal_key]["fee_pct"]
    rows = []
    for cogs_delta in [-0.20, -0.10, 0.00, +0.10, +0.20]:
        for vk_delta in [-0.10, -0.05, 0.00, +0.05, +0.10]:
            cogs = cogs_basis * (1 + cogs_delta)
            vk = vk_basis * (1 + vk_delta)
            cm = vk - cogs - vk * fee
            cm_pct = cm / vk * 100 if vk else 0
            rows.append({
                "COGS Delta": f"{cogs_delta:+.0%}",
                "VK Delta":   f"{vk_delta:+.0%}",
                "VK (EUR)": round(vk, 2),
                "COGS (EUR)": round(cogs, 2),
                "CM (EUR)": round(cm, 2),
                "CM (%)": round(cm_pct, 1),
            })
    return rows


WACHSTUM_PORTIONEN = {
    1: 0, 2: 0, 3: 0,
    4: 300, 5: 600, 6: 900,
    7: 1_200, 8: 1_800, 9: 2_400,
    10: 3_000, 11: 3_900, 12: 4_800,
    13: 5_700, 14: 6_600, 15: 7_500, 16: 8_400,
    17: 9_000, 18: 9_600, 19: 10_200, 20: 10_800,
    21: 11_400, 22: 12_000, 23: 12_600, 24: 13_200,
}

SKU_MIX_LAUNCH = {"CORE": 0.80, "PREWORKOUT": 0.15, "LONGEVITY": 0.05}
SKU_MIX_SCALE  = {"CORE": 0.70, "PREWORKOUT": 0.20, "LONGEVITY": 0.10}

KANAL_MIX_LAUNCH = {"DTC": 0.85, "Amazon": 0.05, "Hyrox": 0.10}
KANAL_MIX_SCALE  = {"DTC": 0.75, "Amazon": 0.20, "Hyrox": 0.05}

CAC_MONAT = {m: 100 if m <= 6 else (75 if m <= 12 else 55) for m in range(1, 25)}


def monatlicher_cm(portionen, sku_mix, kanal_mix, preis_tier="Standard"):
    total_cm = 0.0
    for sku, sku_anteil in sku_mix.items():
        for kanal, kanal_anteil in kanal_mix.items():
            ue = berechne_unit_economics(sku, preis_tier, kanal)
            portion_anteil = portionen * sku_anteil * kanal_anteil
            total_cm += portion_anteil * ue["CM (€)"]
    return total_cm


def monatlicher_umsatz(portionen, sku_mix, kanal_mix, preis_tier="Standard"):
    total = 0.0
    for sku, sku_anteil in sku_mix.items():
        vk = PREISE[sku][preis_tier]
        total += portionen * sku_anteil * vk
    return total


def neue_kunden_monat(portionen, m):
    boxen = portionen / 30
    neue_boxen = boxen * (0.60 if m <= 9 else 0.40)
    return neue_boxen * CAC_MONAT[m]


def berechne_pnl_24m():
    rows = []
    kumuliert_ebitda = 0.0
    for m in range(1, 25):
        portionen = WACHSTUM_PORTIONEN[m]
        is_scale = m >= 10
        sku_mix   = SKU_MIX_SCALE  if is_scale else SKU_MIX_LAUNCH
        kanal_mix = KANAL_MIX_SCALE if is_scale else KANAL_MIX_LAUNCH
        if m <= 3:
            fixk = FIXKOSTEN["Pre-Launch (M1-M3)"]
        elif m <= 9:
            fixk = FIXKOSTEN["Launch (M4-M9)"]
        else:
            fixk = FIXKOSTEN["Scale (M10-M24)"]
        umsatz = monatlicher_umsatz(portionen, sku_mix, kanal_mix)
        cm     = monatlicher_cm(portionen, sku_mix, kanal_mix)
        marketing_spend = neue_kunden_monat(portionen, m)
        ebitda = cm - fixk - marketing_spend
        kumuliert_ebitda += ebitda
        rows.append({
            "Monat": m,
            "Portionen": portionen,
            "Boxen": round(portionen / 30) if portionen else 0,
            "Umsatz (EUR)": round(umsatz),
            "CM (EUR)": round(cm),
            "Fixkosten (EUR)": round(fixk),
            "Marketing-Spend (EUR)": round(marketing_spend),
            "EBITDA (EUR)": round(ebitda),
            "EBITDA kum. (EUR)": round(kumuliert_ebitda),
        })
    return rows


def main(csv_export=False):
    print("Performance Cafe - Unit Economics v2.0  (Schaetzwerte [A], 06/2026)")
    core_cm = berechne_unit_economics("CORE", "Standard", "DTC")["CM (€)"]
    core_cogs = berechne_cogs("CORE")
    print(f"CORE Standard DTC: COGS {core_cogs:.2f} EUR, CM {core_cm:.2f} EUR ({core_cm/3.20*100:.1f}%)")
    be = break_even("CORE", "Standard", "DTC", FIXKOSTEN["Scale (M10-M24)"])
    print(f"Break-Even: {be['Break-Even Boxen/Monat']} Boxen/Monat")
    ltv, cac_max = ltv_cac("CORE", "Standard")
    print(f"LTV: {ltv:.0f} EUR | Max. CAC: {cac_max:.0f} EUR")
    if csv_export:
        pnl = berechne_pnl_24m()
        filename = "models/unit_economics_24m_pnl.csv"
        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=pnl[0].keys(), delimiter=";")
            writer.writeheader()
            writer.writerows(pnl)
        print(f"CSV exportiert: {filename}")


if __name__ == "__main__":
    csv_flag = "--csv" in sys.argv
    main(csv_export=csv_flag)
