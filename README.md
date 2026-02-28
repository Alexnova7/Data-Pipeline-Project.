🚀 Simple Python ETL Pipeline

This project is a clean and organized **Data Engineering** template. It demonstrates a complete **ETL (Extract, Transform, Load)** workflow, designed to handle raw data and convert it into a clean, usable format.

---

### 📂 Project Structure

- **config/**: Contains `settings.py` for centralized management of file paths.
- **data/raw/**: The landing zone for original, untouched source data (`raw.csv`).
- **data/processed/**: The destination for high-quality, cleaned datasets (`clean.csv`).
- **scripts/**: Contains `etl.py`, which houses the core Python logic and data processing engine.

---

### ⚙️ How It Works

1. **Extract**: The system generates or retrieves raw data containing inconsistencies, extra spaces, and invalid entries.
2. **Transform**: Using the **Pandas** library, the pipeline performs:
   - **Data Cleaning**: Trimming leading/trailing whitespace from text.
      - **Normalization**: Converting usernames to a standard case format.
         - **Validation**: Filtering out records with corrupted dates or negative values.
         3. **Load**: The finalized data is saved as a structured CSV in the `processed` folder.

         ---

         ### 🛠️ Getting Started

         **Prerequisites**
         Ensure you have Python 3 and the Pandas library installed:
         ```bash
         pip install pandas