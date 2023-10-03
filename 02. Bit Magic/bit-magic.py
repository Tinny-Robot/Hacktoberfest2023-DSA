def count_set_bits(num):
    # Function to count the number of set bits in a binary representation of num
    count = 0
    while num:
        count += num & 1
        num >>= 1
    return count

def find_ranges_with_set_bit_sum(arr, X):
    n = len(arr)
    prefix_set_bits = [0] * (n + 1)
    
    # Calculate the prefix sum of set bits in the array
    for i in range(1, n + 1):
        prefix_set_bits[i] = prefix_set_bits[i - 1] + count_set_bits(arr[i - 1])
    
    # Create a dictionary to store the starting index of each prefix sum
    index_dict = {}
    ranges = []
    
    for i in range(n + 1):
        prefix_sum = prefix_set_bits[i]
        if prefix_sum - X in index_dict:
            for start in index_dict[prefix_sum - X]:
                ranges.append((start, i - 1))
        if prefix_sum not in index_dict:
            index_dict[prefix_sum] = [i]
        else:
            index_dict[prefix_sum].append(i)
    
    return ranges
