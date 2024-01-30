import timeit as time
import random as ran
import matplotlib.pyplot as plt



def insertion_sort(arr):
    for ind in range(1, len(arr)):
        ele = arr[ind]
        index = ind - 1
        while index >= 0:
            if arr[index] > ele:
                arr[index + 1] = arr[index]
                index -= 1
            else:
                break
        arr[index + 1] = ele


def selection_sort(arr):
     for start_ind in range(len(arr)):
        smallest_element=arr[start_ind]
        ele_ind=start_ind
        for i in range(start_ind+1,len(arr)):
            if(arr[i]<smallest_element):
                smallest_element=arr[i]
                ele_ind=i
   
        arr[start_ind],arr[ele_ind]=arr[ele_ind],arr[start_ind]
       

def bubble_sort(arr):
    for _ in range(len(arr)):
        for ele in range(len(arr)-1):
            if(arr[ele]>arr[ele+1]):
                arr[ele],arr[ele+1]=arr[ele+1],arr[ele]

# Function to generate a random arr of a given size
def generate_random(size):
    return [ran.randint(1, 1000) for _ in range(size)]

# Function to benchmark sorting algorithms
def benchmark(sort_func, arr):
    setup_code = f"from __main__ import {sort_func}, generate_random; arr = generate_random({len(arr)})"
    stmt = f"{sort_func}(arr)"

    # Measure the execution time
    exe_time = time.timeit(stmt, setup=setup_code, number=5)

    return exe_time

# Benchmark parameters
sizes = [5, 10, 20, 50, 100, 200, 500, 1000,2000,3000,4000,5000]  # Adjust as needed

# Results dictionary to store benchmark results
results = {'Insertion Sort': [], 'Selection Sort': [], 'Bubble Sort': []}

# Run benchmarks for each sorting algorithm and arr size
for size in sizes:
    arr = generate_random(size)

    # Insertion Sort
    ins_time = benchmark('insertion_sort', arr)
    results['Insertion Sort'].append(ins_time)
    print(f"Input Size: {size}, Insertion Sort Execution Time: {ins_time:.6f} seconds")


    # Selection Sort
    sel_time = benchmark('selection_sort', arr)
    results['Selection Sort'].append(sel_time)
    print(f"Input Size: {size}, Selection Sort Execution Time: {sel_time:.6f} seconds")

    # Bubble Sort
    bub_time = benchmark('bubble_sort', arr)
    results['Bubble Sort'].append(bub_time)
    print(f"Input Size: {size}, Bubble Sort Execution Time: {bub_time:.6f} seconds")

# Plotting the results
plt.plot(sizes, results['Insertion Sort'], label='Insertion Sort', color='red')
plt.plot(sizes, results['Selection Sort'], label='Selection Sort', color='blue')
plt.plot(sizes, results['Bubble Sort'], label='Bubble Sort', color='green')

plt.xlabel('Array Size')
plt.ylabel('Runtime (sec)')
plt.title('Benchmark Sorting Algorithm')
plt.legend()
plt.show()