def age_assignment(*args, **kwargs):
    res = ''
    dict = sorted(kwargs.items(), key=lambda x:x[0])
    for k, v in dict:
        for val in args:
            if k == val[0]:
                res += f"{val} is {v} years old.\n"

    return res
