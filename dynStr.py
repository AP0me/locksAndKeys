
#rules should change state (done)
#state should change rules (TODO)
#research "Fuzzy Cognitive Maps" (TODO)

def applyRule(rules, causeIndex):
  return rules[causeIndex][1]

def timePasses(rules, eventList):
  resEventList = [0]*len(eventList)
  for eventIndex in range(len(eventList)):
    cause = eventList[eventIndex]
    if cause:
      causeIndex = eventIndex
      resIndexes = applyRule(rules, causeIndex)
      for i in range(len(resIndexes)):
        resEventList[resIndexes[i]]=1
  return resEventList

def gameLoop(eventList):
  while 1:
    eventList = timePasses(rules, eventList)
    for index in range(len(eventList)):
      event = eventList[index]
      if event:
        print(meaning[index])
    input()

rules={
  0:[0, [5]], 1:[1, [0]], 2:[2, [6]], 3:[3, [1]], 4:[4, [3]], 5:[5, [7]], 6:[6, [4]], 7:[7, [8]], 8:[8, [2]],
}
meaning={
  0:"believe", 1:"guardian", 2:"wealth", 3:"culture", 4:"invention", 5:"ally", 6:"discovery", 7:"domination", 8:"peace"
}
eventList = [1,0,1,0,0,0,1,0,0,]
gameLoop(eventList)

