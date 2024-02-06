"""
looking at lists and dictionaries
working with them and also examples
"""

def mul_arr(arr=[], idx=0):
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    for i in range(len(arr)):
        if not isinstance(arr[i], int):
            raise TypeError("Element must be an integer")
        arr[i] *= idx
    return arr       


laptop ={
    "brand" :"HP",
    "ram" :"50gb",
    "rom" : "500gb",
}
print( "The brand name is {}, the ram{}. And the rom is {}".format(laptop["brand"], laptop["ram"], laptop["rom"]) ,end="")

#list comprehension
square_list ={x ** 2 for x in range (1,11)}
print(square_list)

even_list = [y for y in square_list if  y % 2 == 0]
print(even_list)



