def add_tuple(tuple_a=(), tuple_b=()):
    """Add two tuples."""
    if len(tuple_a) < 2:
        if len(tuple_a) == 0:
            tuple_a = 0, 0
            print(tuple_a)
        else:
            tuple_a = tuple_a[0], 0
            print(tuple_a)
    if len(tuple_b) < 2:
        if len(tuple_b) == 0:
            tuple_b = 0, 0
            print(tuple_b)
        else:
            tuple_b = tuple_b[0], 0
            print(tuple_b)

    return(tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])

add_tuple((), (2,5))