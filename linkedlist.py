class linked:
    def __init__(self,*data):
        data = list(data)
        self.data = data.pop(0)
        self.leng = 1
        self.fwd = None
        self.rev = None
        if len(data) > 0:
           for i in data:
            self.insert(i)

    def __str__(self):
        temp = self
        st = str(temp.data)
        temp = temp.fwd
        while temp is not None:
            st += ','
            st += str(temp.data)
            temp = temp.fwd
        return st
        
    def insert(self, val, pos=None):
        if pos == 0:
            tem = linked(self.data)
            self.data = val
            tem.fwd = self.fwd
            tem.rev = self
            self.fwd.rev = tem
            self.fwd = tem
            self.leng += 1
        elif pos is None:
            temp = self
            while temp.fwd is not None:
                temp = temp.fwd
            temp.fwd = linked(val)
            temp.fwd.rev = temp
            self.leng += 1
        else:
            temp = self.atIndex(pos, True)
            te = linked(val)
            if temp is not None:
                te.fwd = temp
                te.rev = temp.rev
                te.rev.fwd = te
                temp.rev = te
                self.leng += 1

    def remove(self, pos=None):
        if pos == 0:
            temp = self.data
            self.data = self.fwd.data
            self.fwd.data = temp
            self.fwd.fwd.rev = self
            self.fwd = self.fwd.fwd
            self.leng -= 1
        elif pos is None:
            temp = self
            while temp.fwd is not None:
                temp = temp.fwd
            temp.rev.fwd = None
            self.leng -= 1
        else:
            temp = self.atIndex(pos, True)
            if temp is not None:
                temp.fwd.rev = temp.rev
                temp.rev.fwd = temp.fwd
                self.leng -= 1
            

    def find(self, val, retpoi=None):
        temp = self
        pos = 0
        while temp is not None:
            if temp.data == val:
                return temp if retpoi else pos
            pos += 1
            temp = temp.fwd
        else:
            return None if retpoi else -1

    def atIndex(self, pos, retpoi=None):
        temp = self
        for i in range(pos):
            if temp is None:
                return None
            temp = temp.fwd
        return temp if retpoi else temp.data

    def length(self):
        return self.leng

    def prin(self):
        temp = self
        while temp is not None:
            if temp.fwd is not None:
                print("fwd",temp.fwd.data,end=" ")
            print(temp.data)
            if temp.rev is not None:
                print("rev",temp.rev.data)
            temp = temp.fwd
            
            
        

a = linked(1,2,3,4,6,7,8,9)    #add any no. of values to initialize the list
a.insert(10)                   #insert with one arg, inserts at last
print(a)
print(a.length())
a.insert(5,4)                  #insert with two args, first arg value, second arg position
print(a)
print(a.length())
a.remove()                     #removes the last element
print(a)
print(a.length())
a.remove(3)                    #removes the element of the specified index
print(a)
print(a.length())
print(a.find(7))
print(a.atIndex(2))
