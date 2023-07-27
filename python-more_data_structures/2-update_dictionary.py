def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value
    for i,v in a_dictionary.items():
        print("{}: {}".format(i,v))
if __name__ == "__main__":
    update_dictionary({"k":"v"}, "key", "value")