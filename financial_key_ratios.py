def calculate_ratios(total_revenue, variable_costs, fixed_costs, taxes, interest_expense):

  gross_profit = total_revenue - variable_costs
  operating_income = gross_profit - fixed_costs
  net_income = operating_income - taxes - interest_expense

  ratios = {
      "Gross Profit Margin (%)": (gross_profit / total_revenue) * 100,
      "Operating Profit Margin (%)": (operating_income / total_revenue) * 100,
      "Net Profit Margin (%)": (net_income / total_revenue) * 100,
      "Return on Equity (ROE) (%)": None  # Not calculated in this exercise
  }

  return ratios

def main():
  """
  Prompts the user for income statement data and displays calculated ratios.
  """
  print("Income Statement Analysis")

  try:
    total_revenue = float(input("Enter Total Revenue: "))
    variable_costs = float(input("Enter Variable Costs: "))
    fixed_costs = float(input("Enter Fixed Costs: "))
    taxes = float(input("Enter Taxes: "))
    interest_expense = float(input("Enter Interest Expense: "))

    if total_revenue <= 0 or variable_costs < 0 or fixed_costs < 0 or taxes < 0 or interest_expense < 0:
      raise ValueError("Input values cannot be negative.")

    ratios = calculate_ratios(total_revenue, variable_costs, fixed_costs, taxes, interest_expense)

    print("\nFinancial Ratios:")
    for ratio_name, ratio_value in ratios.items():
      if ratio_value is not None:
        print(f"{ratio_name}: {ratio_value:.2f}")
      else:
        print(f"{ratio_name}: Not available (requires Shareholders' Equity)")

  except ValueError as e:
    print("Error:", e)

if __name__ == "__main__":
  main()
