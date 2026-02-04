from fibonacci import fibonacci

def main():
    """
    Main function that generates fibonacci sequence and formats output string.
    """
    # Get fibonacci sequence for 9 numbers
    fib_result = fibonacci(9)
    
    # Format the output string as specified in requirements
    output = f"Hello, {fib_result}!"
    print(output)

if __name__ == "__main__":
    main()