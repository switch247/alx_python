def best_score(a_dictionary):
    if a_dictionary:
        return max(a_dictionary.items())[1]
    return
if __name__ == "__main__":
    print(best_score({"2":3}))