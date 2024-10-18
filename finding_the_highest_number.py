#find_the_highest_number

#define_the_variables
def find_highest (num_1, num_2, num_3, num_4, num_5):

#compare_the_variables
    if num_1 > num_2 and num_3:
        if num_1 > num_4 and num_5:
            return num_1
    
    if num_2 > num_1 and num_3:
        if num_2 > num_4 and num_5:
            return num_2
    
    if num_3 > num_1 and num_2:
        if num_3 > num_4 and num_5:
            return num_3
    
    if num_4 > num_1 and num_2:
        if num_4 > num_3 and num_5:
            return num_4
    
    if num_5 > num_1 and num_2:
        if num_5 > num_3 and num_4:
            return num_5

#the_user_will_input
num_1 = int(input("enter your first number: "))   
num_2 = int(input("enter your second number: "))      
num_3 = int(input("enter your third number: "))      
num_4 = int(input("enter your fourth number: "))      
num_5 = int(input("enter your last number: "))  