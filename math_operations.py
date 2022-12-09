def math_operations(*args, a, s, d, m):
    nums = [float(x) for x in args]
    count = 0
    dict = {"a": a, "s": s, "d": d, "m": m}
    for i in nums:
        count += 1
        if count == 1:
            dict["a"] += i
        elif count == 2:
            dict["s"] -= i
        elif count == 3 and i == 0:
            pass
        elif count == 3 and i != 0:
            dict["d"] = d / i
        elif count == 4:
            count = 0
            dict["m"] = i * m

    result = sorted(dict.items(), key = lambda kv: (-kv[1], kv[0]))
    out = ''
    for key, value in result:
        out += f"{key}: {value:.1f}\n"

    return out

