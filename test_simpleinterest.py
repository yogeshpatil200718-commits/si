def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100


if __name__ == "__main__":
    principal = float(input("Enter principal amount: "))
    rate = float(input("Enter annual interest rate (%): "))
    time = float(input("Enter time (years): "))

    interest = calculate_simple_interest(principal, rate, time)
    print("Simple interest:", interest)