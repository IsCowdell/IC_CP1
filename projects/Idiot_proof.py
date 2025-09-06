#IC - 1st Idiot proof



name_input = input("Enter your full name (first and last): ")
phone_input = input("Enter your phone number (10 digits, no spaces): ")
gpa_input = input("Enter your GPA: ")


formatted_name = ' '.join([word.capitalize() for word in name_input.strip().split()])


formatted_phone = f"{phone_input[0:3]} {phone_input[3:6]} {phone_input[6:10]}"


formatted_gpa = round(float(gpa_input), 1)


print("\nFormatted Output:")
print(f"name: {formatted_name}")
print(f"phone: {formatted_phone}")
print(f"GPA: {formatted_gpa}")
