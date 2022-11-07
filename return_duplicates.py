# Write a function to find Duplicate values in the List

#Duplicate class
class Duplicate:
    '''Using in-built count function to find duplicated values and store it in a set'''
    def duplicates1(self, arr):
        '''set() doesn't hold same values more than once'''
        dup = set()

        for item in arr:
            if arr.count(item) > 1:
                dup.add(item)
        #returning list of duplicates
        return list(dup)

    '''In duplicate2(), we have first sorted the arr and then
    traversed the sorted array arr to find duplicated values'''
    def duplicates2(self, arr):
        dup = []
        a = sorted(arr)
        for i in range(0, len(arr)-1):
            if a[i] == a[i+1] and a[i] not in dup:
                dup.append(a[i])
        return dup

    '''In duplicates3(), we have used nested for loops to find the
    the duplicated values'''
    def duplicates3(self,arr):
        dup = []
        for i in range(0, len(arr) - 1):
            for j in range(0, len(arr) - 1):
                if arr[i] == arr[j] and i != j and arr[i] not in dup:
                    dup.append(arr[i])

        return dup

#DRIVER CODE
arr = [11, 5, 5, 23, 18, 18, 9, 9, 9, 0, 0, 4, 4, 4]
d = Duplicate()#object of Duplicate class
print("The list of duplicates from duplicate1:", d.duplicates1(arr))
print("The list of duplicates from duplicate2:", d.duplicates2(arr))
print("The list of duplicates from duplicate3:", d.duplicates3(arr))