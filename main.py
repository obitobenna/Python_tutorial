from lst_and_dictionary import mul_arr

def main():
    arr =[2 ,4, 7 ,5 , 8]
    print(mul_arr(arr ,3))

    arr =[3 , 5 , 9, 10 ,5]
    print(mul_arr(arr , 7))

    arr =[16 ,7 ,9 ,5 , 7]
    print(mul_arr(arr, 4))

    try:
        arr = ["5" , "8" , "9"]
        print (mul_arr(arr , 3))
    except Exception as e:
        print (e) 



    try:
        arr =""
        print(mul_arr(arr , 2))
    except Exception as e:
        print(e)    

main()        
