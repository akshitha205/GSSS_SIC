'''Level 4: Net Salary Calculation
Objective: Calculate annual net salary after tax deductions.
Tasks:
1. Compute Net Salary = Annual Gross Salary - Total Tax Payable.
2. Display:
o Annual Gross Salary
o Total Tax Payable (including cess)
o Annual Net Salary'''

import tax1 as t1 , tax3 as t3

annual_net_salary = t1.annual_gross_salary - t3.total_tax_amount
print(f'The annual net salary of the employee = {annual_net_salary}')