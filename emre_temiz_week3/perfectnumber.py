def isperfectnum(num):
    sum=0    
    for i in range(1,num):
        if num %i==0:
            sum=sum+i
    if sum==num:
        return "perfect"    
def add_perfect():
    i=0
    perfect_list=[]
    for i in range(1,100): #check perfect numbers until 100
        if isperfectnum(i)=="perfect":
            perfect_list.append(i)
    return print(perfect_list)
add_perfect()
           