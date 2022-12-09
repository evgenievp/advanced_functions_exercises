def positive_vs_negative(params):
    nums = [int(x) for x in params]
    sum_pos, sum_neg = 0, 0
    for num in nums:
        if num > 0:
            sum_pos += num
        elif num < 0:
            sum_neg += num
    res = ""
    res += f"{sum_neg}\n{sum_pos}\n"
    if abs(sum_neg) > sum_pos:
        res += f"The negatives are stronger than the positives"
    else:
        res += f"The positives are stronger than the negatives"
    return res


