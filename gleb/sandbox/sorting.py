def sorting(list):
     return sorted(list, key=lambda x: list.count(x), reverse=True)
#print(*sorting([2, 3, 5, 3, 7, 9, 5, 3, 7, 3, 5]))
#3 3 3 3 5 5 5 7 7 2 9
# def sorting(list):
#     return sorted(list, key=lambda x: (list.count(x), x), reverse=True)
# #print(*sorting([2, 3, 5, 3, 7, 9, 5, 3, 7, 3, 5]))
# #3 3 3 3 5 5 5 7 7 9 2


# Nikita code for education
# my_list = [2, 3, 5, 3, 7, 9, 5, 3, 7, 3, 5]
# numbers_and_counts = {}
#
# for my_number in my_list:
#     numbers_and_counts[my_number] = 1 if not my_number in numbers_and_counts.keys() else numbers_and_counts[
#                                                                                              my_number] + 1
# print(numbers_and_counts, 'numbers_and_counts')
# sorted_counts_from_numbers_and_counts = sorted(numbers_and_counts.values(), reverse = True)
# print(sorted_counts_from_numbers_and_counts, 'sorted_counts_from_numbers_and_counts')
# sorted_numbers_and_counts = {}
#
# for item in sorted_counts_from_numbers_and_counts:
#     for i in numbers_and_counts.keys():
#         if numbers_and_counts[i] == item:
#             sorted_numbers_and_counts[i] = numbers_and_counts[i]
# print(sorted_numbers_and_counts, 'sorted_numbers_and_counts')
# result = []
# for i, j in sorted_numbers_and_counts.items():
#     result += [i] * j
# print(*result)
