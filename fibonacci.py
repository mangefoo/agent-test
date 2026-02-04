def fibonacci(n):
    """
    Generate a list containing the fibonacci sequence up to the nth number.
    
    Args:
        n (int): The number of fibonacci numbers to generate
        
    Returns:
        list: A list containing the first n fibonacci numbers
    """
    if n <= 0:
        return []
    elif n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    
    # Initialize the sequence with the first two fibonacci numbers
    fib_sequence = [1, 1]
    
    # Generate the remaining fibonacci numbers
    for i in range(2, n):
        next_fib = fib_sequence[i-1] + fib_sequence[i-2]
        fib_sequence.append(next_fib)
    
    return fib_sequence