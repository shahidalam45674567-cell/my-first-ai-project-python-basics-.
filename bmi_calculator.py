# Project 2: Smart BMI & Fitness Calculator

print("--- AI Fitness Assistant ---")

# User se input lena (Weight kgs me aur Height feet me)
weight = float(input("Aapka weight (KG me) dalein: "))
height_feet = float(input("Aapka height (Feet me) dalein: "))

# Feet ko meters me convert karna (1 foot = 0.3048 meters)
height_meters = height_feet * 0.3048

# BMI Formula: weight / (height * height)
bmi = weight / (height_meters ** 2)

print(f"\nAapka calculated BMI hai: {bmi:.2f}")

# Result check karna
if bmi < 18.5:
    print("Status: Underweight (Aapko acchi diet aur muscle gain ki zaroorat hai!)")
elif 18.5 <= bmi < 24.9:
    print("Status: Normal/Fit (Bahut badhiya! Aap bilkul fit hain.)")
elif 25 <= bmi < 29.9:
    print("Status: Overweight (Thoda cardio aur workout badhane ki zaroorat hai!)")
else:
    print("Status: Obese (Aapko fitness aur diet par dhyan dena chahiye.)")
  
