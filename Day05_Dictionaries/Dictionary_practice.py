# student = {
#    "name": "Daniyal",
#     "age": 22,
#     "score": 80,
#     "fav game" : "sekiro"
# }
# print(student["name"])
# student["age"] = 21
# student["country"] = "Pakistan"
# print(student)
# student.pop("score")
# print(student)
# for key in student:
#     print(f"{key}:")
#     for key , value in student.items():
#         print(f"{key}: {value}")
game_name = input("What is your fvrt game name? ")
release_date = int(input("What is release date? "))
rating: int = int(input("What is your rating of the game? "))

game = {
    "game_name": game_name,
    "release_date": release_date,
    "rating": rating
}
print(game)
game["rating"] = int(input("What is your rating of the game? "))
print(game)
key_name = input("What is your key name? ")
value_name = input("What is your value name? ")
game[key_name] = value_name
print(game)
rem = input("what Would you like to remove ")
if rem in game:
    print(f"{rem} is in the dictionary.")
    game.pop(rem)
else:
    print(f"{rem} is not in the dictionary.")

for key, value in game.items():
    print(f"{key}: {value}")