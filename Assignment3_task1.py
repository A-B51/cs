import time
import sys


def binary_search(key, a):
    """
    Implementation of Binary Search taken from https://introcs.cs.princeton.edu/python/42sort/binarysearch.py.html
    The binary search method (do not modify!)
    
    return: the index of key in array a, or -1 if key is not present.
    """
    return _search(key, a, 0, len(a))

def _search(key, a, lo, hi):
    """
    The binary search (inner) method (do not modify!)
    return: the index of key in array a[lo:hi], or -1 if key is not present.
    """
    if hi <= lo:
        return -1
    mid = (lo + hi) // 2

    if key < a[mid]:
        return _search(key, a, lo, mid)
    elif a[mid] < key:
        return _search(key, a, mid+1, hi)
    else:
        return mid


def read_files(file_allmail,file_blacklist):

    """
    This method should read in a file from the file system containing a list of all email addresses (allmail),
    and a second file from the file system containing a list of all blacklisted email addresses (blacklist).
    The filenames should be put as arguments on the Terminal when starting the script (file with all emails as
    first argument, file with the blacklist addresses as second argument), e.g., you should run
     "python blacklist_filter.py all_email_large.txt blacklist_large.txt" to execute the program.
    Note: When reading in the files line by line you should also remove the newline character "\n" from each entry before
    storing the email addresses in a Python list, use for example the "splitlines()" method for that.
    Return the two Python lists.

    param file_allmail: file name of the file with all email addresses
    param file_blacklist: file name of the file with the blacklisted email addresses
    return allmail: a Python list containing all email addresses
    return blacklist: a Python list containing all blacklisted email addresses
    """
    allmail = []
    blacklist = []

    # opening and reading files
    with open(str(file_allmail), 'r') as f:
        f_emails = f.read().splitlines()    

    with open(str(file_blacklist), 'r') as b:
        b_emails = b.read().splitlines()

    # adding all emails to allmail list
    for email in f_emails:
        allmail += [email]

    # adding blacklisted emails to blacklist list
    for email in b_emails:
        blacklist += [email] 

    return allmail,blacklist

#test = read_files("all_email_small.txt", "blacklist_small.txt")
#print(test)
# print(test.sort())
#print(test[0].sort())

def deduplicate_and_sort(allmail, blacklist):
    """
    This method should remove all the duplicates from the list of all email addresses and the blacklist.
    Here we also sort the entries of the allmail list in ascending order as a prerequisite to run the binary search
    algorithm. We will also do this for the blacklist. You can use the "sort()" method for both lists here.
    
    param allmail: list with all email addresses
    param blacklist: listh with the blacklisted email addresses
    return allmail: List with all email addresses -- duplicates removed, and sorted
    return blacklist: List with all blacklisted email addresses -- duplicates removed, and sorted
    """
    # Remove duplicates
    for email in allmail:
        # defining t as a number that indicates how many times an element appears in the list
        t = allmail.count(email)
        # if elements aper more than once
        if t > 1:
            # safe elements index in delete var
            delete = allmail.index(email)
            # delete element using pop() method
            allmail.pop(delete)

    for email in blacklist:
        t = blacklist.count(email)
        if t > 1:
            delete = blacklist.index(email)
            blacklist.pop(delete)

    # Sort both lists for Binary Search
    allmail.sort()
    blacklist.sort()

    return allmail,blacklist

def filter_binary(allmail,blacklist):
    """
    This method should use the binary search algorithm to find all blacklisted email addresses in the list of all addresses.
    Loop through all blacklisted addresses and use the binary search (see binary_search(key,a)) method to determine if the
    address is contained in the allmail list or not. If so, append this address to a list of invalid email addresses, which
    will be returned at the end (invalid_mail).
    We also want to measure the time it takes to find all the blacklistd email addresses using binary search. The method
    time.time() can be used to approximate the duration. Use this function to generate a timestamp before starting to
    iterate through all blacklisted addresses, and to generate a second timestamp after all iterations are finished.
    The difference between both timestamps gives you an approximate idea of the execution duration.
    Return the list of invalid email addresses and the duration.

    param allmail: List with all email addresses (duplicates removed, and sorted)
    param blacklist: List with all blacklisted email addresses (duplicates removed, and sorted)
    return invalid_mail: List of all invalid (blacklisted) email address from the list of all email addresses
    return duration: Duration of the binary filter
    """
    t_start = time.time()
    invalid_mail=[]

    for email in blacklist:
        # if email in blacklist was found in allemail, binary search returns a positive number
        if _search(email, allmail, 0, len(allmail)) >= 0:
            # if so, we append that to the invalid email lists
            invalid_mail.append(email)
    

    t_end = time.time()
    duration = t_end-t_start

    return invalid_mail,duration

def filter_linear(allmail,blacklist):
    """
    This method should use the linear search algorithm to find all blacklisted email addresses in the list of all
    addresses. Loop through all blacklisted addresses and check if the address is also contained in the allmail list
    (using the in function for lists). If so, append this address to a list of invalid email addresses, which will be 
    returned at the end (invalid_mail).
    We also want to measure the time it takes to find all the blacklistd email addresses using linear search. The method
    time.time() can be used to approximate the duration. Use this function to generate a timestamp before starting to
    iterate through all blacklisted addresses, and to generate a second timestamp after all iterations are finished.
    The difference between both timestamps gives you an approximate idea of the execution duration. Note: if the duration
    is printed as 0.0 then the fraction of the actual execution time is too small to be displayed (e.g., 0.005)
    Return the list of invalid email addresses and the duration.

    param allmail: List with all email addresses (duplicates removed, and sorted)
    param blacklist: List with all blacklisted email addresses (duplicates removed, and sorted)
    return invalid_mail: List of all invalid (blacklisted) email address from the list of all email addresses
    return duration: Duration of the linear filter

    """

    t_start = time.time()
    invalid_mail = []

    # Code pretty self explaining
    for email in blacklist:
        if email in allmail:
            invalid_mail.append(email)
    
    t_end = time.time()
    duration = t_end - t_start
    return invalid_mail,duration

    
def main():
    """
    The main method to be executed (do not change!).
    """

    # Read in both files from the file system in the read_files() method. The names of the files are provided as arguments
    # when running the script.
    filename1 = sys.argv[1] # the file with a list of all email addresses
    filename2 = sys.argv[2] # the file with a list of the blacklisted email addresses
    allmail,blacklist = read_files(filename1,filename2)

    # Remove duplicates and sort both lists in the deduplicate_and_sort() method.
    allmail,blacklist = deduplicate_and_sort(allmail,blacklist)

    # Find all blacklisted mail addresses in list of all addresses using Binary Search
    addresses1,duration1 = filter_binary(allmail,blacklist)

    # Here we print the number of blacklisted email addresses found in the list of all addresses using Binary search and
    # the time it took the execute the search for all addresses.
    print('Number of blacklisted mail addresses with binary search: {}, duration: {}'.format(len(addresses1),duration1))

    # Find all blacklisted mail addresses in list of all addresses using Linear Search
    addresses2,duration2 = filter_linear(allmail,blacklist)

    # Here we print the number of blacklisted email addresses found in the list of all addresses using Linear search and
    # the time it took the execute the search for all addresses.
    print('Number of blacklisted mail addresses with linear search: {}, duration: {}'.format(len(addresses2),duration2))

if __name__ == '__main__': main()
