# SQL and Pandas Notebooks

демо-реконструкция подхода на синтетических данных

Three notebooks: SQL JOIN/GROUP BY, purchase cohorts with right-censoring, and business-case unit
economics. Compatible with the public UCI Online Retail dataset; raw data are not redistributed.
The included executed checks use clearly labeled synthetic transactions, not a downloaded UCI file.

```bash
pip install -r requirements.txt
# Optional: export RETAIL_DATASET=/your/local/Online_Retail.xlsx
jupyter lab notebooks
```

See [source attribution and limitations](DATA_SOURCES.md). Revenue is observed within the sample
window; lifetime and acquisition spend are hypothetical. No claim of measured CAC/LTV from missing data.
Original code and synthetic fixtures are MIT; the optional UCI dataset has its own CC BY 4.0 license.
