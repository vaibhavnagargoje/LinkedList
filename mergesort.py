# def merge(Arr,low,mid,high):
    

#     i=low
#     j=mid+1
#     k=low
#     Brr=Arr.copy()

#     while (i<=mid and j<=high):
#         if(Arr[i]<Arr[j]):
#             Brr[k]=Arr[i]
#             k+=1
#             i+=1
#         else:
#             Brr[k]=Arr[j]
#             k+=1
#             j+=1
#     while(i<=mid):
#         Brr[k]=Arr[i]
#         k+=1
#         i+=1
#     while(j<=high):
#         Brr[k]=Arr[j]
#         k+=1
#         j+=1
    
#     # Arr=Brr
#     # print(Arr)
#     # print(Brr)


# def mergeSort(Arr,low,high):
#     if low<high:
#         mid=(low+(high-low))/2
#         print(mid)
#         mergeSort(Arr,low,mid)
#         mergeSort(Arr,mid+1,high)
#         merge(Arr,low,mid,high)





# Arr=[4,3,6,3,6,7,4,78,9,2,10]
# lenght=len(Arr)-1
# mergeSort(Arr,0,lenght)
# print(Arr)



# i=18
# while(i<=23):
#     if(i%2==0):
#         print(i)
#     i+=1


list1=[3,5,2,6]
num = int(input("enter number"))
for i in list1:
    if i==num:
        print("number found")
        break
else:
    print("not found")



# 2nd way
list1=[3,5,2,6]
if num in list1:
    print("number found")
else:
    print("not found")