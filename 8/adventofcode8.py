import string


#importing file and cleaing it up
text_file = 'input'
skra = open(text_file, 'r').readlines()
clean = []

for line in skra:
    line = line.replace("\n", "")
    clean.append(line)

col = len(clean[0])
row = len(clean)

tracker = []
for i in range(row):
    column = []
    for j in range(col):
        column.append(0)
    tracker.append(column)

for i in range(col):
    tracker[i][0] = 1
    tracker[0][i] = 1
    tracker[i][-1] = 1
    tracker[-1][i] = 1


#part 1
maxnr= 0

for i in range(1, row -1):
    maxnr = clean[i][0]
    for j in range(1, col -1):
        if clean[i][j] > maxnr:
            maxnr = clean[i][j]
            tracker[i][j] = 1

for i in range(1, row-1):
    maxnr = clean[i][-1]
    for j in range(1, col -1):
        if clean[i][col-j] > maxnr:
            maxnr = clean[i][col-j]
            tracker[i][col-j] = 1

for i in range(1, col-1):
    maxnr = clean[0][i]
    for j in range(1, row -1):
        if clean[j][i] > maxnr:
            maxnr = clean[j][i]
            tracker[j][i] = 1

for i in range(1, col-1):
    maxnr = clean[-1][i]
    for j in range(1, row -1):
        if clean[row - j][i] > maxnr:
            maxnr = clean[row-j][i]
            tracker[row-j][i] = 1


cnt = 0
for i in range(row):
    for j in range(col):
        if tracker[i][j] == 1:
            cnt += 1

print('There are:', cnt, 'visible trees.')


#part 2

nvis = 0
svis = 0
evis = 0
wvis = 0

visability = []
for i in range(row):
    column = []
    for j in range(col):
        column.append(0)
    visability.append(column)

for i in range(1, row-1):
    for j in range(1, col-1):
        #print('i:',i,'j:',j)
        for k in reversed(clean[i][:j]):
            if k < clean[i][j]:
                wvis += 1
            else:
                wvis += 1
                break

        for k in clean[i][j+1:]:
            if k < clean[i][j]:
                evis += 1
            else:
                evis += 1
                break

        column = []
        for x in range(col):
            column.append(clean[x][j])
        
        for k in reversed(column[:i]):
            if k < clean[i][j]:
                nvis += 1
            else:
                nvis += 1
                break
        
        for k in column[i+1:]:
            if k < clean[i][j]:
                svis += 1
            else:
                svis += 1
                break

        visability[i][j] = evis * wvis * nvis * svis
        evis = 0
        wvis = 0
        nvis = 0
        svis = 0

for i in range(col):
    visability[i][0] = 0
    visability[0][i] = 0
    visability[i][-1] = 0
    visability[-1][i] = 0

maxVisScore = 0
maxVisCord = (0,0)
for i in range(row):
    for j in range(col):
        if visability[i][j] > maxVisScore:
            maxVisScore = visability[i][j]
            maxVisCord = (i,j)

print('maxVisScore is:', maxVisScore, 'and it is located at:', maxVisCord)