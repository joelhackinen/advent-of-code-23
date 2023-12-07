DIGITS = {
	"one": 1,
	"two": 2,
	"three": 3,
	"four": 4,
	"five": 5,
	"six": 6,
	"seven": 7,
	"eight": 8,
	"nine": 9
}

# expects each line to contain at least one digit
def find_digit(line: str, reverse=False):
	line = line if not reverse else reversed(line)
	read_chars = ""
	for char in line:
		if char.isdigit():
			return char
		read_chars = read_chars + char if not reverse else char + read_chars
		for key in DIGITS.keys():
			if key in read_chars:
				return str(DIGITS[key])
	return "hallelujah"


def main():
	calibrations_sum = 0

	with open("input.txt", "r") as file:
		for line in file:
			digits = ""
			digits += find_digit(line)
			digits += find_digit(line, reverse=True)
			print(digits)
			calibrations_sum += int(digits[0] + digits[-1])
	
	print(calibrations_sum)

if __name__ == "__main__":
	main()