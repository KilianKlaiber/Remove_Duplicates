"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. 
The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

"""

from concurrent.futures import ProcessPoolExecutor


def main():

    num_array = [
        0,
        0,
        1,
        1,
        1,
        2,
        2,
        3,
        3,
        4,
        4,
        4,
        5,
        5,
        5,
        5,
        6,
        7,
        8,
        8,
        8,
        8,
        10,
        12,
        32,
        45,
        45,
    ]
    
    
    
    array1 = list(range(5000))
    array2 = list(range(4000))
    
    zipped = zip(array1, array2)
    
    duplist = []
    for items in zipped:
        duplist.append(items[0])
        duplist.append(items[1])

    
    new_list = remove_Duplicates(duplist)
    
    print(new_list)



def remove_Duplicates(array: list):

    if get_second_element(array) == None:
        return array

    else:

        # If the list has two or more elements, then divide the list into two
        # lists of equal size
        middle = len(array) // 2
        left_array = array[:middle]
        right_array = array[middle:]

        # Delete duplicates at middle:
        while get_last_element(left_array) == get_first_element(right_array):
            right_array = right_array[1:]

    # Use ProcessPoolExecutor to process each half in parallel
    with ProcessPoolExecutor(max_workers=2) as executor:
        # submit tasks to be executed
        futures = [
            executor.submit(remove_Duplicates, left_array),
            executor.submit(remove_Duplicates, right_array),
        ]
        # Collect the results from these tasks
        results = [future.result() for future in futures]

    return results[0] + results[1]


def get_first_element(array):

    try:
        first_element = array[0]
        return first_element
    except:
        return None


def get_second_element(array):
    try:
        seond_element = array[1]
        return seond_element
    except:
        return None


def get_last_element(array):
    try:
        last_element = array[-1]
        return last_element
    except:
        return None


if __name__ == "__main__":
    main()
