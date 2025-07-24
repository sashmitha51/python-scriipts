# Even or Odd Checker (Jenkins compatible)

import sys

if len(sys.argv) != 2:
    print("Usage: python script.py <number>")
    sys.exit(1)

try:
    number = int(sys.argv[1])
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")
except ValueError:
    print("Please provide a valid integer.")
    sys.exit(1)

