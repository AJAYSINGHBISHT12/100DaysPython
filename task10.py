# #Calculator
# def format_name(f_name, l_name):
#     """Take a first
#     and last name
#     and format it to return the title case
#     version of the name."""
#     # if f_name =="" or l_name=="":
#     #     return "You did not provide valid inputs"
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     return f"Result:{formated_f_name} {formated_l_name}"
# formatted_name = format_name("AAngela","ANGELA")
# # print(format_name(input("What is your first name?"), input("What is your last name")))
# # print(formated_string)
# # def function_1(text):
# #     return text + text
# #
# # def function_2(text):
# #     return text.title()
# #
# # output = function_2(function_1("hello"))
# # print(output)
# length = len(formatted_name)
mark = True
while(mark == True):
    x = int(input("What's the first number?:"))
    print("+\n-\n*\n/")
    y = input("Pick an operation:")
    z = int(input("What's the second number?:"))
    if y == "+":
        print(x + z)
    elif y == "-":
        print(x - z)
    elif y == "*":
        print(x * z)
    elif y == "/":
        print(x / z)
    a = input("Restart the calculator 'yes' or 'no'.").lower()
    if a == "yes":
        mark=True
    else:
        mark = False


