#!/usr/bin/env python3
"""
Main script that outputs greeting with fibonacci calculation.
"""

from fibonacci import fibonacci

def main():
    """Main function that outputs the required greeting."""
    # Calculate fibonacci of 5
    fib_5 = fibonacci(5)
    
    # Output the required format
    print(f"Hello, {fib_5}!")

if __name__ == "__main__":
    main()