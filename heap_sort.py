def Heapify ( arr , n , i ) :
  largest = i # Initialize largest as root
  l = 2 * i + 1 # left = 2* i + 1
  r = 2 * i + 2 # right = 2* i + 2
  if l < n and arr [ i ] < arr [ l ]:
    largest = l
  if r < n and arr [ largest ] < arr [ r ]:
    largest = r # Change root , if needed
  if largest != i :
    arr [ i ] , arr [ largest ] = arr [ largest ] , arr [ i ] # swap
    Heapify ( arr , n , largest ) # Heapify the root .

def HeapSort ( arr , n ) : # The main function
  for i in range (n , -1 , -1) : # Build a maxheap .
    Heapify ( arr , n , i ) # One by one extract elements
  for i in range (n -1 , 0 , -1) :
    arr [ i ] , arr [0] = arr [0] , arr [ i ] # swap
    Heapify ( arr , i , 0)
    
arr = [12, 11, 13, 5, 6, 7, 20]
n = len(arr)
HeapSort(arr,n)

print('Sorted array is')
print(arr)