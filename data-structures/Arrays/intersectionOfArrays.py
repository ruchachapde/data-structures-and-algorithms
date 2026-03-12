#Intersection of arrays means the common elements that appear in both arrays.

def intersectionOfArr(arr1, arr2):
  set_arr1 = set(arr1)
  set_arr2 = set(arr2)

  if set_arr1<set_arr2:
    return[x for x in set_arr1 if x in set_arr2]
  
  else:
    return[x for x in set_arr2 if x in set_arr1]
    
#Driver Code
arr1 = [1, 2, 3,4, 5, 5, 7, 6]
arr2 = [2, 3,4,4]
result = []
result = intersectionOfArr(arr1, arr2)

for i in range(len(result)):
  print(result[i], end =' ')

