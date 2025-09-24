def subtract(*args):
    """
    Resta de forma secuencial todos los números pasados como argumento.

    Parameters
    ----------
    *args : int o float
        Números a restar.

    Returns
    -------
    int o float
        El resultado de restar los números en orden.

    Examples
    --------
    >>> subtract(100, 20, 30, 40)
    10
    >>> subtract(10, 3)
    7
    """
    if not args:
        raise ValueError("Debe proporcionar al menos un número")
    result = args[0]
    for num in args[1:]:
        result -= num
    return result
