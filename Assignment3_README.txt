(2a)  #### BUBBLE SORT ####

# random:

n:      64 time: 0.101877 (n:n/2) ratio: -
n:     128 time: 0.208665 (n:n/2) ratio: 2.048214
n:     256 time: 0.833200 (n:n/2) ratio: 3.992997
n:     512 time: 3.050795 (n:n/2) ratio: 3.661539
n:    1024 time: 12.073663 (n:n/2) ratio: 3.957547
n:    2048 time: 51.568568 (n:n/2) ratio: 4.271162


# ascending:

n:      64 time: 0.032944 (n:n/2) ratio: -
n:     128 time: 0.166553 (n:n/2) ratio: 5.055573
n:     256 time: 0.518438 (n:n/2) ratio: 3.112751
n:     512 time: 1.793873 (n:n/2) ratio: 3.460149
n:    1024 time: 7.491335 (n:n/2) ratio: 4.176067
n:    2048 time: 33.914535 (n:n/2) ratio: 4.527169


# descending:

n:      64 time: 0.069602 (n:n/2) ratio: -
n:     128 time: 0.241140 (n:n/2) ratio: 3.464545
n:     256 time: 1.431183 (n:n/2) ratio: 5.935067
n:     512 time: 4.196273 (n:n/2) ratio: 2.932032
n:    1024 time: 18.010809 (n:n/2) ratio: 4.292096
n:    2048 time: 76.013370 (n:n/2) ratio: 4.220431


-> Doubling factor: I would say on average 4 and bounded at aprx. 6.
-> Complexity: constant



2(b)  #### INSERTION SORT ####

# random:

n:      64 time: 0.058402 (n:n/2) ratio: -
n:     128 time: 0.176794 (n:n/2) ratio: 3.027168
n:     256 time: 0.640076 (n:n/2) ratio: 3.620473
n:     512 time: 2.770284 (n:n/2) ratio: 4.328052
n:    1024 time: 13.752953 (n:n/2) ratio: 4.964456
n:    2048 time: 55.230503 (n:n/2) ratio: 4.015901


# ascending

n:      64 time: 0.000994 (n:n/2) ratio: -
n:     128 time: 0.001997 (n:n/2) ratio: 2.008393
n:     256 time: 0.004020 (n:n/2) ratio: 2.013373
n:     512 time: 0.006947 (n:n/2) ratio: 1.728028
n:    1024 time: 0.015958 (n:n/2) ratio: 2.297035
n:    2048 time: 0.036868 (n:n/2) ratio: 2.310394
n:    4096 time: 0.132643 (n:n/2) ratio: 3.597735
n:    8192 time: 0.129653 (n:n/2) ratio: 0.977460
n:   16384 time: 0.278286 (n:n/2) ratio: 2.146399
n:   32768 time: 0.738061 (n:n/2) ratio: 2.652163
n:   65536 time: 2.591103 (n:n/2) ratio: 3.510690
n:  131072 time: 5.526251 (n:n/2) ratio: 2.132779


# descending

n:      64 time: 0.064826 (n:n/2) ratio: -
n:     128 time: 0.248368 (n:n/2) ratio: 3.831316
n:     256 time: 1.617676 (n:n/2) ratio: 6.513220
n:     512 time: 5.664858 (n:n/2) ratio: 3.501850
n:    1024 time: 24.839554 (n:n/2) ratio: 4.384851
n:    2048 time: 103.381489 (n:n/2) ratio: 4.161970


-> Doubling factor: It seems the doubling factor is steadly increasing, even though we do find some outliers that dont follow te pattern.
-> Complexity: I would say linear.


(2c)  #### MERGE SORT ####

# random

n:      64 time: 0.013962 (n:n/2) ratio: -
n:     128 time: 0.040890 (n:n/2) ratio: 2.928640
n:     256 time: 0.079786 (n:n/2) ratio: 1.951203
n:     512 time: 0.131646 (n:n/2) ratio: 1.650002
n:    1024 time: 0.306174 (n:n/2) ratio: 2.325729
n:    2048 time: 0.733154 (n:n/2) ratio: 2.394567
n:    4096 time: 2.214109 (n:n/2) ratio: 3.019979
n:    8192 time: 3.203399 (n:n/2) ratio: 1.446812
n:   16384 time: 9.996259 (n:n/2) ratio: 3.120516
n:   32768 time: 20.656743 (n:n/2) ratio: 2.066447


# ascending

n:      64 time: 0.011004 (n:n/2) ratio: -
n:     128 time: 0.025970 (n:n/2) ratio: 2.359983
n:     256 time: 0.056849 (n:n/2) ratio: 2.189029
n:     512 time: 0.132612 (n:n/2) ratio: 2.332725
n:    1024 time: 0.255315 (n:n/2) ratio: 1.925277
n:    2048 time: 1.090053 (n:n/2) ratio: 4.269445
n:    4096 time: 1.673555 (n:n/2) ratio: 1.535297
n:    8192 time: 3.689132 (n:n/2) ratio: 2.204369
n:   16384 time: 8.935065 (n:n/2) ratio: 2.421997
n:   32768 time: 18.947307 (n:n/2) ratio: 2.120556


# descending

n:      64 time: 0.017952 (n:n/2) ratio: -
n:     128 time: 0.034906 (n:n/2) ratio: 1.944354
n:     256 time: 0.055851 (n:n/2) ratio: 1.600051
n:     512 time: 0.152591 (n:n/2) ratio: 2.732102
n:    1024 time: 0.270310 (n:n/2) ratio: 1.771464
n:    2048 time: 1.214750 (n:n/2) ratio: 4.493915
n:    4096 time: 1.437150 (n:n/2) ratio: 1.183083
n:    8192 time: 3.514631 (n:n/2) ratio: 2.445556
n:   16384 time: 7.727335 (n:n/2) ratio: 2.198619
n:   32768 time: 17.661756 (n:n/2) ratio: 2.285621


-> doubling factor: for me it doesnt seem to follow a defined pattern, but it seems to be bounded at appr. 5.
-> complexity: constant



2(d)  ####  Why do you think my_tuple is defined as a tuple instead of a list? #### 

->  I guess there was a typo in the question, because the code defines it as a list, not a tuple. The reason for that is the method "sort()". It
    can only be used for lists (it is a list data type method) and therefore our tupple must be transformed into a list in order to use this method.



2 (e)  #### Sorter.time_trials() uses “time()”. Look up the documentation at https://docs.python.org and figure out what this function returns. #####

-> "Return the time in seconds since the epoch as a floating point number." (according to the documentation)
