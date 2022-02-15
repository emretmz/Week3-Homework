my_ununique_list=list(input("Enter not unique list of number with space: ").split())
def convert_to_unique(my_ununique_list):
    my_ununique_list=set(my_ununique_list)
    return print(my_ununique_list)
convert_to_unique(my_ununique_list)   