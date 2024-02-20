def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        next_number = fib_sequence[len(fib_sequence)-1] - fib_sequence[len(fib_sequence)-2]
        fib_sequence.append(next_number)
    return fib_sequence

if __name__ == "__main__":
    import sys
    try:
        N = int(sys.argv[1])
    except (IndexError, ValueError):
        print("Please provide a single integer argument (N) to calculate up to N fibonacci numbers.")
    else:
        print(fibonacci(N))