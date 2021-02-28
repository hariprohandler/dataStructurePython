def merge_two_sorted_list(a,b, arr):
    len_a = len(a)
    len_b = len(b)
    i = j =  k = 0
    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            arr[k] = a[i]
            i += 1
        else:
            arr[k] = b[j]
            j += 1
        k += 1
    
    while i < len_a:
        arr[k] = a[i]
        i += 1
        k += 1
    while j < len_b:
        arr[k] = b[j]
        j += 1
        k += 1

def merge_sort(arr):
    if len(arr) <= 1 :
        return
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    merge_sort(left)
    merge_sort(right)

    merge_two_sorted_list(left, right, arr)

if __name__ == '__main__':
    arr = [5,8,12,56, 7,9,45,51]
    merge_sort(arr)
    print(arr)