# StackFuel Referenzprojekt

Willkommen zum StackFuel Referenzprojekt! Dieses Projekt dient als Leitfaden für Teilnehmende unseres Projekt-Portfolio-Kurses, um ein eigenes Data Science oder Data Analytics Projekt umzusetzen. Es bietet eine Vorlage und Beispielcode, an dem Sie sich orientieren können.

## Inhaltsverzeichnis

- [Projektüberblick](#projektüberblick)
- [Projektstruktur](#projektstruktur)
- [Voraussetzungen](#voraussetzungen)
- [Installation](#installation)
- [Daten herunterladen](#daten-herunterladen)
- [Explorative Datenanalyse (EDA)](#explorative-datenanalyse-eda)
- [Modellierung und Pipeline](#modellierung-und-pipeline)
- [Hyperparameter-Optimierung](#hyperparameter-optimierung)
- [Testen](#testen)
- [Verwendete Technologien und Bibliotheken](#verwendete-technologien-und-bibliotheken)
- [Anleitung für Teilnehmende](#anleitung-für-teilnehmende)

---

## Projektüberblick

In diesem Projekt analysieren wir Flugpreisdaten, um Einblicke in Preisstrukturen und Einflussfaktoren zu gewinnen. Dies beinhaltet die Datenbeschaffung, Datenvorverarbeitung, explorative Datenanalyse, Modellierung, Hyperparameter-Optimierung und Testen von Komponenten.

## Projektstruktur

Die Projektstruktur ist wie folgt organisiert:

```
StackFuel_Referenzprojekt/
├── .venv/
├── .vscode/
├── data/
├── .gitignore
├── .python-version
├── BaseModel.ipynb
├── Download_kagglehub.py
├── EDA_flight_prices.ipynb
├── PCA_pretest.ipynb
├── pipelines.py
├── pyproject.toml
├── README.md
├── Test_HyperparameterOptimization.ipynb
├── test_pipelines.py
└── uv.lock
```

- **`.venv/`**: Virtuelle Python-Umgebung für das Projekt.
- **`.vscode/`**: Einstellungen von Visual Studio Code für das Projekt.
- **`data/`**: Ordner für die heruntergeladenen Datensätze.
- **`.gitignore`**: Definiert, welche Dateien von der Versionskontrolle ausgeschlossen werden.
- **`.python-version`**: Spezifiziert die Python-Version (>=3.13).
- **`BaseModel.ipynb`**: Notebook zur Implementierung eines Basis-Modells mit Verwendung der Pipeline.
- **`Download_kagglehub.py`**: Skript zum Herunterladen der Datensätze von Kaggle.
- **`EDA_flight_prices.ipynb`**: Jupyter Notebook für die explorative Datenanalyse.
- **`PCA_pretest.ipynb`**: Notebook zur Voruntersuchung mittels Hauptkomponentenanalyse.
- **`pipelines.py`**: Enthält eine Beispiel-Pipeline für die Datenvorverarbeitung inklusive Column Transformer.
- **`pyproject.toml`**: Projektkonfigurationsdatei mit Abhängigkeiten.
- **`README.md`**: Diese Dokumentation.
- **`Test_HyperparameterOptimization.ipynb`**: Notebook zur Demonstration der Hyperparameter-Optimierung mit Optuna.
- **`test_pipelines.py`**: Testskript für die Pipeline-Funktionen unter Verwendung von pytest.
- **`uv.lock`**: Lock-Datei für den Paketmanager uv.

## Voraussetzungen

Für dieses Projekt benötigen Sie Python und den Paketmanager uv. Alle weiteren Abhängigkeiten sind in der `pyproject.toml` Datei bzw. in der `uv.lock` dokumentiert.

Du kannst Python von der offiziellen Homepage [python.org](https://www.python.org/) herunterladen und installieren. Alternativ kannst du auch einen Packetmanager wie Homebrew (MacOS), winget (Windows) oder apt (Ubuntu) nutzen.

- **Python**: Stellen Sie sicher, dass Sie Python Version 3.13 oder höher installiert haben.
- **uv**: Installieren Sie uv gemäß den Anweisungen auf der offiziellen GitHub-Seite: [uv on GitHub](https://github.com/astral-sh/uv)

#### macOS

1. **Homebrew installieren** (falls nicht bereits installiert):
   
   Öffnen Sie das Terminal und führen Sie folgenden Befehl aus:

   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

2. **uv installieren**:

   Nachdem Homebrew installiert ist, führen Sie folgenden Befehl im Terminal aus:

   ```bash
   brew install uv
   ```


#### Linux

Installieren Sie Python und uv mit ihrem jeweiligen Packetmanager.

Für Debian/Ubuntu mit:

```bash
sudo apt update
sudo apt install python3 python3-pip
pip3 install uv
```

#### Windows

1. **Winget installieren** (falls nicht bereits installiert):

   Winget ist in den neuesten Windows-Versionen standardmäßig installiert. Andernfalls installieren Sie es über den [Microsoft Store App Installer](https://apps.microsoft.com/store/detail/9NBLGGH4NNS1).

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
   uv sync
   ```

   Dies erstellt die virtuelle Umgebung im Ordner `.venv` und installiert alle benötigten Pakete gemäß `pyproject.toml`.

## Daten herunterladen

Führen Sie das Skript `Download_kagglehub.py` aus, um den Datensatz herunterzuladen:

```bash
uv run Download_kagglehub.py
```

Dies lädt den Datensatz von Kaggle herunter und verschiebt die Dateien in den Ordner `data/`.

## Explorative Datenanalyse (EDA)

Öffnen Sie das Notebook `EDA_flight_prices.ipynb` in VS Code oder Jupyter und führen Sie es aus, um eine erste Analyse des Datensatzes durchzuführen.

## Modellierung und Pipeline

- **`pipelines.py`**: Enthält eine beispielhafte Preprocessing-Pipeline inklusive Column Transformer.
- **`BaseModel.ipynb`**: Demonstriert die Verwendung der Pipeline zur Erstellung eines Basis-Modells.
- **`PCA_pretest.ipynb`**: Führt eine Hauptkomponentenanalyse durch, um die Dimensionalität der Daten zu reduzieren.

## Hyperparameter-Optimierung

- **`Test_HyperparameterOptimization.ipynb`**: Zeigt, wie man mit Optuna eine Hyperparameter-Optimierung durchführt, um die Modellleistung zu verbessern.

## Testen

- **`test_pipelines.py`**: Enthält Tests für die Pipeline-Funktionen unter Verwendung von pytest.
- **Tests ausführen**:

  ```bash
  uv run -m pytest
  ```

  Dies führt die Tests aus und stellt sicher, dass die Pipeline-Komponenten korrekt funktionieren.

## Verwendete Technologien und Bibliotheken

- **Python 3.13**: Programmiersprache.
- **uv**: Paketmanager für Python.
- **Jupyter Notebook**: Interaktive Entwicklungsumgebung.
- **Pandas**: Datenanalyse und -manipulation.
- **NumPy**: Numerische Berechnungen.
- **Matplotlib & Seaborn**: Datenvisualisierung.
- **Scikit-Learn**: Maschinelles Lernen.
- **Statsmodels**: Statistische Modellierung.
- **kagglehub**: Vereinfachtes Herunterladen von Kaggle-Datensätzen.
- **tqdm**: Fortschrittsbalken für Schleifen.
- **Optuna**: Hyperparameter-Optimierung.
- **Plotly**: Interaktive Visualisierungen.
- **pytest**: Framework zum Testen von Python-Code.

## Anleitung für Teilnehmende

- **Anpassung des Projekts**: Nutzen Sie dieses Projekt als Vorlage und passen Sie es an Ihre eigenen Anforderungen an.
- **Erweiterung der Analyse**: Fügen Sie weitere Analyseschritte oder Visualisierungen hinzu.
- **Modellierung**: Entwickeln Sie eigene Modelle und experimentieren Sie mit verschiedenen Algorithmen.
- **Hyperparameter-Optimierung**: Nutzen Sie Optuna, um die Hyperparameter Ihrer Modelle zu optimieren.
- **Modularisierung**: Lagern Sie wiederverwendbaren Code in Module wie `pipelines.py` aus.
- **Testen**: Schreiben Sie Tests für Ihre Funktionen, um die Zuverlässigkeit Ihres Codes sicherzustellen.
- **Dokumentation**: Kommentieren Sie Ihren Code und dokumentieren Sie Ihre Ergebnisse ausführlich.

Wir wünschen dir viel Erfolg und Freude bei deinem Projekt!
