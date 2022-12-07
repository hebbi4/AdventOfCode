import string
import time

start = time.time()

#importing file and cleaing it up
text_file = 'input'
skra = open(text_file, 'r').readlines()
clean = []

for line in skra:
  clean.append(line.replace("\n", ""))

#part 1
sumINeed = 0
currentDirL = []
currentDirS = ''
dirSize = {}
allFiles = 0 #added for part 2

for line in clean:
  line = line.split()
  
  if line[0] == '$':
    if line[1] == 'cd':
      if line[2] == '..':
        currentDirL.pop()
      else:  
        currentDirL.append(line[2])
        currentDirS = ''
        #This is done to create a uniqe key in the dictionary
        #since there are duplicate directory names
        for i in range(len(currentDirL)):
          currentDirS += currentDirL[i] + '/'
        if currentDirS not in dirSize.keys():
          dirSize[currentDirS] = 0
  elif line[0] != 'dir':
    allFiles += int(line[0]) #added for part 2
    currentDirS = ''
    #making sure to add the size to all parent directories
    for i in range(len(currentDirL)):
      currentDirS += currentDirL[i] + '/'
      dirSize[currentDirS] += int(line[0])

for i in dirSize:
  if dirSize[i] < 100000:
    sumINeed += dirSize[i]

#answer is 1367870
print(sumINeed)

#part 2
totalSpace = 70000000
neededFreeSpace = 30000000
currentFreeSpace = totalSpace - allFiles
needToDelete = neededFreeSpace - currentFreeSpace
sizeToDelete = 40528671

for i in dirSize:
  if dirSize[i] > needToDelete and dirSize[i] < sizeToDelete:
    sizeToDelete = dirSize[i]

print(needToDelete)
print(sizeToDelete)

end = time.time()
print(end-start)