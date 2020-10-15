good = .2
fair = .15
bad = .1

bill_amount = input('How much was the bill?\n')
service_quality = input('How good was the service? Select \'Good\', \'Fair\', \'Bad\'.\n')

bill_amount = int(bill_amount)

if service_quality == 'Good':
    tip_amount = bill_amount * good
elif service_quality == 'Fair':
    tip_amount = bill_amount * fair
else: 
    tip_amount = bill_amount * bad

total_bill = bill_amount + tip_amount
number_in_party = input('Split how many ways?')
number_in_party = int(number_in_party)

total_bill_split = total_bill/number_in_party

print(f'Total bill amount: {total_bill}')
print(f'Bill amount: {bill_amount}')
print(f'Level of service: {service_quality}')
print(f'Tip amount: {tip_amount}')
print(f'Split how many ways: {number_in_party}')
print(f'Amount per person: {total_bill_split}')





