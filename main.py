unsorted = [5, 6, 0, 8, 2, 3, 9, 1, 7, 4]

def insertionSort(array):
  answer = []
  for x in range(0, len(array)):
    inserted = False
    for y in range(0, len(answer)):
      if(inserted == False):
        if(array[x] < answer[y]):
          inserted = True
          copy = answer
          answer = []
          for z in range(0, y):
            answer.append(copy[z])
          answer.append(array[x])
          for z in range (y, len(copy)):
            answer.append(copy[z])
    if(inserted == False):
      answer.append(array[x])
    print(answer)
  for x in range(0, len(answer)):
    print(answer[x])

insertionSort(unsorted)

