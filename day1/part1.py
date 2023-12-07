calibrations_sum = 0

with open("input.txt", "r") as file:
	# expects each line to contain at least one digit
	for line in file:
		digits = list(filter(str.isdigit, line))
		calibrations_sum += int(digits[0] + digits[-1])

print(calibrations_sum)