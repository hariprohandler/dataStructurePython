from util import time_it
@time_it
def linear_search(number_list, number_to_find):
    for index, element in enumerate(number_list):
        if element == number_to_find:
            return index;
    return -1
@time_it
def binary_search(number_list, number_to_find):
    left_indx = 0
    right_index = len(number_list)-1
    mid_index = 0
    #find mid index
    while left_indx <= right_index:
        mid_index = (left_indx +right_index) // 2  #return integer
        mid_number = number_list[mid_index]
        if(mid_number == number_to_find):
            return mid_index;
        
        if mid_number < number_to_find:
            left_indx = mid_index + 1
        else:
            right_index = mid_index -1
    return -1;


if __name__ == '__main__':
    number_list = [12,15,17,19,21,24,45,67]
    number_to_find = 10000
    number_list = [i for i in range(1000001)];
    index = linear_search(number_list, number_to_find);
    print(f"Number found at index {index} using linear search")
    index = binary_search(number_list, number_to_find);
    print(f"Number found at index {index} using binary search")