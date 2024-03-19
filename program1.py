def fibonacci_sequence(n):
    sequence = [0, 1] #Fibonacci sequence starts with o and 1

    if n == 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return sequence
    
    while len(sequence) < n:
        next_term = sequence[-1] + sequence[-2]
        sequence.append(next_term)

    return sequence

def main():
    n=int(input("Enter the number of terms for the Fibonacci sequence: "))

    fibonacci = fibonacci_sequence(n)

    print("Fibonacci sequence up to term", n, "is:", fibonacci)

if __name__ == "__main__":
    main()