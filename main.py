import sys  # importa sys

def calculate_average(numbers):
    return sum(numbers) / len(numbers)

def main():
    print("call main")

if __name__ == "__main__":
    print(len(sys.argv))
    main()
