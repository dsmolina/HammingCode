# Copyright 2023 Dasha Smolina dsmolina@bu.edu
 
def calcRedundantBits(m):
 
    # 2 ^ result >= data_length+ r + 1
 
    for i in range(m):
        if(2**i >= data_length+ i + 1):
            return i
 
def posRedundantBits(data, result):
 
    j = 0
    k = 1
    data_length= len(data)
    res = ''
 
    # If position is power of 2 then insert '0'
    # Else append the data
    for i in range(1, data_length+ result+1):
        if(i == 2**j):
            res = res + '0'
            j += 1
        else:
            res = res + data[-1 * k]
            k += 1
 
    # The result is reversed since positions are
    # counted backwards. (data_length+ r+1 ... 1)
    return res[::-1]
 
 
def calcParityBits(arr, result):
    n = len(arr)
 
    # For finding rth parity bit, iterate over
    # 0 to r - 1
    for i in range(result):
        val = 0
        for j in range(1, n + 1):

            if(j & (2**i) == (2**i)):
                val = val ^ int(arr[-1 * j])

        arr = arr[:n-(2**i)] + str(val) + arr[n-(2**i)+1:]
    return arr
 
 
def detectError(arr, nr):
    n = len(arr)
    res = 0
 
    for i in range(nr):
        val = 0
        for j in range(1, n + 1):
            if(j & (2**i) == (2**i)):
                val = val ^ int(arr[-1 * j])
        res = res + val*(10**i)

    return int(str(res), 2)
 
 
# data to be transmitted
data = '1011001'
 
# Calculate number of Redundant Bits Required
data_length= len(data)
result= calcRedundantBits(data_length)
 
# Find positions of Redundant Bits
arr = posRedundantBits(data, result)
 
# Find the parity bits
arr = calcParityBits(arr, result)
 
# Data to be transferred
print("Data transferred is " + arr) 
 
# Stimulate error in transmission by changing
# a bit value.
# 10101001110 -> 11101001110, error in 10th position.
 
arr = '11101001110'
print("Error Data is " + arr)
correction = detectError(arr, result)
if(correction==0):
    print("There is no error in the received message.")
else:
    print("The position of error is ",len(arr)-correction+1,"from the left")