# Program to find all the unique palindromes of a string.

# function to find unique palindromes
def find_unique_palindromes(mystr) :

    # a set doesn't allow to store duplicate values
    unique_palindromes = set()

    for index in range(len(mystr)) :

        # adding all the unique palindromes of odd length with mystr[index] as midpoint
        add_palindromes(mystr, index, index, unique_palindromes)

        # adding all the unique palindromes of even length with mystr[index] and mystr[index + 1] as midpoints
        add_palindromes(mystr, index, index + 1, unique_palindromes)

    # printing the unique palindromes
    print(unique_palindromes, end = '')


# function for adding palindromes to the unique_palindromes set
def add_palindromes(mystr, low_ptr, high_ptr, unique_palindromes) :

    # loop through the string
    while low_ptr >= 0 and high_ptr < len(mystr) and mystr[low_ptr] == mystr[high_ptr] :

        # adding palindromes to the set
        unique_palindromes.add(mystr[low_ptr : high_ptr + 1])

        # decreasing low_ptr index
        low_ptr = low_ptr - 1
        # increasing high_ptr index
        high_ptr = high_ptr + 1

# input string
mystr = input("Enter the string for finding its unique palindromes: ")
find_unique_palindromes(mystr)