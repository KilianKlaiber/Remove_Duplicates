"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. 
The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

"""

from multiprocessing import Process


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

    result = remove_Duplicates(num_array)
    print("number_of_instances: ", number_of_instances)

    print(result)

    print("number of unique elements: ", len(result))


# Global variable counting how often remove_Duplicates is called:
number_of_instances = 0


def remove_Duplicates(array: list):
    global number_of_instances
    number_of_instances += 1

    if len(array) == 0 or len(array) == 1:
        number_of_instances -= 1
        return array

    else:

        # If the list has two or more elements, then divide the list into two
        # lists of equal size
        middle = len(array) // 2

        left_array = array[:middle]
        right_array = array[middle:]

        # Make sure that the left and the right list do not have equal elements.
        # If they do, then delete them
        while left_array[-1] == right_array[0]:
            if len(right_array) >= 2:
                right_array = right_array[1:]
            elif len(left_array) >= 2:
                left_array = left_array[:-1]
            else:
                right_array = []
                break
        print("left array: ", left_array)
        print("right array: ", right_array)

        # Recursively apply the function to the left and right list. Concatenate the
        # results and return it as result.

        if number_of_instances <= 8:
            right = Process(
                target=remove_Duplicates, args=right_array
            )  # Create a Process object
            right.start()  # Start the process
            left = remove_Duplicates(left_array)
            right.join()  # Wait for the process to finish
            result = left

        number_of_instances -= 1
        return remove_Duplicates(left_array) + remove_Duplicates(right_array)


if __name__ == "__main__":
    main()
