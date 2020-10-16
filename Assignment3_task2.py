# -*- coding: utf-8 -*-
import random
from random import randint
from sys import maxsize
from time import time

"""
Sorter implements several algorithms to sort a list.
my_tuple: A tuple of integers to be sorted.
algorithm: The algorithm to be used for sorting. Valid names are 'merge', 'insertion', 'bubble', and 'default'.
tuple_order: The order of the integers in the generated tuple to be sorted. Valid orders are: 'random', 'ascending', descending' Default: random.
Each sorting method make a list copy of `my_tuple` and maintains the original order.
"""

class Sorter():

    def __init__(self):
        """
        Sorter constructor.
        By default, the `algorithm` is set as 'default' to use the built-in sort()
        By default, the sorting will be done on a tuple with random order of elements.
        """
        self.my_tuple = tuple([])
        self.algorithm = 'default'
        self.tuple_order='random'

    def generate_new_tuple(self, n, tuple_order):
        if tuple_order=='random':
            self.generate_random_tuple(n)
        elif tuple_order=='ascending':
            self.generate_ascending_tuple(n)
        elif tuple_order=='descending':
            self.generate_descending_tuple(n)

    ########## Task 2 starts here. ###########

    def generate_random_tuple(self, n):
        """
        Generate n-length tuple of random integers.
        `n` is an integer indicates the length of the list.
        Random integers are in a range from 0 to 9223372036854775807 (sys.maxsize)
        The method generate_random_tuple() first generates a new list of `n` length
        containing random integers, converts the newly generated list to a tuple,
        and assigns the tuple to `self.my_tuple`. Nothing needs to be returned.
        """

        # transforming tuple into empty list to run for loop
        self.my_tuple = list([])
        # for loop for defining a random number n times and appending result to empty list
        for i in range(n):
            i = [random.randint(0, 9223372036854775807)]
            self.my_tuple.append(i)
        # transforming list into tupple again
        self.my_tuple = tuple(self.my_tuple)
        pass

    def generate_ascending_tuple(self, n):
        """
        Generate n-length tuple of random integers in ascending order.
        `n` is an integer indicates the length of the list.
        Random integers are in a range from 0 to 9223372036854775807 (sys.maxsize)
        The method generate_ascending_tuple() first generates a new list of `n` length
        containing random integers (like in the previous method). You can reuse the code of the generate_random_tuple
        method here. Now sort this list in ascending order, here you are allowed to use the built-in sort() function
        on the list. Convert the list to a tuple and assign the tuple to `self.my_tuple`. Nothing needs to be returned.
        """
        self.my_tuple = list([])
        for i in range(n):
            i = [random.randint(0, 9223372036854775807)]
            self.my_tuple.append(i)
        # using sort method for ascending order (reverse=False)
        self.my_tuple.sort(reverse=False)
        self.my_tuple = tuple(self.my_tuple)
        pass

    def generate_descending_tuple(self, n):
        """
        Generate n-length tuple of random integers in descending order.
        `n` is an integer indicates the length of the list.
        Random integers are in a range from 0 to 9223372036854775807 (sys.maxsize)
        The method generate_descending_tuple() first generates a new list of `n` length
        containing random integers (like in the previous method). You can reuse the code of the generate_random_tuple
        method here. Now sort this list in descending order, here you are allowed to use the built-in sort() and
        reverse() functions on the list. Convert the list to a tuple and assign the tuple to `self.my_tuple`. Nothing needs to be returned.
        """
        self.my_tuple = list([])
        for i in range(n):
            i = [random.randint(0, 9223372036854775807)]
            self.my_tuple.append(i)
        # using sort method for descending order (reverse=True)
        self.my_tuple.sort(reverse=True)
        self.my_tuple = tuple(self.my_tuple)
        pass

    ########## Task 2 ends here. ###########

    def set_algorithm(self, algo):
        # Set the attribute to select which algorithm to be used for sort().
        # Check if the given algorithm is valid
        if algo not in ['default', 'merge', 'insertion', 'bubble']:
            raise AlgorithmNotImplementedError
        self.algorithm = algo


    def time_trials(self, n):
        """
        Time sorting `self.my_tuple` with a specific algorithm for n times.
        `n` is an integer value. The sorting will be performed `n` times.
        The method time_trials() returns a float value for how long it took in seconds.

        """
        start_time = time() # current time
        for i in range(n):
            if self.algorithm == 'merge':
                self._merge_sort()
            elif self.algorithm == 'insertion':
                self._insertion_sort()
            elif self.algorithm == 'bubble':
                self._bubble_sort()
            else:
                self._default_sort()

        return time() - start_time # time elapsed


    def _bubble_sort(self):
        """
        Sort `self.my_tuple` with Bubble Sort algorithm.
        https://www.geeksforgeeks.org/bubble-sort/
        The bubble_sort() method returns the sorted list while it keeps `self.my_tuple` unsorted. The returned value MUST be List data type.
        """
        a = list(self.my_tuple)
        n = len(a)

        # Traverse through all list elements
        for i in range(n):
            # Last i elements are already in place
            for j in range(0, n-i-1):
                # traverse the list from 0 to n-i-1
                # Swap if the element found is smaller
                # than the next element
                if a[j] > a[j+1]:
                    a[j], a[j+1] = a[j+1], a[j]
        return a


    def _default_sort(self):
        """
        Sort `self.my_tuple` with the Python built-in list sorting function.
        https://docs.python.org/3/library/stdtypes.html#list.sort
        The default_sort() method returns the sorted list while it keeps `self.my_tuple` unsorted. The returned value MUST be List data type.
        """
        # Make a list copy of self.my_tuple
        a = list(self.my_tuple)
        # sort the list by the built-in list.sort()
        # 
        a.sort()
        return a

    def _insertion_sort(self):
        
        """
        Sort `self.my_tuple` with Insertion Sort algorithm.
        Implementation of Insertion Sort algorithm taken from:
        https://introcs.cs.princeton.edu/python/42sort/insertion.py.html

        The insertion_sort() method returns the sorted list while it keeps `self.my_tuple` unsorted. The returned value MUST be List data type.

        """
        a = list(self.my_tuple)
        n = len(a)
        for i in range(1, n):
            j = i
            while (j > 0) and (a[j] < a[j - 1]):
                self._exchange(a, j - 1, j)
                j -= 1
        return a

    def _exchange(self,a,i,j):
        # Exchange a[i] and a[j] for Insertion Sort.
        a[i], a[j] = a[j], a[i]

    def _merge_sort(self):
        """
        Sort `self.my_tuple` with Merge Sort algorithm.
        Implementation of Merge Sort algorithm taken from:
        https://introcs.cs.princeton.edu/python/42sort/merge.py.html
        
        The merge_sort() method returns the sorted list while it keeps `self.my_tuple` unsorted. The returned value MUST be List data type.

        """
        a = list(self.my_tuple)
        n = len(a)
        aux = [0.0] * n
        self._sort(a, 0, n, aux)
    
    def _sort(self,a, lo, hi, aux):
        # Sort a[lo:hi] into increasing order, using array aux as auxiliary memory.
        n = hi - lo
        if n <= 1:
            return
        mid = (lo + hi) // 2
        self._sort(a, lo, mid, aux)
        self._sort(a, mid, hi, aux)
        self._merge(a, lo, mid, hi, aux)
    
    def _merge(self,a, lo, mid, hi, aux):
        # Merge a[lo:mid] with a[mid:hi] using aux as auxiliary memory.
        n = hi - lo
        i = lo
        j = mid
        for k in range(n):
            if i == mid:
                aux[k] = a[j]
                j += 1
            elif j == hi:
                aux[k] = a[i]
                i += 1
            elif a[j] < a[i]:
                aux[k] = a[j]
                j += 1
            else:
                aux[k] = a[i]
                i += 1
        a[lo:hi] = aux[0:n]


class AlgorithmNotImplementedError(Exception):
    """Raised when an unknown algorithm was selected"""
    pass
