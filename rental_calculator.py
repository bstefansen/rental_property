HOUSE_PRICE = 300000
DOWN_PAYMENT = 20000
INTEREST_RATE = 0.04
MONTHLY_RENT = 2600 
MONTHLY_EXPENSES = 500



MONTHLY_INTEREST = (INTEREST_RATE * HOUSE_PRICE) / 12
annual_rent = MONTHLY_RENT*12
annual_expenses = MONTHLY_EXPENSES*12
annual_interest = MONTHLY_INTEREST*12
monthly_pmi = (0.01 * HOUSE_PRICE) / 12 if DOWN_PAYMENT < (HOUSE_PRICE * 0.2) else 0
annual_pmi = monthly_pmi * 12
total_expenses = annual_expenses + annual_interest + annual_pmi
noi = annual_rent - total_expenses
roi = (noi / DOWN_PAYMENT)*100
cap = (noi / HOUSE_PRICE)*100


print(f"HOUSE_PRICE: ${format(HOUSE_PRICE, '.2f')}")
print(f"DOWN_PAYMENT: ${format(DOWN_PAYMENT, '.2f')}")
print(f"MONTHLY_RENT: ${format(MONTHLY_RENT, '.2f')}")
print(f"MONTHLY_EXPENSES: ${format(MONTHLY_EXPENSES, '.2f')}")
print(f"MONTHLY_INTEREST: ${format(MONTHLY_INTEREST, '.2f')}")
print(f"MONTHLY_PMI: ${format(monthly_pmi, '.2f')}")
print()
print(f"TOTAL INCOME: ${format(annual_rent, '.2f')}")
print(f"TOTAL EXPENSES: ${format(total_expenses, '.2f')}")
print(f"ANNUAL NOI: ${format(noi, '.2f')}")
print(f"ROI: {format(roi, '.2f')}%")
print(f"CAP: {format(cap, '.2f')}%")

