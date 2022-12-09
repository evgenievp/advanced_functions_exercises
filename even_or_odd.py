def even_odd(*param):
    odd, even = [], []
    for i in range(len(param) - 1):
        if param[i] % 2 != 0:
            odd.append(param[i])
        else:
            even.append(param[i])
    if param[-1] == "even":
        return even
    return odd