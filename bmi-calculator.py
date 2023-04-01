# Let’s make finding out your BMI quicker and easier,
# by creating a program that takes a person's weight and height as 
# input and outputs the corresponding BMI category.
# BMI + Weight/Height²

MIN_WEIGHT = 20
MAX_WEIGHT = 300
MIN_HEIGHT = 1
MAX_HEIGHT = 3

while True:
    try:
        weight = float(input("Enter Weight (in kg): "))
        if weight < MIN_WEIGHT or weight > MAX_WEIGHT:
            raise ValueError(f"Weight must be between {MIN_WEIGHT} and {MAX_WEIGHT} kg")
        break
    except ValueError as e:
        print(e)

while True:
    try:
        height = float(input("Enter Height (in meters): "))
        if height < MIN_HEIGHT or height > MAX_HEIGHT:
            raise ValueError(f"Height must be between {MIN_HEIGHT} and {MAX_HEIGHT} meters")
        break
    except ValueError as e:
        print(e)

bmi = weight / height ** 2

if bmi < 18.5 :
    print("Your BMI is", int(bmi))
    print("Underweight")
elif bmi == 18.5 or bmi < 25:
    print("Your BMI is", int(bmi))
    print("Normal")
elif bmi == 25 or bmi < 30:
    print("Your BMI is", int(bmi))
    print("Overweight")
else:
    print("Your BMI is", int(bmi))
    print("Obesity")