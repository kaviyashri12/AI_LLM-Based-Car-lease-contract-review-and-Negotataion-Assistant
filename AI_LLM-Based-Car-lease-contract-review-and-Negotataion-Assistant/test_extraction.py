#!/usr/bin/env python3
"""Test script to verify contract field extraction"""

import re

def test_extraction():
    # Read the sample contract with proper encoding
    with open('sample_honda_contract.txt', 'r', encoding='utf-8', errors='ignore') as f:
        text = f.read()

    # Test the fixed regex patterns
    apr = re.search(r'(?:APR|annual.*?rate)[:\s]*([\d.]+)\s*%', text, re.I)
    term = re.search(r'(?:lease term|duration)[:\s]*(\d+)\s*(?:months|month)', text, re.I)
    monthly = re.search(r'(?:monthly(?:\s+)?payment|total monthly payment)[:\s]*\$?([\d,]+(?:\.\d{2})?)', text, re.I)
    down = re.search(r'(?:down\s+payment|cap\s+reduction)[:\s]*\$?([\d,]+(?:\.\d{2})?)', text, re.I)
    residual = re.search(r'(?:residual\s+value|buyout|purchase.*?price)[:\s]*\$?([\d,]+(?:\.\d{2})?)', text, re.I)
    mileage = re.search(r'(?:annual mileage allowance|miles\s+per\s+year)[:\s]*(\d+(?:,\d{3})*)', text, re.I)
    overage = re.search(r'(?:excess mileage charge)[:\s]*\$?([\d.]+)\s*(?:per|/)?\s*mile', text, re.I)
    warranty = re.search(r'(?:factory warranty|warranty period)[:\s]*([^\n]+)', text, re.I)

    results = {
        'APR (%)': apr.group(1) if apr else 'Not detected',
        'Lease Term (Months)': term.group(1) if term else 'Not detected',
        'Monthly Payment ($)': monthly.group(1) if monthly else 'Not detected',
        'Down Payment ($)': down.group(1) if down else 'Not detected',
        'Residual/Buyout ($)': residual.group(1) if residual else 'Not detected',
        'Annual Mileage': mileage.group(1) if mileage else 'Not detected',
        'Excess Mileage ($/mile)': overage.group(1) if overage else 'Not detected',
        'Warranty': warranty.group(1).strip()[:60] if warranty else 'Not detected'
    }

    print("\n📋 Extracted Contract Summary")
    print("=" * 50)
    print(f"{'Field':<25} {'Value':<25}")
    print("=" * 50)
    for key, value in results.items():
        print(f"{key:<25} {value:<25}")
    print("=" * 50)

if __name__ == '__main__':
    test_extraction()
