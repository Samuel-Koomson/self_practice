new_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#index      0, 1, 2, 3, 4, 5, 6, 7, 8, 9
#index    -10,-9,-8,-7,-6,-5,-4,-3,-2,-1
#[start:end:step]
print([3])
print([-3])
print([10])
print(new_list[1: ])
print(new_list[:4])
print(new_list[::-1])
print(new_list[1:8:3])

#slicing is the function that allows for individual and groups of elements in a list to be accessed. several ways can be used to achieve slicing including reversing and stepping.

sentence = ['myveryeyesmayjustseeundernineplanets']
print(sentence [0:9])
sentence = 'myveryeyesmayjustseeundernineplanets'
print(sentence[0:9])

#when slicing strings, if the variable is initialised to a string in a list, the slicing does not work as desired, rather it prints the entire list unto the console whenever it is sliced
