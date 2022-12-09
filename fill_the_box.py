def fill_the_box(*args):
    limit = args[0] * args[1] * args[2]
    i = 3
    while args[i] != "Finish":
        limit -= args[i]
        i += 1
    if limit > 0:
        return f"There is free space in the box. You could put {limit} more cubes."
    return f"No more free space! You have {abs(limit)} more cubes."
