# Measure timing and  plot result for deleting duplicates

import matplotlib.pyplot as plt
import timeit
from random import shuffle
from multiprocessing import Pool


def measure_time(source, algorithm, data):
    setup_code = f"from {source} import {algorithm}"
    stmt = f"{algorithm}({data})"
    execution_time = timeit.timeit(stmt, setup=setup_code, number=1)
    return execution_time


multi_times = []
simple_times = []
input_sizes = [10, 100, 1000, 10000]


for size in input_sizes:
    
    array1 = list(range(size))
    array2 = list(range(size))

    zipped = zip(array1, array2)

    duplist = []
    for items in zipped:
        duplist.append(items[0])
        duplist.append(items[1])

    
    # calculate remove times for multiprocessing algorithm
    time = measure_time(
        source="multiprocess", 
        algorithm="multiremove_Duplicates", 
        data=duplist
    )
    multi_times.append(time)
    
    # Calculate remove times for simple algorithm
    time = measure_time(
        source="main", 
        algorithm="remove_Duplicates", 
        data=duplist
    )
    simple_times.append(time)
    
# Plot the first curve for kilian2 algo
plt.plot(input_sizes, multi_times, label="multi")
# Plot the second curve for merge_sort algo
plt.plot(input_sizes, simple_times, label="simple")


plt.xlabel("Input Size")
plt.ylabel("Execution Time (seconds)")
plt.title("Time Complexity of Searchin Algorithms")
plt.legend()
plt.show()