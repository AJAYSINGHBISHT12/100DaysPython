#Bidders
# dict = {"AJA": 1,"MAyank":"2"}
# # print(dict["AJA"])
# dict["Loop"]= "The action of doing something over and over again."
# # print(dict)
# empty = {}
# dict = {}
# print(dict)
# student_scores = {
#     'Harry': 88,
#     'Ron': 78,
#     'Hermione': 95,
#     'Draco': 75,
#     'Neville': 60
# }
#
# student_grades ={}
#
# for key in student_scores:
#     if student_scores[key]>=91:
#         print("Outstanding")
#     elif 91> student_scores[key]>=81:
#         print("Exceeds Expectations")
#     elif 81> student_scores[key]>=71:
#         print("Acceptable")
#     elif student_scores[key]<=70:
#         print("Fail")
# travel_log = {
#     "France":{"cities_visited": ["Paris", "Lille", "Dijon"],
#               "total_visits":12},
#     "Germany":{"cities_visited" : ["Stuttgart", "Berlin"],
#                "total_visits" : 5 },
# }
# print(travel_log["France"][1])
# nested_list = ["A","B",["C","D"]]
# print(nested_list[2][1])
# # print(travel_log["France"]["cities_visited"][0])
# empty={1:2,2:3}
# empty[1]=7
# print(empty)
# TODO-1: Ask the user for input
# from task8_1 import should_continue

# name= input("What is Your Name?")
# price = int(input("What is your bid? $"))

#TODO-2: Save data into dictionary{name: price}
# dictionary = {}
# dictionary[name]= price
def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid o f ${highest_bid}.")
# TODO-3: Whether if new bids need to be added
# should_continue =input("Are there any other bidders? Type 'yes' or 'no'.\n")
bids = {}
continue_bidding = True
while continue_bidding:
    name = input("What is Your Name?")
    price = int(input("What is your bid? $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("\ n" * 20)


# TODO-4: Compare bids in dictionary

# print(x)

# print(y)