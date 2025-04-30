def mergeSort(arr):
    n = len(arr)
    if n>1:
        mid1 = n//3
        mid2 = 2*n//3
        
        Left = arr[:mid1]
        Mid = arr[mid1:mid2]
        Right = arr[mid2:]

        mergeSort(Left)
        mergeSort(Mid)
        mergeSort(Right)

        i=j=k=key=0
        
        while i<len(Left) and j<len(Mid):
            if Left[i] < Mid[j]:
                arr[key]=Left[i]
                i+=1
            else:
                arr[key] = Mid[j]
                j+=1                
            key+=1

        while i<len(Left):
            arr[key] = Left[i]
            i+=1
            key+=1
        
        while j<len(Mid):
            arr[key] = Mid[j]
            j+=1
            key+=1
            
        # Now merge the result with Right
        i=k=0
        temp = arr[:key]
        key=0
        
        while i < len(temp) and k < len(Right):
            if temp[i] < Right[k]:
                arr[key] = temp[i]
                i+=1
            else:
                arr[key] = Right[k]
                k+=1
            key+=1
            
        while i < len(temp):
            arr[key] = temp[i]
            i+=1
            key+=1
            
        while k<len(Right):
            arr[key] = Right[k]
            k+=1
            key+=1
        
    return arr
        
            
Even_Length_arr = [4, 3, 6, 1, 2, 5] 
sorted_Even_array = mergeSort(Even_Length_arr)
print("Sorted Even length array-->",sorted_Even_array)

Odd_Length_arr = [7, 9, 3, 5, 1] 
sorted_Odd_array = mergeSort(Odd_Length_arr)
print("Sorted Odd length array-->",sorted_Odd_array)

With_duplicates_arr = [2, 3, 2, 1, 1, 4] 
sorted_duplicate_value_array = mergeSort(With_duplicates_arr)
print("Sorted Odd length array-->",sorted_duplicate_value_array)

empty_array = []
arr = mergeSort(empty_array)
print('Sorted array-->',arr)