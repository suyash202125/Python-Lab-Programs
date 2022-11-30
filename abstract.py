from abc import ABC, abstractmethod

# Abstract sort class in which the construct takes
#array as input to initialize it.
class AbstractSort(ABC):
    def __init__(self, arr):
        self.arr = arr
        super().__init__()

    @abstractmethod
    def sort(self):
        pass
    
    def display(self):
        print("The array output from abstract class:", self.arr)

#Bubble Sort class
class BubbleSort(AbstractSort):
    def sort(self):
        l = len(self.arr)
        for i in range(l-1):
            for j in range(0, l-i-1):
                if self.arr[j] > self.arr[j + 1]:
                    self.arr[j], self.arr[j + 1] = self.arr[j + 1], self.arr[j]

    def bubbleSort_display(self):
        print("The sorted array via Bubble sort:", self.arr)
        
#Selection Sort class
class SelectionSort(BubbleSort):
    def sort(self):
        l = len(self.arr)
        for i in range(l):
            min_val_index = i
            for j in range(i+1, l):
                if self.arr[min_val_index] > self.arr[j]:
                    min_val_index = j
                
            self.arr[i], self.arr[min_val_index] = self.arr[min_val_index], self.arr[i]

    def sel_sort_display(self):
        print("The sorted array via Selection Sort is:", self.arr)


#DRIVERCODE
a = [9, 8, 22, 6, 5, 11, 3, 7]

#creating an object of Selecttion sort and passing
#the array "a" as argument
s = SelectionSort(a)
#calling abstract class display function from the object
#of Selection sort class
s.display()

s.sort()
#calling display function of BubbleSort class
s.bubbleSort_display()
#calling display function of SelectionSort class
s.sel_sort_display()