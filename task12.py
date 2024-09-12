# enemies = 1
#
# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside function: {enemies}")
#
# increase_enemies()
# print(f"enemies outside function: {enemies}")
# # Local Scope
# # def drink_potion():
# #     potion_strength = 2
# #     print(potion_strength)
# # global variable
# player_health = 10
#
# def drink_potion():
#     potion_strength = 2
#     print(player_health)
#
# drink_potion()
# # print(potion_strength)
# game_level = 3
# enemies = ["Skelton", "Zombie", "alien"]
# def create_enemy():
#     if game_level < 5:
#         new_enemy = enemies[0]
#     print(new_enemy)
# create_enemy()
#
# animal = 1
# def increase():
#     global animal
#     animal += 1
#     print(animal)
#
# increase()
# print(animal)
# Global Constants

#
i = 50


def foo():
    i = 100
    return i


foo()
print(i)