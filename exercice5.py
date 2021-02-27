# arr = [4, 3, 2, 4, 1, 3, 2]


# def uniqueNumber(arr):
    
#     d = {}

#     for num in arr:
#         d[num] = d.get(num, 0) + 1
    
#     for k, v in d.items():
#         if v == 1:
#             return k


# print(uniqueNumber(arr))




class A:
    def who_am_i(self):
        print("I am a A")

class B(A):
    def who_am_i(self):
        print("I am a B")

class C(A):
    def who_am_i(self):
        print("I am a C")

class D(B,C):
    def who_am_i(self):
        print("I am a D")

d1 = D()
d1.mro()