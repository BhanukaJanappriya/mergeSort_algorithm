def mergeSort(arr):
    if len(arr)>1:
        mid = len(arr)//2
        L=arr[:mid]
        R=arr[mid:]
        mergeSort(L)
        mergeSort(R)

        i=j=key=0
        
        #Copy data to temp arrays L[] and R[]
        while i<len(L) and j<len(R):
            if L[i] < R[j]:
                arr[key]=L[i]
                i+=1
            else:
                arr[key] = R[j]
                j+=1
            key+=1

        while i<len(L):
            arr[key] = L[i]
            i+=1
            key+=1
        
        while j<len(R):
            arr[key] = R[j]
            j+=1
            key+=1
    return arr
        
            
arr = [2,4,6,3,8,33,64,22,54] 
sorted_array = mergeSort(arr)
print("Sorted array-->",sorted_array)