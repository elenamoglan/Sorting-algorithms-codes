def BubbleSort ( arr , n ) :
  for i in range ( n ) : # Traverse through all elements
    for j in range (0 , n -i -1) : # Traverse n -i -1
      if arr [ j ] > arr [ j +1]: # Swap if the element found is greater than the next element
        arr [ j ] , arr [ j +1] = arr [ j +1] , arr [ j ]
        
data = [-2, 45, 0, 11, -9]

BubbleSort(data, len(data))

print('Sorted Array in Ascending Order:')
print(data)