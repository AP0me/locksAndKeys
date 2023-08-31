#this game works
import random

def checkInput(inpLockIndex, quits):
  if inpLockIndex=="quit":
    quits=1
    return [quits, None]
  elif inpLockIndex.isdigit():
    inpLockIndex = int(inpLockIndex)
    if -1<inpLockIndex<len(allLocks):
      if allLocks[inpLockIndex][0][1] == allKeys[playerPosition][0][1]:
        return [quits, inpLockIndex, "breaks"]
      else:
        print("Key", allKeys[playerPosition][0], "doesn't fit", allLocks[inpLockIndex][0])
        return [quits, inpLockIndex, None]
    else:
      print(inpLockIndex, "is not a valid index.")
      return [quits, None, None]
  else:
    print(inpLockIndex, "is not an index.")
    return [quits, None, None]

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

youwin=0
quits=0
playerPosition=play2Position
while not youwin and not quits:
  if playerPosition==play1Position:
    playerPosition=play2Position
    input("Press Enter to: Switch to player2")
  elif playerPosition==play2Position:
    playerPosition=play1Position
    input("Press Enter to: Switch to player1")
  else:
    print("WTF")
  print("\n"*20)
  

  print(measure , ": Indexes")
  print(allLocks, ": Locks")
  print(allKeys , ": Keys ")
  
  print("You are locked behind position", playerPosition, "Escape.")
  goodInput=0
  while not goodInput:
    inpLockIndex = input("Trade your key with another key. Choose by Entering its index or 'quit' to quit the game: \n")
    [quits, inpLockIndex, breaks] = checkInput(inpLockIndex, quits)
    if breaks!=None:
      goodInput=1
    else:
      if playerPosition==play1Position:
        playerPosition=play2Position
      elif playerPosition==play2Position:
        playerPosition=play1Position
      else:
        print("WTF")
      break

    if quits:
      break
    if allLocks[inpLockIndex][0][1] == allKeys[playerPosition][0][1]:
      if playerPosition == inpLockIndex:
        if playerPosition==play1Position:
          print("\n                     !!!!! Player1 Wins !!!!!")
          youwin=1
        elif playerPosition==play2Position:
          print("\n                     !!!!! Player2 Wins !!!!!")
          youwin=1
      else:
        gainedKey  = allKeys[inpLockIndex]
        allKeys[inpLockIndex] = allKeys[playerPosition]
        allKeys[playerPosition] = gainedKey
        print(measure , ": Indexes")
        print(allLocks, ": Locks")
        print(allKeys , ": Keys ")
      break

  if quits:
    break
