---
title: Structured Data Directory README
type: source
tags: [data, dataview, csv, infrastructure, vault-structure, cli]
sources: ["raw/data/README.md"]
created: 2026-06-15
updated: 2026-06-15
summary: README for the raw/data/ directory — placeholder instructing placement of CSV exports (cashflow, health metrics, training logs) for Dataview and CLI tools; explicitly forbids secrets or credentials
---

# Structured Data Directory — README

## Overview

This source page captures the README for the `raw/data/` directory in [[Oleg Personal Context|Oleg]]'s vault. The directory is designated as a structured data store for machine-readable exports consumed by [[Dataview]] queries and CLI tooling.

## Purpose

The `raw/data/` directory is intended to hold **CSV exports** across three domains:

| Domain | Examples |
|---|---|
| **Cashflow** | Monthly income/expense exports, budget vs. actual |
| **Health metrics** | Biomarker results, body scan measurements, HRV, weight tracking |
| **Training logs** | Workout logs, Hyrox training data, Zone 2 session records |

## Constraints

- **No secrets or credentials** — explicitly prohibited by the README
- Data here is structured/machine-readable (CSV), not prose notes
- Intended for tool consumption, not human browsing

## Relationship to Wiki Concepts

The data stored here would feed into:

- **[[Biomarker Testing]]** / **[[Blutbild Panel]]** — quarterly blood panel results as CSV
- **[[3D Body Scan]]** / **[[3D Body Scan Scaneca Mai 2026]]** — body composition metrics over time
- **[[BMR and TDEE]]** — caloric tracking exports
- **[[Hyrox 10-Week Training]]** — training log data
- **[[Fixkosten Übersicht]]** — cashflow / fixed cost exports
- **[[MOC Finanzen]]** — financial data exports

## Dataview Integration

[[Dataview]] is an Obsidian plugin that enables SQL-like queries over vault content, including CSV files in this directory. This enables dynamic dashboards for health metrics, financial summaries, and training progress without duplicating data manually into notes.

## Current State

As of the README's creation, the directory contains **no data files** — only this instructional README. Data population is a future action as CSV exports are generated from:
- Wahoo/Garmin training exports
- Blood panel lab results
- Bank/Finom account exports
- Body scan follow-up data

## No Contradictions

This README does not contradict any existing wiki content. It establishes infrastructure context only.

## Related Pages

- [[Blutbild Panel]] — health metrics to be stored here
- [[3D Body Scan Scaneca Mai 2026]] — body composition data
- [[BMR and TDEE]] — metabolic tracking context
- [[Fixkosten Übersicht]] — cashflow data source
- [[MOC Finanzen]] — financial data context
- [[MOC Performance und Leben]] — health/training data context
- [[Oleg Personal Context]] — vault owner
