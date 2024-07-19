def calculate_discount(total_amount, day_of_week):
    discount = 0
    
    if day_of_week.lower() == 'monday' and total_amount > 20:
        discount = 0.10
    elif day_of_week.lower() == 'friday' and total_amount > 10:
        discount = 0.05
    
    final_amount = total_amount * (1 - discount)
    return final_amount

def main():
    print("Welcome to the Coffee Shop!")
    
    try:
        total_amount = float(input("Enter the total amount of your order: $"))
        day_of_week = input("Enter the day of the week: ")
        
        final_amount = calculate_discount(total_amount, day_of_week)
        
        print(f"The final amount after applying the discount (if any) is: ${final_amount:.2f}")
    
    except ValueError:
        print("Invalid input. Please enter numeric values for the total amount.")

if __name__ == "__main__":
    main()
