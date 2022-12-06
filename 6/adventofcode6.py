import string

text_file = 'input'
skra = open(text_file, 'r').readlines()
clean = []

for line in skra:
  clean.append(line.replace("\n", ""))

print(skra)
print(clean)

checking = []
cnt = 0
flag = False

for i in clean[0]:
  checking.append(i)
  if len(checking) > 14:
    checking.pop(0)
  else:
    flag=False
  for x in range(len(checking)-1):
    for y in range((x+1),len(checking)):
      if checking[x] == checking[y]:
        flag = False
  cnt += 1
  if flag:
    print(cnt)
    break
  flag = True