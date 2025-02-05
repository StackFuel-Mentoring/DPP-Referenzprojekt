# StackFuel Referenzprojekt

Willkommen zum StackFuel Referenzprojekt! Dieses Projekt dient als Leitfaden für Teilnehmende unsere Projekt-Portfolio Kurses, um ein eigenes Data Science oder Data Analytics Projekt umzusetzen. Es bietet eine Vorlage und Beispielcode, an dem Sie sich orientieren können.

## Inhaltsverzeichnis

- [Projektüberblick](#projektüberblick)
- [Projektstruktur](#projektstruktur)
- [Voraussetzungen](#voraussetzungen)
- [Installation](#installation)
- [Daten herunterladen](#daten-herunterladen)
- [Explorative Datenanalyse (EDA)](#explorative-datenanalyse-eda)
- [Verwendete Technologien und Bibliotheken](#verwendete-technologien-und-bibliotheken)
- [Anleitung für Teilnehmer](#anleitung-für-teilnehmer)
- [Kontakt](#kontakt)

---

## Projektüberblick

In diesem Projekt analysieren wir Flugpreisdaten, um Einblicke in Preisstrukturen und Einflussfaktoren zu gewinnen. Dies beinhaltet die Datenbeschaffung, Datenvorverarbeitung, explorative Datenanalyse und ggf. Modellierung.

## Projektstruktur

Die Projektstruktur ist wie folgt organisiert:

```
StackFuel_Referenzprojekt/
├── .venv/
├── data/
├── .gitignore
├── .python-version
├── Download_kagglehub.py
├── EDA_flight_prices.ipynb
├── pyproject.toml
├── README.md
└── uv.lock
```

- **.venv/**: Virtuelle Python Umgebung für das Projekt. (Wird durch `uv init` erstellt und von git ignoriert)
- **data/**: Ordner für die heruntergeladenen Datensätze. (Wird durch das Script `Download_kagglehub.py` erstellt)
- **.gitignore**: Definiert, welche Dateien von der Versionskontrolle ausgeschlossen werden.
- **.python-version**: Spezifiziert die Python-Version (>=3.13).
- **Download_kagglehub.py**: Skript zum Herunterladen der Datensätze von Kaggle.
- **EDA_flight_prices.ipynb**: Jupyter Notebook für die explorative Datenanalyse.
- **pyproject.toml**: Projektkonfigurationsdatei mit Abhängigkeiten.
- **README.md**: Diese Dokumentation.
- **uv.lock**: Lock-Datei für den Paketmanager uv.

## Voraussetzungen

Für dieses Projekt benötigen Sie Python und den Paketmanager uv.

### macOS

1. **Homebrew installieren** (falls nicht bereits installiert):
   
   Öffnen Sie das Terminal und führen Sie folgenden Befehl aus:

   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

2. **uv installieren**:

   Nachdem Homebrew installiert ist, führen Sie:

   ```bash
   brew install uv
   ```

### Linux

Installieren Sie Python und uv mit ihrem jeweiligen Packetmanager.

Für Debian/Ubuntu mit:

   ```bash
   sudo apt update
   sudo apt install python3 python3-pip
   pip3 install uv
   ```


### Windows

1. **Winget installieren** (falls nicht bereits installiert):

   Winget ist in den neuesten Windows-Versionen standardmäßig installiert. Andernfalls holen Sie es sich über das [Microsoft Store App Installer](https://apps.microsoft.com/store/detail/9NBLGGH4NNS1).

2. **uv installieren**:

   Öffnen Sie PowerShell und führen Sie folgenden Befehl aus:

   ```powershell
   winget install astral-sh.uv
   ```

Sobald Python und uv installiert sind, können Sie das Projekt initialisieren und die Abhängigkeiten mit uv installieren.

## Installation

1. **Repository klonen**

   Klonen Sie das Repository oder laden Sie es als ZIP-Datei herunter:

   ```bash
   git clone <REPOSITORY_URL>
   cd DPP-Referenzprojekt
   ```



2. **Virtuelle Umgebung einrichten**

   Initialisieren Sie die virtuelle Umgebung und installieren Sie die Abhängigkeiten:

   ```bash
   uv init
   ```

   Dies erstellt die virtuelle Umgebung im Ordner `.venv` und installiert alle benötigten Pakete gemäß `pyproject.toml`.

## Daten herunterladen

Führen Sie das Skript `Download_kagglehub.py` aus, um den Datensatz herunterzuladen:

```bash
uv run Download_kagglehub.py
```

Dies lädt den Datensatz von Kaggle herunter und verschiebt die Dateien in den Ordner `data/`.

## Explorative Datenanalyse (EDA)

Die Datei `EDA_flight_prices.ipynb` stellt eine Beispielhafte EDA an dem Datensatz dar. Öffne das Notebook in VS-Code oder Jupyter und führe es aus.

## Verwendete Technologien und Bibliotheken

- **Python 3.13**: Programmiersprache.
- **uv**: Paketmanager für Python.
- **Jupyter Notebook**: Interaktive Entwicklungsumgebung.
- **Pandas**: Datenanalyse und -manipulation.
- **NumPy**: Numerische Berechnungen.
- **Matplotlib & Seaborn**: Datenvisualisierung.
- **Scikit-Learn**: Maschinelles Lernen (optional).
- **tqdm**: Fortschrittsbalken für Loops.
- **Statsmodels**: Statistische Modellierung.
- **kagglehub**: Vereinfachtes Herunterladen von Kaggle-Datensätzen.

## Anleitung für Teilnehmer

- **Anpassung des Projekts**: Nutzen Sie dieses Projekt als Vorlage und passen Sie es an Ihre eigenen Anforderungen an.
- **Erweiterung der Analyse**: Fügen Sie weitere Analyseschritte oder Visualisierungen hinzu.
- **Modellierung**: Optional können Sie Vorhersagemodelle erstellen und evaluieren.
- **Dokumentation**: Kommentieren Sie Ihren Code und halten Sie Ihre Ergebnisse fest.


Wir wünschen Ihnen viel Erfolg und Freude bei Ihrem Projekt!