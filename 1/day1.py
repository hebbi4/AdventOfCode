import string

text_file = 'calories'
skra = open(text_file, 'r').readlines()



current_largest = 1
largest_cal = 0
second_cal = 0
third_cal = 0
current_cal = 0
cnt = 1


for line in skra:
  if line == "\n":
    if current_cal >= largest_cal:
      third_cal = second_cal
      second_cal = largest_cal
      largest_cal = current_cal
      current_largest = cnt
      cnt+= 1
      current_cal = 0
    elif current_cal >= second_cal:
      third_cal = second_cal
      second_cal = current_cal
      cnt += 1
      current_cal = 0
    elif current_cal >= third_cal:
      third_cal = current_cal
      cnt += 1
      current_cal = 0
    else:
      cnt += 1
      current_cal = 0
  else:
    current_cal = int(line) + current_cal

print(largest_cal + second_cal + third_cal)
print(largest_cal)
print(second_cal)
print(third_cal)

print(194812)