def add(*args):
    """
    Devuelve la suma de todos los números pasados como argumento.

    Parameters
    ----------
    *args : int o float
        Números a sumar.

    Returns
    -------
    int o float
        La suma de todos los números.

    Examples
    --------
    >>> add(2, 3, 5)
    10
    >>> add(1, 2)
    3
    """
    return sum(args)
