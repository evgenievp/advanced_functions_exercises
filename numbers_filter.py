def even_odd_filter(**kwargs):
    odd, even = [], []
    for key, values in kwargs.items():
        if key == 'even':
            for v in values:
                if v % 2 != 0:
                    odd.append(v)
        elif key == 'odd':
            for v in values:
                if v % 2 == 0:
                    even.append(v)
    for v in odd:
        kwargs['even'].remove(v)
    for v in even:
        kwargs['odd'].remove(v)
    return kwargs
