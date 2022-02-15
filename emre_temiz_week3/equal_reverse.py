str_equal_rev=list(input("Enter words with space: ").split())
def is_equal_reversed(str_equal_rev):
    result=[]
    reversed_list=[]
    for x in str_equal_rev:
        x=x[::-1]
        reversed_list.append(x)
    i=0
    while i<len(reversed_list): 
        if str_equal_rev[i]==reversed_list[i]:           
            result.append("True")
        else: result.append("False")
        i+=1 
    return print(result)      
is_equal_reversed(str_equal_rev)


