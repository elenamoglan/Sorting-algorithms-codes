def mergesort ( x ) :
  if len ( x ) < 2: # Return if arr was reduced to size 1
    return x
  result = []
  mid = int ( len ( x ) / 2)
  y = mergesort ( x [: mid ]) # 1 st half of array
  z = mergesort ( x [ mid :]) # 2 nd half of array
  i , j = 0 , 0
  while i < len ( y ) and j < len ( z ) :
    if y [ i ] > z [ j ]:
      result . append ( z [ j ])
      j += 1
    else :
      result.append ( y [ i ])
      i += 1
  result += y [ i :] # Add left over elements
  result += z [ j :] # Add left over elements
  return result

A = [64, 25, 12, 22, 11]

print('Sorted Array in Ascending Order:')
print(mergesort(A))