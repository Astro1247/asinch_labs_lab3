import threading
import random

arrays_count = 2
arrays = [int] * arrays_count
threads = [threading.Thread] * arrays_count


def array_random_filler_thread(arrays, index):
    arrays[index] = [random.randrange(-100, 100) for _ in range(50)]


if __name__ == '__main__':
    for i in range(len(threads)):
        threads[i] = threading.Thread(target=array_random_filler_thread, args=(arrays, i))
        threads[i].start()
    # Defined threads for filling arrays, waiting while they are finished
    for i in range(len(threads)):
        threads[i].join()
    print("Filled arrays:\n{}".format(arrays))

    print("Max value of first arr: {}\n0.5 of its value: {}".format(max(arrays[0]), max(arrays[0])*0.5))

    arrays[0] = list(filter(lambda x: x > max(arrays[0])*0.5, arrays[0]))
    arrays[1] = list(filter(lambda x: x%2 == 0, arrays[1]))
    print("Filtered first array to 0.5 of max value\nFiltered second array to be even\nResult:\n{}".format(arrays))
    print("Sorting elements and creating array from elements of second array that are not present in first")
    new_arr = list(filter(lambda x: x not in arrays[0], arrays[1]))
    print("Result:\n{}\nRemoved {} elements from second array.".format(new_arr, len(arrays[1])-len(new_arr)))
