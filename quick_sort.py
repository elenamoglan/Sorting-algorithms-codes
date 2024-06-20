def Partition ( arr , low , high ) :
  i = ( low -1) # index of smaller element
  pivot = arr [ high ]
  for j in range(low, high):
    if arr [ j ] <= pivot :
      i = i +1
      arr [ i ] , arr [ j ] = arr [ j ] , arr [ i ]
  arr [ i +1] , arr [ high ] = arr [ high ] , arr [ i +1]
  return ( i +1)
def QuickSort ( arr , low , high ) : # The main function
  if low < high :
    pi = Partition ( arr , low , high ) # partitioning index
    QuickSort ( arr , low , pi -1) # Separately sort elements
    QuickSort ( arr , pi +1 , high )
    
data = [1, 7, 4, 1, 10, 9, -2] 
size = len(data)
 
QuickSort(data, 0, size - 1)
 
print('Sorted Array in Ascending Order:')
print(data)