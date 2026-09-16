#!/usr/bin/env python3

"""
Pay Check Calculator

Program calculates net pay based upon hours worked, hourly rate, and taxes paid.
"""

print("Pay Check Calculator")
print(
    "Program calculates net pay based upon hours worked, "
    "hourly rate, and taxes paid."
)

print("\nProgram Requirements:")
print("Developer: Khushi Patel")
print("1. Must use float data type for user input.")
print("2. Must round calculations to two decimal places.")
print("3. Must format currency with dollar sign and two decimal places.")

# Input
print("\nUser Input:")

hours = float(input("Hours Worked: "))
hourly_rate = float(input("Hourly Rate: $"))
tax_rate = float(input("Tax Rate (percent): "))

# Process
gross_pay = hours * hourly_rate
tax_amount = gross_pay * (tax_rate / 100)
net_pay = gross_pay - tax_amount

# Output
print("\nProgram Output:")

print(f"Gross Pay: ${gross_pay:,.2f}")
print(f"Tax Rate: {tax_rate:.2f}%")
print(f"Tax Amount: ${tax_amount:,.2f}")
print(f"Net Pay: ${net_pay:,.2f}")

