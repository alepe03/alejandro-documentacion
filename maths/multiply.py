def multiply(*args):
    """
    Multiplica de forma secuencial todos los números pasados como argumento.

    Parameters
    ----------
    *args : int o float
        Números a multiplicar.

    Returns
    -------
    int o float
        El producto de todos los números.

    Examples
    --------
    >>> multiply(2, 3, 4)
    24
    >>> multiply(5, 2)
    10
    """
    result = 1
    for num in args:
        result *= num
    return result
