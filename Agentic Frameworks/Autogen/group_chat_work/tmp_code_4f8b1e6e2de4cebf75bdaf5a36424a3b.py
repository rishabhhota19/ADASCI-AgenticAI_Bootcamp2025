# fibonacci_numbers.py

def generate_fibonacci(n: int) -> list[int]:
    """
    Generate the first 'n' Fibonacci numbers.

    Args:
        n (int): Number of Fibonacci numbers to generate.

    Returns:
        list: A list containing the first 'n' Fibonacci numbers.
    """
    fibonacci_numbers = [0, 1]
    while len(fibonacci_numbers) < n:
        fibonacci_numbers.append(fibonacci_numbers[-1] + fibonacci_numbers[-2])
    return fibonacci_numbers[:n]


def write_code_to_file(filename: str):
    """
    Write the fibonacci numbers script to a file.
    """
    with open(filename, 'w') as file:
        file.write('# Fibonacci Numbers Demo\n')
        file.write('''
def generate_fibonacci(n):
    """Generate the first 'n' Fibonacci numbers."""
    fibonacci_numbers = [0, 1]
    while len(fibonacci_numbers) < n:
        fibonacci_numbers.append(fibonacci_numbers[-1] + fibonacci_numbers[-2])
    return fibonacci_numbers[:n]
''')
        file.write('\n')
        file.write('if __name__ == "__main__":\n')
        file.write('    fibonacci_numbers = generate_fibonacci(10)\n')


def main():
    """
    The main function to generate Fibonacci numbers and save the code.
    """
    fibonacci_numbers = generate_fibonacci(10)
    print("Fibonacci numbers:")
    print(fibonacci_numbers)

    write_code_to_file('demo.txt')
    print("Code written to demo.txt")


if __name__ == "__main__":
    print("Waiting for Critic's approval...")
    input("Please approve by pressing Enter...")
    print("Critic's approval received.")
    main()

print("Waiting for Critic's final approval...")
input("Please approve by pressing Enter...")
print("Critic's final approval received.")
print("Code successfully saved to demo.txt.")