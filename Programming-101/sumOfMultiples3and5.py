counter = 1
sum_of_multiples = 0
while counter < 1000:
    if counter % 3 == 0 or counter % 5 == 0:
        sum_of_multiples += counter
    counter += 1
    
print(sum_of_multiples)