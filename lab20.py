#!/usr/bin/env python3

import random

wordbank = ["indentation", "spaces"]

tlgstudents= ['Albert', 'Anthony', 'Brenden', 'Craig', 'Deja', 'Elihu', 'Eric', 'Giovanni', 'James', 'Joshua', 'Maria', 'Mohamed', 'PJ', 'Philip', 'Sagan', 'Suchit', 'Meka', 'Trey', 'Winton', 'Xiuxiang', 'Yaping']

#random.shuffle(tlgstudents)

wordbank.append(4)

num = int(input(f"Please enter a number between 1 and {len(tlgstudents)}: "))

student_name = tlgstudents[num-1]

print(f"{student_name} always uses", wordbank[2], wordbank[1], "to indent.")

