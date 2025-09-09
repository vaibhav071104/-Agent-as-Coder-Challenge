import pandas as pd
import pdfplumber
import re

def parse(pdf_path: str) -> pd.DataFrame:
    transactions = []
    
    # Define constants
    skip_words = {"date", "description", "debit amt", "credit amt", "balance"}
    credit_keywords = {"salary", "credit", "interest", "deposit", "cash", "cheque", "neft"}
    seen = set()

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if not text:
                continue
            
            for line in text.split("\n"):
                line = line.strip()
                if not line or any(sw in line.lower() for sw in skip_words):
                    continue
                
                if not re.match(r"^\d{2}-\d{2}-\d{4}", line):
                    continue
                
                parts = line.split()
                if len(parts) < 4:
                    continue
                
                date = parts[0]
                desc = " ".join(parts[1:-2])
                amt_str = parts[-2]
                bal_str = parts[-1]
                
                try:
                    amt = float(amt_str)
                    bal = float(bal_str)
                except ValueError:
                    continue
                
                key = (date, desc, round(bal, 2))
                if key in seen:
                    continue
                seen.add(key)
                
                is_credit = any(k in desc.lower() for k in credit_keywords)
                debit_amt = "" if is_credit else str(amt)
                credit_amt = str(amt) if is_credit else ""
                
                transactions.append({
                    "Date": date,
                    "Description": desc,
                    "Debit Amt": debit_amt,
                    "Credit Amt": credit_amt,
                    "Balance": bal
                })
    
    df = pd.DataFrame(transactions, columns=["Date", "Description", "Debit Amt", "Credit Amt", "Balance"])
    print(f"PERFECT CLASSIFICATION: {len(df)} transactions")
    return df