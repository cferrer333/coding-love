# Question 1
# def hello_name(user_name):
#     print("Hello " + user_name)

# hello_name('Brandon')

# Question 2
# def first_odds(num):
#         odd_numbers=[]
#         for num in range(1,100,2):
#             odd_number = num
#             odd_numbers.append(odd_number)
#         print(odd_numbers)
#         return ""

# first_odds(1)

# Question 3
# def max_num_in_list(a_list):
#     max_num = a_list[0]

# loops through list until largest number is greater than x then 
# returns largest number
#     for x in a_list:
#         if x > max_num:
#             max_num = x
    
#     return max_num

# num_list=[1,2,3,4,5,234,45,98495,2]
# print("The largest number is: ", max_num_in_list(num_list))

# Question 4
# def is_leap_year(a_year):
#     leap_year=True
#     while leap_year == True:
#         if a_year % 400 == 0:
#             leap_year=True
#         elif a_year % 100 == 0:
#             leap_year=False
#         elif a_year % 4 == 0:
#             leap_year=True
#         return print(leap_year) 
    
# is_leap_year(400)

# Question 5
# sum of list of numbers "x"
# if the largest number in list "x"
#  max(x) = x * (x+1) /2  returns true and is consecutive
# def is_consecutive(a_list):
#     maximum = max(x)
#     if sum(x) == maximum * (maximum + 1) / 2: 
#         return print(True)
#     else: 
#         return print(False)

# x = [1,2,3,4,5,6,7,8,9]

# is_consecutive(x)
