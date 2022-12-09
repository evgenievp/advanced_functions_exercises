def grocery_store(**kwargs):
    dict = sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
    res = ''
    for val in dict:
        res += f"{val[0]}: {val[1]}\n"

    return res
