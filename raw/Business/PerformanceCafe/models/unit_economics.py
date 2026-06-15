"""
Performance Coffee Brand — Unit Economics Modell
=================================================
Basiert auf Recherche-Daten aus research/02_ingredienzen_db.md
und research/05_prototyp_partner.md (Stand 2026-06)

Ausführen: python3 models/unit_economics.py
"""

# ============================================================
# KONFIGURATION — Bulk-Preise DACH 2025/2026
# ============================================================

PORTIONEN_PRO_SACHET = 1  # 1 Sachet = 1 Portion

# --- ROHSTOFFE (€ pro Portion, Bulk-Preise DE/EU) ---
# Tier-1 Stack (Morning Performance SKU) — sofort launchbar
rohstoffe_tier1 = {
    "Kaffee Light Roast Instant":        0.054,  # 3g × 18€/kg
    "L-Theanin":                         0.007,  # 200mg × 35€/kg
    "Alpha-GPC 50%":                     0.036,  # 300mg × 120€/kg
    "Lions Mane 8:1 Extrakt":            0.040,  # 500mg × 80€/kg
    "Ashwagandha KSM-66":               0.018,  # 300mg × 60€/kg
    "Kreatin Monohydrat Creapure":       0.032,  # 2g × 16€/kg
    "Taurin":                            0.006,  # 500mg × 12€/kg
    "Aromen + Stevia":                   0.008,  # pauschal
}

# Tier-2 Stack (Longevity Pro SKU) — nach Novel-Food-Klärung
rohstoffe_tier2_zusatz = {
    "NMN":                               0.300,  # 250mg × 1200€/kg ⚠️ Novel Food
    "Urolithin A":                       1.250,  # 500mg × 2500€/kg ⚠️ Patent
    "Spermidine (Weizenkeimextrakt)":   0.004,  # 5mg × 800€/kg
    "NAC":                               0.009,  # 300mg × 30€/kg
    "Curcumin Mizellar":                0.030,  # 200mg × 150€/kg
    "Quercetin":                         0.018,  # 250mg × 70€/kg
    "Astaxanthin":                       0.005,  # 6mg × 900€/kg
    "CoQ10 Ubiquinol":                  0.040,  # 100mg × 400€/kg
}

# Aktiver Stack (Tier-1 als Standard)
rohstoffe = rohstoffe_tier1

# --- PRODUKTION & PACKAGING ---
cmo_manufacturing_pro_portion   = 0.20   # CMO-Aufschlag ~35% auf Rohstoffe (Schätzung)
sachet_packaging_pro_portion    = 0.05   # Aluminium Stick-Pack
box_packaging_pro_portion       = 0.03   # 30er Box Outer
zertifizierung_pro_portion      = 0.005  # Kölner Liste amortisiert auf 10K Einheiten/Jahr

# --- LOGISTIK & FULFILLMENT ---
fulfillment_pro_portion         = 0.40   # Lager + Pick & Pack (DTC, 30er Box = 12€/Box)
retouren_pro_portion            = 0.03   # ~3% Retourenrate

# --- VERKAUFSKANAL-KOSTEN ---
dtc_payment_fee_pct             = 0.025
amazon_fee_pct                  = 0.15
subscription_discount_pct       = 0.10

# --- PREISSZENARIEN (aus Marktanalyse research/04_marktanalyse.md) ---
preise_szenarien = {
    "Entry (Abo-Preis)":   2.99,
    "Standard (VK)":       3.49,
    "Premium (VK)":        3.99,
}

# --- BENCHMARKS (aus research/04_marktanalyse.md) ---
BENCHMARK_BLUEPRINT_LONGEVITY_MIX   = 1.50  # EUR/Portion (49 USD / 30 Portionen)
BENCHMARK_TIMELINE_MITOPURE         = 4.17  # EUR/Portion (~125 EUR / 30 Portionen)
BENCHMARK_FOUR_SIGMATIC             = 1.75  # EUR/Portion
BENCHMARK_RYZE                      = 1.00  # EUR/Portion
BENCHMARK_PUROVITALIS_NMN           = 2.00  # EUR/Tag (EU-Referenz Longevity)


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
