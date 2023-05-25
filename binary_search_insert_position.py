def binary_search_insertion_pos(element, sorted_list):
    left = 0
    right = len(sorted_list) - 1

    while left <= right:
        mid = (left + right) // 2

        if sorted_list[mid] == element:
            return mid
        elif sorted_list[mid] < element:
            left = mid + 1
        else:
            right = mid - 1

    # Jika elemen tidak ada dalam daftar, kembalikan posisi sisipan
    return left

# Contoh penggunaan
sorted_list = [2, 4, 6, 8, 10, 12, 14, 16]
element = 9

insertion_pos = binary_search_insertion_pos(element, sorted_list)
print("Posisi sisipan elemen {}: {}".format(element, insertion_pos))
