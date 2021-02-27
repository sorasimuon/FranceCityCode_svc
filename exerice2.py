import math
from typing import List

l = [1,2,3,4,5]
    
def permutations(l: List[int]) -> List[List[int]]:
    pass




class Modifiers:

    def __init__(self, name):
        self.__protected_member = name  # Protected Attribute

m = Modifiers("SKAUL05")
print(m.__protected_member)
m.__protected_member = "Github" # Changing Protected Attribute values
print(m.__protected_member)