
# pdfsplit

Ein einfaches CLI-Tool zum schnellen Aufteilen von PDF-Dateien oder eBooks in mehrere Kapitel-Subfiles, ohne den Umweg über „Drucken als PDF“ gehen zu müssen.

---

## Features

- Zerlegt PDFs anhand definierter Kapitelanfangsseiten.
- Überspringt optional Seiten am Dokumentanfang (Offset).
- Speichert die einzelnen Kapitel in einem neuen Ordner mit dem Namen der Original-PDF.

---

## Installation

```bash
/bin/python3 -m pip install git+https://github.com/kamexx/pdf_splitter.git@main
```

---

## Verwendung

1. Wechsle in das Verzeichnis, in dem sich deine PDF-Datei befindet:
   ```bash
   cd /pfad/zur/pdf
   ```

2. Führe das Skript mit den notwendigen Parametern aus:
   ```bash
   /bin/python3 -m pdfsplit.pdfsplit --filename "dateiname.pdf" --offset 0 --chapter 1 10 20 30
   ```

### Parameter

- `--filename`: Name der PDF-Datei (inkl. Endung).
- `--offset`: Anzahl der Seiten, die zu Beginn übersprungen werden sollen (Standard: 0).
- `--chapter`: Liste der Seitenzahlen, an denen ein neues Kapitel beginnt.

---

## Beispiel

```bash
cd my_pdf_collection/
  
/bin/python3 -m pdfsplit.pdfsplit --filename myscript.pdf --offset 18 --chapter 1 9 35 53 71 93 117 127 139 153 169
```

Das Skript erstellt einen neuen Ordner `myscript`, in dem die einzelnen Kapitel als separate PDF-Dateien abgelegt werden.

---

## Optional

Du kannst das Python-Paket auch in deinen `PATH` aufnehmen, um das Tool ohne den langen Aufruf `/bin/python3 -m pdfsplit.pdfsplit` verwenden zu können.

---

## Lizenz

MIT License  
(C) 2025 by kamexx

---

Bei Fragen oder Problemen gerne melden!
