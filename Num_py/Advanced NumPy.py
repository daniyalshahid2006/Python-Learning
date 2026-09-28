import numpy as np
#
# # numbers = np.array([10, 25, 5, 40, 15])
# #
# # result = np.where(numbers > 20, 1, 0)
# #
# # print(result)
#
#
# # np.where(condition, value_if_true, value_if_false)
# # np.where(numbers > 20, numbers, 0)
#
# numbers = np.array([10, 20, 10, 30, 20, 40, 30])
#
# print(np.unique(numbers))
#
# values, counts = np.unique(numbers, return_counts=True)
#
# print(values)
# print(counts)
#
#
#
# import numpy as np
#
# numbers = np.array([40, 10, 50, 20, 30])
#
# print(np.sort(numbers))
# sorted_numbers = np.sort(numbers)
#
# print(sorted_numbers)
#
#
# numbers = np.array([
#     [30, 10, 20],
#     [60, 40, 50]
# ])
#
# print(np.sort(numbers))


numbers = np.array([10, 50, 30, 80, 20])

print(np.max(numbers))
print(np.argmax(numbers))

print(np.min(numbers))
print(np.argmin(numbers))

numbers = np.array([40, 10, 30, 20])

print(np.argsort(numbers))