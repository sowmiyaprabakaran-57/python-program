def get_outfit_recommendation(temp, condition):
    if temp < 0:
        return "Wear a heavy coat, gloves, and a hat. It's freezing!"
    elif 0 <= temp < 10:
        return "Wear a warm coat and a scarf. It's chilly!"
    elif 10 <= temp < 20:
        return "Wear a jacket or sweater. It's cool."
    elif 20 <= temp < 30:
        return "Wear a t-shirt and light pants. It's warm."
    else:
        return "Wear light clothing. It's hot!"

def main():
    print("Welcome to the Weather Outfit Recommendation System!")
    
    while True:
        try:
            temp = float(input("Please enter the temperature (in Celsius): "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    condition = input("Please enter the weather condition (sunny, rainy, cloudy, etc.): ").lower()

    outfit = get_outfit_recommendation(temp, condition)
    
    print(f"Based on the temperature of {temp}°C and the condition '{condition}', you should: {outfit}")

if __name__ == "__main__":
    main()
