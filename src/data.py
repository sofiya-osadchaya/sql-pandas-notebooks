from pathlib import Path
import pandas as pd

def load_transactions(path=None):
    # External data are optional and never silently presented as synthetic observations.
    if path and Path(path).exists():
        p=Path(path);raw=pd.read_excel(p) if p.suffix==".xlsx" else pd.read_csv(p)
        data=raw.rename(columns={"InvoiceNo":"invoice","InvoiceDate":"date","CustomerID":"customer","Quantity":"quantity","UnitPrice":"unit_price","StockCode":"product"})
        return clean(data),"UCI Online Retail (user-downloaded public file)"
    rows=[]
    for month in range(1,7):
        for customer in range(1,31):
            if customer%4==month%4:continue
            rows.append({"invoice":f"SYN-{month}-{customer}","date":f"2026-{month:02}-10","customer":f"SYN-C{customer}","quantity":1+customer%3,"unit_price":20+customer,"product":f"P{customer%5}"})
    return clean(pd.DataFrame(rows)),"Synthetic fallback fixture, not open-data results"

def clean(data):
    required={"invoice","date","customer","quantity","unit_price","product"}
    if not required<=set(data):raise ValueError("Missing retail columns")
    data=data.dropna(subset=list(required)).copy()
    data["date"]=pd.to_datetime(data["date"])
    data=data[(data["quantity"]>0)&(data["unit_price"]>0)&(~data["invoice"].astype(str).str.upper().str.startswith("C"))]
    data["revenue"]=data["quantity"]*data["unit_price"]
    return data
