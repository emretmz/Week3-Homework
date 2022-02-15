from numpy import str_


str_of_user=list(input("Enter a info with hypen(-): ").split('-'))
def alpha_order(str_of_user):
    sorted_list=sorted(str_of_user)
    return print(sorted_list)
alpha_order(str_of_user)    

