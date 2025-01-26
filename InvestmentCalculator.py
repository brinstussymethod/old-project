class InvestmentCalculator:
    def calculate_future_value(self, principal_amount, annual_interest_rate, years):
        if annual_interest_rate < 0:
            raise ValueError("Interest rate cannot be negative.")
        
        future_value = principal_amount * (1 + annual_interest_rate) ** years
        print(f"The future value of your investment is: ${future_value:.2f}")

def get_valid_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input! Please enter a numeric value.")

calculator = InvestmentCalculator()

while True:
    try:
        principal_amount = get_valid_input("Enter the principal amount: ")
        annual_interest_rate = get_valid_input("Enter the annual interest rate (as a decimal): ")
        years = get_valid_input("Enter the number of years: ")

        calculator.calculate_future_value(principal_amount, annual_interest_rate, years)
        break
    except ValueError as e:
        print(e)
    except Exception:
        print("An unexpected error occurred. Please try again.")