# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
age_as_int = int(age)
days = (90 * 365) - (age_as_int * 365)
weeks = (90 * 52) - (age_as_int * 52)
months = (90 * 12) - (age_as_int * 12)

live = f"You have {days} days, {weeks} weeks, and {months} months left."
print(live)