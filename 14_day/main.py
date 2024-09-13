from game_data import data
import random

cnt = 1
score = 0
while(cnt==1):
    selected_personality1=random.choice(data)
    filtered_data = [item for item in data if item != selected_personality1]
    selected_personality2=random.choice(filtered_data)
    def personality():
        selected_personality1_name=selected_personality1["name"]
        selected_personality1_description = selected_personality1["description"]
        selected_personality1_country = selected_personality1["country"]
        print(f"Compare A: {selected_personality1_name}, a {selected_personality1_description},from {selected_personality1_country}")
        selected_personality2_name=selected_personality2["name"]
        selected_personality2_description = selected_personality2["description"]
        selected_personality2_country = selected_personality2["country"]
        print(f"Compare B: {selected_personality2_name}, a {selected_personality2_description}, from {selected_personality2_country}")
    personality()
    input_user = input("Who has more followers? Type 'A' or 'B':")
    A = selected_personality1["follower_count"]
    B = selected_personality2["follower_count"]
    if input_user=="A":
        if A>B:
            print("You are right!")
            cnt = 1
            score = score + 1
        else:
            print("Sorry! You are wrong")
            cnt = 0
    elif input_user=="B":
        if B>A:
            print("You Are Right")
            score = score + 1
            cnt = 1
        else:
            print("Sorry! You are wrong")
            cnt = 0
    else:
        cnt = 0
        print("Invalid")

print(score)

