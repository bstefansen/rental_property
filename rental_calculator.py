
HOUSE_PRICE = 250_000
DOWN_PAYMENT = 50_000
MONTHLY_RENT = 2000 
MONTHLY_EXPENSES = 500
MONTHLY_INTEREST = 830



annual_rent = MONTHLY_RENT*12
annual_expenses = MONTHLY_EXPENSES*12
annual_interest = MONTHLY_INTEREST*12
noi = annual_rent - annual_expenses - annual_interest
roi = (noi / DOWN_PAYMENT)*100
cap = (noi / HOUSE_PRICE)*100


print(f"HOUSE_PRICE: {HOUSE_PRICE}")
print(f"DOWN_PAYMENT: {DOWN_PAYMENT}")
print(f"MONTHLY_RENT: {MONTHLY_RENT}")
print(f"MONTHLY_EXPENSES: {MONTHLY_EXPENSES}")
print(f"MONTHLY_INTEREST: {MONTHLY_INTEREST}")
print()
print(f"NOI: {noi}")
print(f"ROI: {format(roi, '.2f')}%")
print(f"CAP: {format(cap, '.2f')}%")
