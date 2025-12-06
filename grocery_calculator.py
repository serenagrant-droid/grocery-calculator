def main():
    # Prompt for coupon
    coupon = float(input("Enter coupon amount as a decimal (example .10): "))

    # Validate coupon range
    if coupon > 1 or coupon <= 0:
        print("Invalid coupon amount. Setting coupon to 10%.")
        coupon = 0.10

    # Grocery bills
    w1 = float(input("Enter Week 1 grocery bill: "))
    w2 = float(input("Enter Week 2 grocery bill: "))
    w3 = float(input("Enter Week 3 grocery bill: "))
    w4 = float(input("Enter Week 4 grocery bill: "))

    # Calculations
    monthly_total = w1 + w2 + w3 + w4
    weekly_average = monthly_total / 4

    discounted_monthly = monthly_total - (monthly_total * coupon)
    discounted_weekly = discounted_monthly / 4

    # Display results
    print("\n----- RESULTS -----")
    print(f"Monthly total (no coupon): ${monthly_total:.2f}")
    print(f"Weekly average (no coupon): ${weekly_average:.2f}")

    print(f"Monthly total (with coupon): ${discounted_monthly:.2f}")
    print(f"Weekly average (with coupon): ${discounted_weekly:.2f}")


# Run the program
main()
