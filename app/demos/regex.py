import re


input_text = "Call me at 123-456-7890, make sure to get the ticket 987-654-3210."

# Look for any phone numbers, 3 digits - 3 digits - 4 digits
phone_pattern = r"\b\d{3}-\d{3}-\d{4}\b"

scrubbed_output = re.sub(phone_pattern, "<PHONE>", input_text)

print(f"Original: {input_text}")
print(f"Regex Output: {scrubbed_output}")
