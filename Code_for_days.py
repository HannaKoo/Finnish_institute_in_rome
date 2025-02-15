weekdays = [
    "Sunnuntaina",
    "Maanantaina",
    "Tiistaina",
    "Keskiviikkona",
    "Torstaina",
    "Perjantaina",
    "Lauantaina"
]

# Start date for numbering (16th of February)
current_day = 16
month = "helmikuuta"

numbered_weekdays = []

# Loop until the 28th of February
while current_day <= 28:
    for day in weekdays:
        if current_day > 28:
            break
        numbered_weekdays.append(f"### {current_day}. {month} {day}")
        current_day += 1

# Print the modified list
for day in numbered_weekdays:
    print(day)
