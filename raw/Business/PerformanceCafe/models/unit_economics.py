"""
Performance Café — Unit Economics Modell
========================================
Ausfüllen mit Daten aus research/02_ingredienzen_db.md und research/05_prototyp_partner.md

Ausführen: python3 models/unit_economics.py
"""

# ============================================================
# KONFIGURATION — hier Zahlen eintragen wenn Daten vorliegen
# ============================================================

PORTIONEN_PRO_SACHET = 1  # 1 Sachet = 1 Portion

# --- ROHSTOFFE (€ pro Portion) ---
# Aus research/02_ingredienzen_db.md befüllen
rohstoffe = {
    "Kaffee (Freeze-Dried, Specialty)":  0.00,  # TODO
    "L-Theanin":                         0.00,  # TODO
    "Alpha-GPC":                         0.00,  # TODO
    "Lion's Mane Extrakt":               0.00,  # TODO
    "Cordyceps Militaris":               0.00,  # TODO
    "Ashwagandha KSM-66":                0.00,  # TODO
    "NAC":                               0.00,  # TODO
    "Urolithin A":                       0.00,  # TODO — Amazentis Patent prüfen!
    "Spermidine":                        0.00,  # TODO — Novel Food Status prüfen!
    "Astaxanthin":                       0.00,  # TODO
    "CoQ10 Ubiquinol":                   0.00,  # TODO
    "Sonstige Inhaltsstoffe":            0.00,  # TODO
}

# --- PRODUKTION & PACKAGING ---
cmo_manufacturing_pro_portion   = 0.00  # TODO: aus research/05_prototyp_partner.md
sachet_packaging_pro_portion    = 0.00  # TODO: Stick-Pack Material + Druck
box_packaging_pro_portion       = 0.00  # TODO: Outer Box (30er Pack)
zertifizierung_pro_portion      = 0.00  # TODO: Kölner Liste / Informed Sport amortisiert

# --- LOGISTIK & FULFILLMENT ---
fulfillment_pro_portion         = 0.00  # TODO: Lager + Pick & Pack + Versand
retouren_pro_portion            = 0.00  # TODO: ~3-5% Retourenrate

# --- VERKAUFSKANAL-KOSTEN ---
dtc_payment_fee_pct             = 0.025  # 2,5% Stripe/Zahlungsabwicklung
amazon_fee_pct                  = 0.15   # ~15% Amazon Referral Fee (Kategorie abhängig)
subscription_discount_pct       = 0.10   # 10% Subscription-Rabatt

# --- PREISE (Zielkorridor) ---
preise_szenarien = {
    "Entry (30er Box)":     0.00,   # TODO: Zielpreis pro Portion
    "Premium (30er Box)":   0.00,   # TODO
    "Ultra (30er Box)":     0.00,   # TODO
}

# --- BENCHMARKS (Recherche) ---
BENCHMARK_BLUEPRINT_LONGEVITY_MIX   = 1.63  # USD/Portion (49 USD / 30 Portionen)
BENCHMARK_TIMELINE_MITOPURE         = 3.30  # EUR/Portion (~100 EUR / 30 Portionen)
BENCHMARK_FOUR_SIGMATIC             = 3.00  # EUR/Portion (ca.)
BENCHMARK_RYZE                      = 2.00  # EUR/Portion (ca.)


# ============================================================
# BERECHNUNGEN
# ============================================================

def berechne_cogs():
    rohstoff_gesamt = sum(rohstoffe.values())
    cogs = (
        rohstoff_gesamt
        + cmo_manufacturing_pro_portion
        + sachet_packaging_pro_portion
        + box_packaging_pro_portion
        + zertifizierung_pro_portion
        + fulfillment_pro_portion
        + retouren_pro_portion
    )
    return rohstoff_gesamt, cogs


def berechne_unit_economics(vk_preis: float, kanal: str = "DTC") -> dict:
    rohstoff_gesamt, cogs = berechne_cogs()
    
    if kanal == "DTC":
        kanal_kosten = vk_preis * dtc_payment_fee_pct
    elif kanal == "Amazon":
        kanal_kosten = vk_preis * amazon_fee_pct
    else:
        kanal_kosten = 0

    contribution_margin = vk_preis - cogs - kanal_kosten
    contribution_margin_pct = (contribution_margin / vk_preis * 100) if vk_preis > 0 else 0

    return {
        "VK-Preis": vk_preis,
        "Rohstoffe": rohstoff_gesamt,
        "COGS gesamt": cogs,
        "Kanal-Kosten": kanal_kosten,
        "Contribution Margin (€)": contribution_margin,
        "Contribution Margin (%)": contribution_margin_pct,
        "COGS/VK Ratio (%)": (cogs / vk_preis * 100) if vk_preis > 0 else 0,
    }


def break_even_analyse(fixkosten_monat: float, vk_preis: float, kanal: str = "DTC") -> dict:
    """Wie viele Portionen/Boxen müssen pro Monat verkauft werden?"""
    ue = berechne_unit_economics(vk_preis, kanal)
    cm = ue["Contribution Margin (€)"]
    
    if cm <= 0:
        return {"Fehler": "Contribution Margin <= 0 — Preis zu niedrig oder COGS zu hoch"}
    
    portionen_break_even = fixkosten_monat / cm
    boxen_break_even = portionen_break_even / 30  # 30er Box

    return {
        "Fixkosten/Monat": fixkosten_monat,
        "CM pro Portion": cm,
        "Break-Even Portionen/Monat": round(portionen_break_even),
        "Break-Even Boxen/Monat": round(boxen_break_even),
        "Break-Even Umsatz/Monat": round(portionen_break_even * vk_preis, 2),
    }


# ============================================================
# OUTPUT
# ============================================================

def main():
    print("=" * 60)
    print("PERFORMANCE CAFÉ — UNIT ECONOMICS")
    print("=" * 60)

    rohstoff_gesamt, cogs = berechne_cogs()

    print(f"\n📦 COGS BREAKDOWN (pro Portion)")
    print(f"  Rohstoffe gesamt:        {rohstoff_gesamt:.3f} €")
    print(f"  CMO Manufacturing:       {cmo_manufacturing_pro_portion:.3f} €")
    print(f"  Sachet Packaging:        {sachet_packaging_pro_portion:.3f} €")
    print(f"  Box Packaging:           {box_packaging_pro_portion:.3f} €")
    print(f"  Zertifizierung (amor.):  {zertifizierung_pro_portion:.3f} €")
    print(f"  Fulfillment:             {fulfillment_pro_portion:.3f} €")
    print(f"  Retouren:                {retouren_pro_portion:.3f} €")
    print(f"  ─────────────────────────────────")
    print(f"  COGS GESAMT:             {cogs:.3f} €")

    print(f"\n📊 SZENARIEN (DTC vs. Amazon)")
    for szenario, preis in preise_szenarien.items():
        if preis == 0:
            print(f"\n  {szenario}: Preis noch nicht definiert")
            continue
        print(f"\n  {szenario} — {preis:.2f} €/Portion")
        for kanal in ["DTC", "Amazon"]:
            ue = berechne_unit_economics(preis, kanal)
            print(f"    [{kanal}] CM: {ue['Contribution Margin (€)']:.2f} € "
                  f"({ue['Contribution Margin (%)']:.1f}%) "
                  f"| COGS/VK: {ue['COGS/VK Ratio (%)']:.1f}%")

    print(f"\n🎯 BENCHMARK-VERGLEICH (Ziel-Positionierung)")
    print(f"  Blueprint Longevity Mix:  {BENCHMARK_BLUEPRINT_LONGEVITY_MIX:.2f} USD/Portion")
    print(f"  Timeline Mitopure:        {BENCHMARK_TIMELINE_MITOPURE:.2f} EUR/Portion")
    print(f"  Four Sigmatic:            {BENCHMARK_FOUR_SIGMATIC:.2f} EUR/Portion")
    print(f"  RYZE:                     {BENCHMARK_RYZE:.2f} EUR/Portion")

    print(f"\n⚠️  Noch auszufüllen:")
    fehlend = [(k, v) for k, v in rohstoffe.items() if v == 0.0]
    for stoff, _ in fehlend:
        print(f"  - {stoff}: Preis fehlt → research/02_ingredienzen_db.md")
    if cmo_manufacturing_pro_portion == 0:
        print(f"  - CMO Manufacturing: Angebot einholen → research/05_prototyp_partner.md")

    print(f"\n{'=' * 60}")
    print("Daten aus research/ Dateien ergänzen, dann erneut ausführen.")


if __name__ == "__main__":
    main()
