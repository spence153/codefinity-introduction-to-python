def calculate_total_cost(price, quantity): # Call the function and print the result
    total_cost = price * quantity
    return total_cost
    
apples_total_cost = calculate_total_cost(1.50, 10)

print(f"The total cost for apples is ${apples_total_cost}")