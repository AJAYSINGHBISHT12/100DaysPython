# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")
#
# greet_with_name("Amgela")
# def life_in_weeks(age):
#     print(f"you have {(90 - age) * 52} weeks left")
# life_in_weeks(30)

# def life_in_weeks(age,location):
#     print(f"you have {(90 - age) * 52} weeks left at {location}")
# life_in_weeks(70,"ZHey")
def calculate_love_score(name1,name2):
    x="true"
    z="love"
    y=name1+name2
    m = 0
    n = 0
    for letter in x:
        cnt=0
        for letter1 in y:
            if letter==letter1:
                cnt = cnt + 1
        # print(f"{letter} occurs {cnt} times")
        m = m + cnt

    for letter in z:
        cnt=0
        for letter1 in y:
            if letter==letter1:
                cnt = cnt + 1
        # print(f"{letter} occurs {cnt} times")
        n = n + cnt
    print(f"{m}{n}")


calculate_love_score("angela yu","jack bauer")