'''Taxation Problem:

Tax Calculator Problem
GlobalNext Solutions, a rapidly growing IT company, employs a diverse workforce ranging from entry-
level developers to senior executives. The HR department wants to streamline the tax calculation
process for employees under the New Tax Regime (2023). They’ve decided to build a tax calculation
program that computes salaries, taxes, and net incomes while ensuring compliance with the latest tax
laws.
As a software developer in GlobalNext’s HR-Tech team, you are tasked with developing this program.
The system should process employee salary details, validate inputs, calculate taxes, and generate
detailed reports.
The program should:
1. Accept employee details, including monthly salary components.
2. Calculate gross and taxable income according to the New Tax Regime (2023).
3. Compute the tax payable using the appropriate tax slabs.
4. Apply any applicable standard deductions and rebates.
5. Generate reports detailing gross salary, taxable income, tax payable, and net salary.
Level 1: Basic Input and Salary Calculation
Objective: Capture employee details and calculate the gross salary.
Tasks:
• Accept the following inputs for an employee:
o Name
o EmpID
o Basic Monthly Salary
o Special Allowances (Monthly)
o Bonus Percentage (Annual Bonus as % of Monthly Gross Salary)
• Calculate:
o Gross Monthly Salary = Basic Salary + Special Allowances
o Annual Gross Salary = (Gross Monthly Salary × 12) + Bonus
• Output:
o Display the employee details, gross monthly salary, and annual gross salary.
'''

print("Enter the details of the employee")
emp_name = input("Name of an employee: ")
emp_id = input("Employee ID: ")
emp_salary = int(input("Enter your Basic Monthly Salary: "))
emp_allowances = int(input("Enter your Special Allowances (Monthly): "))

emp_bonus = int(input("Enter your Bonus Percentage: "))
emp_bonus_percent = emp_bonus / 100

gross_monthly_salary = emp_salary + emp_allowances
annual_salary_without_bonus = gross_monthly_salary * 12
bonus_amount = annual_salary_without_bonus * emp_bonus_percent
annual_gross_salary = annual_salary_without_bonus + bonus_amount

print("Name of the employee:", emp_name)
print("Employee ID:", emp_id)
print("Salary of the employee:", emp_salary)
print("Special Allowances (Monthly) of the employee:", emp_allowances)
print("Bonus of the employee:", emp_bonus, "%")
print("Gross monthly salary of the employee is", gross_monthly_salary)
print("Annual gross salary of the employee is", annual_gross_salary)