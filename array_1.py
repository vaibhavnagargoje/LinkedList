# exrecise 1 ********************************************************************************
# # array datastructure

# # january - 2200
# # february= 2350
# # march= 2600
# # april= 3000
# # may = 10000
# # june = 2000



# expense= [2200,2350,2600,3000,10000,2000]

# #  1) in feb how many rupes you spent extra compare to january
# print("in febuary this much extra was spent compared to jan:", expense[1]-expense[0])


# # 2)find the out your total expensein first quarter (firest three month) of the year
# print("expence of 1st quarter:",expense[0]+expense[1]+expense[2])

# # 3)find out of if you spnt exactly 2000 rupes in any month
# for i in expense:
#     if (i==2000):
#         print(i)
# print("did you spent 2000 in any mounth ",2000 in expense)

# # June month just finished and your expense is 1980 dollar. Add this item to our monnthly expense list
# expense.append(1980)
# print("expences of the end of july ",expense)


# # you returned an item that you bought in a month of  april and 
# #  got a refund of 200$ .Make a correction to your monthly expense list
# # based of this 

# expense[3]=expense[3]-200
# print("Expense after 200$ return in April: ",expense)


# exercise 2 ************************************************

# heros=['spider man','thor','hulk','iron man','caption america']

# 1)length of the list
# print(heros.__len__())
# print(len(heros))

# 2) add  black panther at the end of this list
# a= 'black panther'
# heros.append('black panther')
# print(heros)

# 3) you relize  that you need to add 'black panther' after 'hulk'
#so remove it from the list first and then add  it after 'hulk'

# heros.remove('black panther')
# print(heros)

# heros.insert(3,'black panther')
# print(heros)

# 4)  Now  you don't like thor and hulk bexause they get angry easily :)
# so you want to remove thor and hulk from list and replace then whit doctor strange ( because he is cool).
# do that with one line code 
# print(heros[1:3])
# heros [1:3]= ['doctor strange']
# print( heros)




#  5) sort the list in alphabetical order 

# heros.sort()
# print(heros)

# print(heros.sort())




# create a list of all numbers between 1 and a max number.Max number is somthing you need to take from a user using unput function 
# count=0
# odd = []
# a= int(input("Enter the number "))
# for num in range(a):
#     if (num%2==0):
#         pass
#     else:
#         odd.append(num)
#         count+=1
# print(odd,"total number :",count)






# def ArraySort(arr):
#     if len(arr)==1:
#         return True
#     return arr[0]<=arr[1] and ArraySort(arr[1:])

# arr=[2,7,9,10,20]
# print(ArraySort(arr))












