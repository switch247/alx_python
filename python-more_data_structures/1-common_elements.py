def common_elements(set_1, set_2):
    return set(filter(lambda x: x in set_1, set_2))


if __name__ == "__main__":
    print(common_elements( (1,2,3),(2,6,7) ) )

    # lambda x: (float(5)/9)*(x-32)