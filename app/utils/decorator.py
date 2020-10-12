import traceback


def debug_out_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"{'=' * 10}  {func.__name__} {'=' * 10}")
        result = None
        try:
            result = func(*args, **kwargs)
            print(result.status_code, result.text)
        except:
            traceback.print_exc()
        print(f"{'=' * 30}", end="\n\n")
        return result

    return wrapper
#
#
# def debug_out_decorator(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return result
#
#     return wrapper
