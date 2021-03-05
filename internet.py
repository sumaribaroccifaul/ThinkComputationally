#!/usr/bin/env python3

# install packages #
from datetime import datetime

# user instructions #
start = datetime.now()
print("Please look up the value of Pi on the internet.")
print()

# user input #
val = input("Enter your value: ")
end = datetime.now()

# print input value #
print("value:", val)
print("duration:", end-start)

with open("internet.yaml", "w") as f:
    f.write(f"value: \"{val}\"\n")
    f.write(f"duration: {end-start}\n")
