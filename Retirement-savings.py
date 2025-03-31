import random

# Constants
initial_salary = 65000
contribution_rate = 0.09
salary_increase_rate = 0.02
interest_rate = 0.105
total_years = 34


# Function to calculate future value of retirement savings
def calculate_retirement_savings():
    total_future_value = 0

    for n in range(1, total_years + 1):
        # Calculate the salary for year n
        salary_n = initial_salary * (1 + salary_increase_rate) ** (n - 1)
        # Calculate the contribution for year n
        contribution_n = salary_n * contribution_rate
        # Calculate the future value of that contribution
        future_value_n = contribution_n * (1 + interest_rate) ** (total_years - n)
        total_future_value += future_value_n

    return total_future_value


# Run the analysis 1000 times
results = [calculate_retirement_savings() for _ in range(1000)]

# Check the results
average_value = sum(results) / len(results)
min_value = min(results)
max_value = max(results)

print(f"Average Future Value: ${average_value:,.2f}")
print(f"Minimum Future Value: ${min_value:,.2f}")
print(f"Maximum Future Value: ${max_value:,.2f}")
