# Source and license

Optional public dataset: Daqing Chen (2015), Online Retail, UCI Machine Learning Repository.
https://archive.ics.uci.edu/dataset/352/online+retail
DOI: https://doi.org/10.24432/C5BW33
Dataset license: CC BY 4.0, as listed by UCI. MIT covers our code, not the external dataset.
Download Online Retail.xlsx from UCI and set RETAIL_DATASET to its local path. Raw files are ignored.
No external dataset is redistributed here. The bundled reproducible run uses fictional transactions.

The real dataset records GBP transactions and includes cancellations and customer identifiers.
The loader excludes cancellations, nonpositive amounts and missing identifiers for this exercise;
therefore results describe positive-purchase activity, not net revenue after returns.
Do not publish raw customer IDs or label these historic transactions as current market data.

No acquisition spend, gross margin or full customer lifetime is supplied. CAC and margin-based LTV
are explicitly hypothetical sensitivity inputs, not measurements from this dataset.
