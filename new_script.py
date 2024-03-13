import string
from data import *

from linked_list import LinkedList

def greet():
    print("Hello, this is Michael's video game recommendation program.")
    print("This program will provide you with a variety of different video games from different genres.")

def get_search_on():
    search_by = " "
    while len(search_by) == 0:
        user_input = str(input("\nTo see a list of game genres, enter g.")).lower()
        if user_input != "g":
            print("\nThat is not a valid response. Please try again.")
        else:
            search_by = "genre"
    return search_by

def insert_genre_types():
    genre_list = LinkedList()
    for genre in genres:
        genre_list.insert_beginning(genre)
    return genre_list

def insert_game_data_genre():
    game_data_list = LinkedList()
    remove_list = []
    for genre in genres:
        genre_sublist = LinkedList()
        for game in games:
            index = 0
            while index < len(game[0]):
                if game[0][index] == genre:
                    game_this_genre = [genre] + game
                    genre_sublist.insert_beginning(game_this_genre, 2)
                index += 1
        if genre_sublist.get_head_node().get_value() != None:
            game_data_list.insert_beginning(genre_sublist)
        else:
            remove_list.append(genre)
    return game_data_list, remove_list

print(greet)

search_by = get_search_on()

my_type_list = insert_genre_types()
my_game_list, remove_list = insert_game_data_genre()

selected_type = ""

while len(selected_type) == 0:
    user_input = str(input("\nWhat genre of game would you like to play?\nType the beginning of that {0} and press enter to see if it's here.\n".format(search_by))).title()

    matching = []
    current_node = my_type_list.get_head_node()
    while current_node is not None:
        if str(current_node.get_value()).title().startswith(user_input) and not current_node.get_value() in remove_list and not current_node.get_value()[0] in remove_list:
            matching.append(current_node.get_value())
        current_node = current_node.get_next_node()

    if len(matching) > 1:
        print("\nMore than one {0} matches that search: ".format(search_by))
        for match in matching:
            print(match)

    if len(matching) == 0:
        print("\nSorry, there are no {0}s that match that search\n".format(search_by))

    if len(matching) == 1:
        if search_by == "letter":
            select_games = "y"
        else:
            select_games = str(input("\n\There is only one {1} that mathces your search: {0} \n\n\nDo you want to look at {0} games? Enter y for yes and n for no.\n".format(matching[0], search_by))).lower()

        if select_games == "y":
            selected_type = matching[0]
            print("----------------------------")
            print("Selected {1}: {0}".format(matching[0], search_by))
            print("--------------------------\n")
            my_game_head = my_game_list.get_head_node()
            while my_game_head:
                sublist = my_game_head.get_value().get_head_node()
                if sublist.get_value() is not None and sublist.get_value()[0] == selected_type:
                    while sublist is not None:
                        title = sublist.get_value()[2]
                        game_genre = ",".join(sublist.get_value()[1])
                        developer = sublist.get_value()[3]
                        g_system = sublist.get_value()[4]
                        release = sublist.get_value()[5]
                        sublist = sublist.get_next_node()
                my_game_head = my_game_head.get_next_node()

        repeat = str(input("\nDo you want to search for other games in another {0}? Enter y for yes and n for no.\n".format(search_by))).lower()
        selected_type = ""
        if repeat == "n":
            search_again = str(input("\nWould you like to begin another game search? Enter y for yes and n for no.\n"))
            if search_again == "y":
                selected_type = ""
                search_by = get_search_on()
                my_type_list = insert_genre_types()
                my_game_list, remove_list = insert_game_data_genre()
            else:
                print("Thank you for using Michael's Video Game Recommendation program.")