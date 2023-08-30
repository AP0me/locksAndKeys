#this game works
import random

allKeys = []
for i in range(10):
  rKeyNum = random.randint(1, 9)
  allKeys.append(["K" + str(rKeyNum)])

allLocks = []
for i in range(len(allKeys)):
  allLocks.append(list(allKeys[i]))
random.shuffle(allLocks)

for i in range(len(allLocks)):
  allLocks[i][0] = allLocks[i][0].replace("K", "L")
myPosition = random.randint(0, len(allLocks) - 1)

measure = []
for i in range(len(allLocks)):
  measure.append(" "+str(i)+"  ")

youwin = False
while not youwin:
  print(measure)
  print(allLocks)
  print(allKeys)
  
  print("You are behind lock", allLocks[myPosition][0], "at position", myPosition, "open your lock.")
  inpLockIndex = int(input("Choose a lock index to open: "))

  hasCorrectKey = False
  for i in range(len(allKeys[myPosition])):
    if allLocks[inpLockIndex][0][1] == allKeys[myPosition][i][1]:
      if myPosition == inpLockIndex:
        youwin = True
      allLocks[inpLockIndex] = ["  "]
      gainedKey  = allKeys[inpLockIndex]
      allKeys[inpLockIndex] = ["  "]
      allKeys[myPosition] = allKeys[myPosition] + gainedKey
      allLocks[myPosition].append("  ")
      measure[myPosition] = measure[myPosition]+"      "

      hasCorrectKey = True
  if hasCorrectKey == False:
    print("\n                     !!!!!You don't have correct Key!!!!!\n", allLocks[inpLockIndex][0], allKeys[myPosition][i])

print("You Win")

