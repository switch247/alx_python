def safe_print_division(a, b):
    try:
        result = a / b
    except:
        result = None
    finally:
        print("Inside result: {}".format(result) )
    return result


if __name__ == "__main__":
    safe_print_division(5, 6)
