def fibonacci(n):
    """
    Calculate the nth fibonacci number using iterative approach.
    
    Args:
        n (int): Position in fibonacci sequence (0-indexed)
        
    Returns:
        int: The nth fibonacci number
    """
    if n < 0:
        raise ValueError("Fibonacci sequence is not defined for negative numbers")
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    # Use iterative approach for better performance
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    
    return b