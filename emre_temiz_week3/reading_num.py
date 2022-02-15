import inflect
int_num=int(input("Enter a number:"))
def num_to_word(int_num):
    nums_reader=inflect.engine()
    return print(nums_reader.number_to_words(int_num))
num_to_word(int_num)    