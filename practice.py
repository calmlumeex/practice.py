# how_many_snakes = 1
# snake_string = """
# Welcome to Python3!
#              ____
#             / . .\\
#             \  ---<
#              \  /
#    __________/ /
# -=:___________/
#
# <3, Juno
# """
#
# print(snake_string * how_many_snakes)
# name = input("Enter your name ")
# print("Hello there, {}!".format(name.title()))
# result = eval(input("Enter an expression: "))
# print(result)

# names= input("Enter names separated by commas: ").title().split(',')
# assignments= input("Enter assignment_counts separated by commas: ").split(',')
# grades= input("Enter grades separated by commas: ").split(',')
#
# message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
# submit before you can graduate. You're current grade is {} and can increase \
# to {} if you submit all assignments before the due date.\n\n"
# for name, assignment, grade in zip(names, assignments, grades):
#     print(message.format(name, assignment, grade, (int(grade)+(2*int(assignment)))))

# f = open('some_file.txt', 'r')
# file_data = f.read()
# f.close()
# print(file_data)

# files = []
# for i in range(10000):
#     files.append(open('some_file.txt', 'r'))
#     print(i)

# f =open('some_fle.txt','w')
# f.write("Hello")
# f.close()

# f=open('some_file.txt','w')
# f.write('''Hello!!\nYou've read the contents of this file!''')

# def chunker(iterable, size):
#     for i in  range(0, len(iterable), size):
#         yield iterable[i:i+size]
#     # Implement function here
# for chunk in chunker(range(25), 4):
#     print(list(chunk))
