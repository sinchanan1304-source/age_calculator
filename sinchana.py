quantity = int(input("Enter the quantity purchase:"))

cost = quantity * 100

if cost > 2000:
    discount = 0.15 * cost
elif cost > 1000:
    discount = 0.10 * cost
else :
    discount = 0

    total_cost = cost - discount

    print("Initial cost :", cost)
    print("Discount applied :", discount)
    print("Total cost after discount:", total_cost)