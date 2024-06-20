def selection_sort ( arr ) :
  for i in range (0 , len ( arr ) - 1) :
    minIndex = i
    for j in range ( i +1 , len ( arr ) ) :
      if arr [ j ] < arr [ minIndex ]:
        minIndex = j
    arr [ i ] , arr [ minIndex ] = arr [ minIndex ] , arr [ i ]

A = [64, 25, 12, 22, 11]
selection_sort(A)
print('Sorted Array in Ascending Order:')
print(A)