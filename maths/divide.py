def divide(*args):
    """
    Divide de forma secuencial todos los números pasados como argumento.

    Parameters
    ----------
    *args : int o float
        Números a dividir.

    Returns
    -------
    int o float
        El resultado de dividir los números en orden.

    Examples
    --------
    >>> divide(100, 2, 5)
    10.0
    >>> divide(20, 2)
    10.0
    """
    if not args:
        raise ValueError("Debe proporcionar al menos un número")
    result = args[0]
    for num in args[1:]:
        if num == 0:
            raise ZeroDivisionError("No se puede dividir entre cero")
        result /= num
    return result
