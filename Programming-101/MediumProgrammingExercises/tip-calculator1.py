good = .2
fair = .15
bad = .1

bill_amount = input('How much was the bill?\n')

service_quality = input('How good was the service? Select \'Good\', \'Fair\', \'Bad\'.\n')

bill_amount = int(bill_amount)

if service_quality.capitalize() == 'Good': 
    tip_amount = bill_amount * good
    total_amount = bill_amount + tip_amount
    print(f'Bill: {bill_amount}.')
    print(f'Level of service was {service_quality}.')
    print(f'Tip amount: {tip_amount}')
    print(f'Total amount: {total_amount}')
elif service_quality.capitalize() == 'Fair':
    tip_amount = bill_amount * fair
    total_amount = bill_amount + tip_amount
    print(f'Bill: {bill_amount}.')
    print(f'Level of service was {service_quality}.')
    print(f'Tip amount: {tip_amount}')
    print(f'Total amount: {total_amount}')
elif service_quality.capitalize() == 'Bad':
    tip_amount = bill_amount * bad
    total_amount = bill_amount + tip_amount
    print(f'Bill: {bill_amount}.')
    print(f'Level of service was {service_quality}.')
    print(f'Tip amount: {tip_amount}')
    print(f'Total amount: {total_amount}')

else: 
    print('You didn\'t give a valid response. Try again')



