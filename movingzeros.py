'''
Write an algorithm that takes an array and moves all of the zeros to
the end, preserving the order of the other elements.
move_zeros([false,1,0,1,2,0,1,3,"a"]) # returns[false,1,1,2,1,3,"a",0,0]
'''


def move_zeros(array):
    list_1 = [] # Check all values 
    list_2 = []

    for i in array:
        if (type(i) == int or type(i) == float) and int(i) ==0:
            list_1.append(i)
            
        else:
            list_2.append(i)
    return list_2 + list_1
        


        


