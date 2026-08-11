# from datetime import datetime,date
# today=date.today()
# name=input("Enter Your name:")

# letter= "Dear",name, "You are Selected!", today

# print(letter)

from datetime import date

# The given letter template
letter = '''Dear <|NAME|>,
You are selected!
<|DATE|>'''

# Get inputs from the user
name = input("Enter the name: ")

# Get today's date dynamically and format it (e.g., 2026-08-11)
today_date = str(date.today())

# Replace the placeholders with the dynamic values
filled_letter = letter.replace("<|NAME|>", name)
filled_letter = filled_letter.replace("<|DATE|>", today_date)

# Print the final letter
print("\n--- Generated Letter ---")
print(filled_letter)
