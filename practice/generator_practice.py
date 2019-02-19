# my_nums = (num*num for num in [1,2,3,4,5])
#
# print(list(my_nums))

nums = (num for num in [1,2,3,4,5,6,7,8,9,10])

print(list(nums))



# import random
#
# names = ['john', 'corey', 'adam', 'steve', 'rick', 'thomas']
# majors = ['math', 'engineering', 'compsci', 'arts', 'business']
#
#
# def people_list(num_people):
#     result = []
#     for i in xrange (num_people):
#         person = {
#             'id': i,
#             'name': random.choice(names),
#             'major': random.choice(majors)
#         }
#         result.append(person)
#     return result
#
# def people_generator(num_people):
#     for i in xrange(num_people):
#         person = {
#                     'id': i,
#                     'name': random.choice(names),
#                     'major': random.choice(majors)
#                     }
#         yield person



