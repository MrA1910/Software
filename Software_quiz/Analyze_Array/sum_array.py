import json


def sum_min_max(filename):
    with open(filename, 'r') as file:
        data = json.load(file)["data"]

    total_sum = 0
    results = []
    for array in data:
        if len(array) > 0:  # Check if the array is not empty
            min_val = min(array)
            max_val = max(array)
            array_sum = min_val + max_val
            results.append(array_sum)
            total_sum += array_sum

    return total_sum, results


total, results = sum_min_max('input.json')
#print(f"Sum of min and max in each array: {results}") #Display resilt of each Array
print(f"Total sum: {total}")
