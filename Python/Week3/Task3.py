#Program  calculates BMI and gives also a textual description.
#BMI = mass(kg)/height(m)/height(m)

mass = float(input("Give a weight (kg): "))
height = float(input("Give a height (m): "))

BMI = mass / height / height

if BMI < 15:
    cat = "(Very severely underweight)"
elif BMI >= 15 and BMI < 16:
    cat = "(Severely underweight)"
elif BMI >= 16 and BMI < 18.5:
    cat = "(Underweight)"
elif BMI >= 18.5 and BMI < 25:
    cat = "(Normal healthy weight)"
elif BMI >= 25 and BMI < 30:
    cat = "(Overweight)"
elif BMI >= 30 and BMI < 35:
    cat = "(Moderately obese)"
elif BMI >= 35 and BMI < 40:
    cat = "(Severely obese)"
else:
    cat = "(Very severely obese)"

print ("BMI is: {:.1f}".format(BMI),(cat))
