def best_score(a_dictionary):
    if a_dictionary:
        return max(a_dictionary.items())[0]
    return
if __name__ == "__main__":
    print(best_score({'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}))