def fibonacci_sequence(n):
    sequence = [0, 1]  # Initialize the sequence with the first two numbers
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return sequence
    for i in range(2, n):
        next_number = sequence[i-1] + sequence[i-2]
        sequence.append(next_number)
    return sequence
