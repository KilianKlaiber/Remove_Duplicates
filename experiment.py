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

num_array.pop(0)

new_list = [1]

def get_second_element(array):
    try:
        seond_element = array[1]
        return seond_element
    except:
        return None
    
result = get_second_element(new_list)

print(result)