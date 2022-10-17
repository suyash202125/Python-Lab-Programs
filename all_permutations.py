#Program to find all permutations of a string.

def put_in_string(List) :
    return ''.join(List)

#printing permutations
def all_permutations(mystr, start_index, end_index) :
    if start_index == end_index :
        print(put_in_string(mystr))
    else :
        for i in range(start_index, end_index) :
            mystr[start_index], mystr[i] = mystr[i], mystr[start_index]
            all_permutations(mystr, start_index + 1, end_index)
            mystr[start_index], mystr[i] = mystr[i], mystr[start_index] #backtrack

#input taking and passing to print all permutations
x = input("Enter the string: ")
l = len(x)
mystr = list(x)
all_permutations(mystr, 0, l)