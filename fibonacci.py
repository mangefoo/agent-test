def fibonacci(n):
    """
    Generate fibonacci sequence up to the nth number.
    Returns a list containing the fibonacci sequence.
    
    Args:
        n (int): The position up to which to generate fibonacci numbers
        
    Returns:
        list: List of fibonacci numbers up to position n
    """
    if n <= 0:
        return []
    elif n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    
    # Initialize the sequence with first two fibonacci numbers
    fib_sequence = [1, 1]
    
    # Generate remaining fibonacci numbers
    for i in range(2, n):
        next_fib = fib_sequence[i-1] + fib_sequence[i-2]
        fib_sequence.append(next_fib)
    
    return fib_sequence