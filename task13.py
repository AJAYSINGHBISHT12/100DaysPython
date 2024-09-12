# # # #debugging
# # # def my_function():
# # #     for i in range(1,21):
# # #         if i == 20:
# # #             print("you got it")
# # #
# # # my_function()
# # #  # Describe the problem - write your answers as comments:
# # #  #  1.What is the for loop doing?
# # #  #  2.What is the function meant to print "you got it"?
# # #  #  3.what are your assumptions about the value of i?
# # from random import randint
# # dice_images = ["1","2","3","4","5","6"]
# # dice_num = randint(0,5)
# # print(dice_images[dice_num])
# try:
#     age = int(input("How old are you?"))
# except ValueError:
#     print("You have typed in  a an invalid number. please try again with a numerical response!")
#     age = int(input("How old are you?"))
# if age > 18:
#     print(f"you can drive at age {age}.")
word_per_page = 0
pages = int(input("Number of pages: "))
print(pages)
word_per_page = int  (input("Number of words per page: "))
print(word_per_page)
total_words = pages * word_per_page
print(total_words)

