def destructure_sequence(sequence):
    """Destructures a sequence into its first, second, and remaining elements.

    Args:
        sequence: The sequence to destructure.

    Returns:
        A tuple containing the first element, the second element, and the remaining elements.
    """

    first, second, *rest = sequence
    return first, second, rest

# Example usage
primes = [2, 3, 5, 7, 11, 13, 17, 19]
first, second, rest = destructure_sequence(primes)

print("First element:", first)
print("Second element:", second)
print("Rest:", rest)
