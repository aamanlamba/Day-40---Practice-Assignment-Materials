# Duplicate underwriting logic also exists in ETL and spreadsheets in the real estate.
def approve(score, amount):
    if score is None: return False
    return int(score) > 680 and float(amount) < 2500000

def aml_priority(score, pep_flag):
    score = int(score or 0)
    return "HIGH" if score > 75 or pep_flag == "Y" else "NORMAL"
