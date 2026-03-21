# Langzeit-Ping-Monitor mit Latenz-Plot

Ein einfaches Python-Skript, das über einen langen Zeitraum kontinuierlich einen Ziel-Server anpingt, die Latenz misst und am Ende (bei Abbruch mit Strg+C) einen Graphen der Latenzentwicklung inkl. sichtbarer Timeouts erstellt.

## Was macht das Skript genau?

- Sendet alle X Sekunden (standardmäßig 1 Sekunde) einen einzelnen Ping an einen Ziel-Server
- Misst die **Round-Trip-Time** (Latenz) mit hoher Genauigkeit über `time.time()`
- Erkennt Timeouts / Paketverluste
- Speichert Zeitstempel + Latenzwerte
- Zeigt live im Terminal die aktuelle Latenz oder „Zeitüberschreitung“
- Erstellt beim Beenden (Strg+C) einen **Matplotlib-Plot** mit:
  - blauer Linie = Latenzverlauf
  - rote vertikale Balken = erkannte Timeouts / Paketverluste

## Features

- Läuft auf **Windows** und **Linux/macOS** (automatische Erkennung des ping-Befehls)
- Sehr einfache Konfiguration über wenige Variablen am Anfang
- Visuelle Darstellung von Instabilitäten (Jitter, Paketverlust, Aussetzer)
- Keine externen Abhängigkeiten außer `matplotlib` (und den Standardmodulen)

## Voraussetzungen

```text
Python 3.6+
pip install matplotlib
