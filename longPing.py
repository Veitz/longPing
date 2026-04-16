import subprocess
import time
import matplotlib.pyplot as plt
from datetime import datetime

# --- EINSTELLUNGEN ---
TARGET = "8.8.8.8"  # Ziel-Server (Google DNS)
INTERVALL = 1        # Sekunden zwischen den Pings
# ---------------------

timestamps = []
latencies = []

print(f"Starte Langzeit-Ping-Test für {TARGET}...")
print("Beenden und Plot anzeigen mit STRG + C")

try:
    while True:
        now = datetime.now().strftime("%H:%M:%S")
        
        # Ping-Befehl absetzen (Windows: -n, Linux/Mac: -c)
        try:
            # Wir nutzen subprocess für präzisere Zeitmessung der Antwort
            start = time.time()
            output = subprocess.run(
                ["ping", "-n", "1", TARGET] if subprocess.os.name == 'nt' else ["ping", "-c", "1", TARGET],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                encoding='cp850'  # <--- Diese Zeile ist entscheidend für Windows
            )
            end = time.time()
            
            if output.returncode == 0:
                ms = (end - start) * 1000
                print(f"[{now}] Antwort von {TARGET}: {ms:.2f} ms")
                latencies.append(ms)
            else:
                print(f"[{now}] Zeitüberschreitung (Timeout)")
                latencies.append(None) # Markierung für Paketverlust
            
            timestamps.append(now)
            
        except Exception as e:
            print(f"Fehler: {e}")
            
        time.sleep(INTERVALL)

except KeyboardInterrupt:
    print("\nTest beendet. Erstelle Plot...")

    # Plot erstellen
    plt.figure(figsize=(12, 6))
    
    # Lücken bei Timeouts (None) im Plot behandeln
    plt.plot(timestamps, latencies, marker='.', linestyle='-', color='b', label='Latenz in ms')
    
    # Paketverluste (Timeouts) rot markieren
    for i, val in enumerate(latencies):
        if val is None:
            plt.axvline(x=i, color='r', alpha=0.3, label='Timeout' if i == 0 else "")

    plt.title(f"Ping-Stabilitätstest für {TARGET}")
    plt.xlabel("Uhrzeit")
    plt.ylabel("Latenz (ms)")
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    
    # X-Achse lesbar machen (nur jeden n-ten Zeitstempel zeigen)
    n = max(1, len(timestamps) // 10)
    plt.xticks(timestamps[::n], rotation=45)
    
    plt.tight_layout()
    plt.show()
