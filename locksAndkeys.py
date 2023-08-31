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

while 1:
  play1Position = random.randint(0, len(allLocks) - 1)
  play2Position = random.randint(0, len(allLocks) - 1)
  if play1Position != play2Position:
    break

measure = []
for i in range(len(allLocks)):
  measure.append(" "+str(i)+"  ")

youwin = False
playerPosition=play1Position
while not youwin:
  if playerPosition==play1Position:
    playerPosition=play2Position
  elif playerPosition==play2Position:
    playerPosition=play1Position
  else:
    print("WTF")


  print(measure , ": Indexes")
  print(allLocks, ": Locks")
  print(allKeys , ": Keys ")
  
  print("You are locked at position", playerPosition, "escape.")
  quits=0
  while 1:
    inpLockIndex = input("Trade your key with another key. Choose by Entering its index: \n")
    if inpLockIndex=="quit":
      quits=1
    elif inpLockIndex.isdigit():
      inpLockIndex = int(inpLockIndex)
      if -1<inpLockIndex<len(allLocks):
        break
      else:
        print(inpLockIndex, "is not a valid index.")
    else:
      print(inpLockIndex, "is not an index.")
  if quits:
    break
  
  if allLocks[inpLockIndex][0][1] == allKeys[playerPosition][0][1]:
    if playerPosition == inpLockIndex:
      if playerPosition==play1Position:
        print("\n                     !!!!! Player1 Wins !!!!!")
        break
      elif playerPosition==play2Position:
        print("\n                     !!!!! Player2 Wins !!!!!")
        break
    else:
      gainedKey  = allKeys[inpLockIndex]
      allKeys[inpLockIndex] = allKeys[playerPosition]
      allKeys[playerPosition] = gainedKey
  else:
    print("\n                     !!!!!You don't have correct Key!!!!!\n", allLocks[inpLockIndex][0], allKeys[playerPosition][0])

