

## count sort with O(N^2) time complexity

def CountSort1(arr):
    # Create a count array to store the frequency of each element in arr.
    m = max(arr) + 1
    count_array = [0] * (m+1)
    print(count_array)
    for i in range(len(arr)):
        count_array[arr[i]] +=1
    print(count_array)
    
    #update count array
    for i in range(1,len(count_array)):
        count_array[i]=count_array[i]+count_array[i-1]
    print(count_array)

    
    arr2=arr.copy()
    print(arr2)
    for i in range(len(arr)-1,-1,-1):
        # print(i)
        count_array[arr[i]]-=1
        arr2[count_array[arr[i]]]=arr[i]

    print(arr2)















def CountSort2(arr):
    
    count=[]
    max_ele=arr[0]
    for i in range(len(arr)):
        if(arr[i]>max_ele):
            max_ele=arr[i]
    
    for i in range(max_ele+2):
        count.append(0)
    
    print(count)

    for i in range(len(count)):
        count[arr[i]]+=1
    print(count)


    arr2=[]
    for i in range(len(arr)):
        j=i
        while(count[j]>0):
            arr2.append(i)
            count[j]-=1
        
    print(arr2)
    





arr=[3,5,2,3,4,2,34,23,2,4,1,5]
CountSort1(arr)