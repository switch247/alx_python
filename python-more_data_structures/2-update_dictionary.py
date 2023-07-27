def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value
    return a_dictionary
    # for i,v in a_dictionary.items():
    #     print("{}: {}".format(i,v))
if __name__ == "__main__":
    print(update_dictionary({ "a": "a", } ,  "a" ,"A"))