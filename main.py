from fibonacci import fibonacci

def main():
    """
    Main function that generates fibonacci sequence and formats output.
    """
    # Get fibonacci sequence for position 9
    fib_list = fibonacci(9)
    
    # Convert list to comma-separated string
    fib_string = ", ".join(map(str, fib_list))
    
    # Create the required output format
    output = f"Hello, {fib_string}!"
    
    print(output)

if __name__ == "__main__":
    main()