sum_of_even_terms = 0
fib1 = 0
fib2 = 1
term = 0


while term < 4000000+1:
    term = fib1 + fib2
    if term % 2 == 0:
        sum_of_even_terms += term
    fib1 = fib2
    fib2 = term

print(sum_of_even_terms)

    
