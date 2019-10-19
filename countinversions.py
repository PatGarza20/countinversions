# By Patricio Garza / https://github.com/PatGarza20

#Global Variables
inversions = 0

def countInversions(data):
    global inversions
    # No array to split if there's only one number left.
    if len(data) == 1:
        return data

    # Current array is split in half, then
    # countInversions() is recursively called with the halves.
    else:
        length = int(len(data)/2)

        former = data[:length]
        latter = data[length:]

        countInversions(former)
        countInversions(latter)

        x = 0
        y = 0
        z = 0
    
    # x and y iterate through the halves to compare values.
    # z adds values to the data array in their sorted order.
    # Since x already tracks how many times an element in former is smaller than latter,
    # then len(former) - x returns the number of inversions.
    while x < len(former) and y < len(latter):
        if int(former[x]) <= int(latter[y]):
            data[z] = former[x]
            x += 1

        else: 
            data[z] = latter[y]
            y += 1
            inversions += (len(former) - x)
        z += 1
    
    # Adds what remains in the halves to data after the previous function.
    while x < len(former):
        data[z] = former[x]
        x += 1
        z += 1

    while y < len(latter):
        data[z] = latter[y]
        y += 1
        z += 1

def main():
    # Reads data from the given file
    # split() turns raw data into an array.
    # e.g 0 1 1 becomes ['0', '1', '1']
    with open('input1.txt', 'r') as file:
        data = file.read()
        actualData = data.split()

    # Performs recursive Merge Sort
    # and counts inversions using the global variable.
    countInversions(actualData)

    # Prints # of inversions and sorted array.
    global inversions

    print(int(inversions))
    print(actualData)
    
main()