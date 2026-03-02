def factorial(n):
    if not isinstance(n, int):
        return "Invalid Input"

    if n < 0:
        return "Invalid Input"

    if n == 0 or n == 1:
        return 1

    result = 1
    for i in range(1, n + 1):
        result *= i

    return result
