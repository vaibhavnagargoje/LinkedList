import ctypes

class MeraList:
    def __init__(self):
        self.size=1
        self.n=0
        # We have to create a C type array with size = self.size 
        self.A=self.__make_array(self.size)
    
    def __make_array(self, capacity):
        # this code creates a C type array (static array (refrential array )) with size capacity 
        return (capacity*ctypes.py_object)()
    
    #  len function 
    def __len__(self):
        return self.n
    
    #append function 
    def append(self,item):
        if self.n==self.size:
            #resize
            self.__resize(self.size*2)
        self.A[self.n]=item
        self.n+=1
    def __resize(self,new_capacity):
        #create a new array with new capactity
        B=self.__make_array(new_capacity)
        self.size=new_capacity

        #copy the content of A to  B
        for i in range(self.n):
            B[i]=self.A[i]
        # reassing A
        self.A=B
    def __str__(self):
        result = ''
        for i in range(self.n):
            result=result+str(self.A[i])+" , "
        return '['+ result[ :-2] +']'
    
    #indexing
    def __getitem__(self,index):
        if (0<= index<self.n):
            return self.A[index]
        else:
            return "IndexError"
    def pop(self):
        if self.n ==0:
            return "Empty List"
        print(self.A[self.n-1])
        self.n-=1
    def clear(self):
        self.n=0
        self.size=1
    def find(self, item):
        for i in range(self.n):
            if self.A[i]==item:
                return i
        return "Value Error , item not found...."

    def insert(self,position, item):
        if self.n==self.size:
            self.__resize(self.size*2)
        for i in range(self.n,position,-1):
            self.A[i]=self.A[i-1]
        self.A[position]=item
        self.n+=1
    
    #deleting element for array
    def __delitem__(self,pos):
        if  0<=pos <self.n:
            for i in range(pos,self.n-1):
                self.A[i]=self.A[i+1]
            self.n-=1   

    def remove(self, item):
        pos = self.find(item)
        if type(pos)==int:
            self.__delitem__(pos)
        else:
            return pos


L = MeraList()
L.append("hello")
L.append(4.5)
L.append(True)
L.append(100)

# print(len(L))
# print(type(L))
# print(L)
# print(L[4])

# L.pop()
# L.pop()
# L.pop()
# L.pop()
# L.pop()
# print(L)

# print(L)
# L.clear()
# print(L )



# print(L)
# print(L.find(4.5))


# print(L)
# L.insert(3,"world"
# print(L)

# print(L)
# del(L[54])
# print(L)



print(L)
L.remove(4.5)
print(L)
