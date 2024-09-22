iterations = int(input("Enter the number of iterations: "))
sum_result = 0
n = 1

while n <= iterations:
    #3^n
    power_3n = 1
    i = 0
    while i < n:
        power_3n *= 3
        i += 1

    #n!
    factorial_n = 1
    i = 1
    while i <= n:
        factorial_n *= i
        i += 1

    #n^n
    power_nn = 1
    i = 0
    while i < n:
        power_nn *= n
        i += 1

    term = (power_3n * factorial_n) / power_nn
    sum_result += term

    print(f"After {n} iterations, the cumulative sum is: {sum_result}")
    n += 1
