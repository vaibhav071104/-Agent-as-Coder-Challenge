import pandas as pd
import pdfplumber
import re

import pandas as pd
import pdfplumber

def parse(pdf_path:
    skip_words = {'date', 'description', 'debit amt', 'credit amt', 'balance'}
    credit_keywords = {'salary', 'credit', 'interest', 'deposit', 'cash', 'cheque', 'neft'}
    seen = set()
 str) -> pd.DataFrame:
    with pdfplumber.open(pdf_path) as pdf:
        data = []
        for page in pdf.pages:
            for line in page.extract_text().splitlines():
                parts = line.split()
                if len(parts) >= 3:
                    date, desc, amount = parts[0:3]
                    if any(keyword in desc.lower() for keyword in credit_keywords):
                        credit_amt = float(amount)
                        debit_amt = 0
                    else:
                        debit_amt = float(amount)
                        credit_amt = 0
                    data.append({"Date": date, "Description": desc, "Debit Amt": debit_amt, "Credit Amt": credit_amt})
        return pd.DataFrame(data).head(100)