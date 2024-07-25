# Measure timing and  plot result

import matplotlib.pyplot as plt
import timeit
from random import shuffle
from multiprocessing import Pool


def measure_time(source, algorithm, data):
    setup_code = f"from {source} import {algorithm}"
    stmt = f"{algorithm}({data})"
    execution_time = timeit.timeit(stmt, setup=setup_code, number=1)
    return execution_time


kilian_merge_times = []
merge_times = []
input_sizes = [10, 100, 1000,10000]

for size in input_sizes:
    input_array = list(range(size))
    shuffle(input_array)
    
    # calculate merge times for kilian2_merge algorithm
    kilian_time = measure_time(
        source="kilian2_merge", 
        algorithm="kilian2_merge", 
        data=input_array
    )
    kilian_merge_times.append(kilian_time)
    
    # Calculate merge times for merge_sort algorithm
    merge_time = measure_time(
        source="merge_sort", 
        algorithm="merge_sort", 
        data=input_array
    )
    merge_times.append(merge_time)
    
# Plot the first curve for kilian2 algo
plt.plot(input_sizes, kilian_merge_times, label="kilian2")
# Plot the second curve for merge_sort algo
plt.plot(input_sizes, merge_times, label="merge sort")


plt.xlabel("Input Size")
plt.ylabel("Execution Time (seconds)")
plt.title("Time Complexity of Searchin Algorithms")
plt.legend()
plt.show()