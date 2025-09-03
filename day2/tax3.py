'''Level 3: Tax and Rebate Calculation
Objective: Compute tax payable using the New Tax Regime (2023) slabs.
Tasks:
1. Calculate tax based on the following slabs:
o ₹0 - ₹3,00,000: 0%
o ₹3,00,001 - ₹6,00,000: 5%
o ₹6,00,001 - ₹9,00,000: 10%
o ₹9,00,001 - ₹12,00,000: 15%
o ₹12,00,001 - ₹15,00,000: 20%
o Above ₹15,00,000: 30%
2. Apply Section 87A Rebate:
o Taxable income ≤ ₹7,00,000 → 100% rebate (tax payable = ₹0).
3. Add a 4% Health and Education Cess to the calculated tax.
Output:
• Display a detailed tax breakdown, including slabs, cess, and total tax payable.'''



import tax2 as t2

section_87A_rebate = True

tax_amount = 0
tax_percentage = 0
if t2.taxable_income >= 0 and t2.taxable_income <= 3_00_000:
    pass
elif t2.taxable_income <= 6_00_000:
    tax_percentage = 0.05
elif t2.taxable_income <= 9_00_000:
    tax_percentage = 0.1
elif t2.taxable_income <= 12_00_000:
    tax_percentage = 0.15
elif t2.taxable_income <= 15_00_000:
    tax_percentage = 0.2
else:
    tax_percentage = 0.3

tax_amount = t2.taxable_income * tax_percentage
cess_amount = tax_amount * 0.04
total_tax_amount = tax_amount + cess_amount

print(
'''
₹0 - ₹3,00,000: 0%
o ₹3,00,001 - ₹6,00,000: 5%
o ₹6,00,001 - ₹9,00,000: 10%
o ₹9,00,001 - ₹12,00,000: 15%
o ₹12,00,001 - ₹15,00,000: 20%
o Above ₹15,00,000: 30%
'''
)
print(f'Cess Amount      = {cess_amount}')
if section_87A_rebate and t2.taxable_income <= 7_00_000:
    print(f'Total Tax Amount = 0')
else:
    print(f'Total Tax Amount = {total_tax_amount}')