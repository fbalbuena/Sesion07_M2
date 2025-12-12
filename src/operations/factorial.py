def factorial(x: int) -> int:
    """
    Esta función calcula el factorial de un número no negativo 'x'
    """
    if x < 0:
        raise ValueError("Factorial no definido para números negativos")
    output = 1
    for i in range(2, x + 1):
        output *= i
    return output
