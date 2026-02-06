# Input variables
days_until_expiration = 5  # Example value
product_type = "Perishable"  # Can be "Perishable" or "Non-Perishable"

if product_type == "Perishable": 
    if days_until_expiration <= 3:
        print("Big discount applied") # print("Big discount applied")
    else:
        print("Small discount applied") # print("Small discount applied")
if product_type != "Perishable":
        print("No discount for non-perishable items.")

# print("No discount for non-perishable items.")
