def func_executor(*args):
    result = ""
    for func, arg in args:
        func_result = func(*arg)
        result += f"{func.__name__} - {func_result}\n"
    return result
