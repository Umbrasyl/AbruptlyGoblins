def add_gamer(gamer, gamers_list):
    keys_that_should_exist = ["name", "availability"]
    for key in gamer.keys():
        if key not in keys_that_should_exist:
            return False
    gamers_list.append(gamer)


gamers = []
add_gamer({"name": "Kimberly Warner", "availability": ["Monday", "Tuesday", "Friday"]}, gamers)
add_gamer({'name': 'Thomas Nelson', 'availability': ["Tuesday", "Thursday", "Saturday"]}, gamers)
add_gamer({'name': 'Joyce Sellers', 'availability': ["Monday", "Wednesday", "Friday", "Saturday"]}, gamers)
add_gamer({'name': 'Michelle Reyes', 'availability': ["Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name': 'Stephen Adams', 'availability': ["Thursday", "Saturday"]}, gamers)
add_gamer({'name': 'Joanne Lynn', 'availability': ["Monday", "Thursday"]}, gamers)
add_gamer({'name': 'Latasha Bryan', 'availability': ["Monday", "Sunday"]}, gamers)
add_gamer({'name': 'Crystal Brewer', 'availability': ["Thursday", "Friday", "Saturday"]}, gamers)
add_gamer({'name': 'James Barnes Jr.', 'availability': ["Tuesday", "Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name': 'Michel Trujillo', 'availability': ["Monday", "Tuesday", "Wednesday"]}, gamers)


def calculate_availability(gamers_list):
    week_dict = {"Monday": 0, "Tuesday": 0, "Wednesday": 0, "Thursday": 0, "Friday": 0, "Saturday": 0, "Sunday": 0}
    for gamer in gamers_list:
        for day in gamer["availability"]:
            week_dict[day] += 1
    return week_dict


def find_best_night(week):
    best_day = ""
    highest_count = 0
    for day, count in week.items():
        if count > highest_count:
            highest_count = count
            best_day = day
    return best_day


def available_on_night(gamers_list, day):
    attending_list = []
    for gamer in gamers_list:
        if day in gamer["availability"]:
            attending_list.append(gamer["name"])
    return attending_list


def send_email(gamers_who_can_attend, day, game):
    form_email = "Hi {name}. We will be playing {game} on {day_of_week} night."
    for gamer in gamers_who_can_attend:
        print(form_email.format(name=gamer, game=game, day_of_week=day))


game_night = find_best_night(calculate_availability(gamers))
attending_gamers = available_on_night(gamers, game_night)
send_email(attending_gamers, game_night, "Abruptly Goblins")

rest_of_gamers = []
for that_gamer in gamers:
    if not that_gamer["name"] in attending_gamers:
        rest_of_gamers.append(that_gamer)

second_night = find_best_night(calculate_availability(rest_of_gamers))
second_night_gamers = available_on_night(rest_of_gamers, second_night)
send_email(second_night_gamers, second_night, "Abruptly Goblins")
