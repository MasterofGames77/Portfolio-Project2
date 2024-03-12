from games import games

from linked_list import LinkedList

def greet():
    print("Hello, this is Michael's video game recommendation program.")
    print("This program will provide you with a variety of different video games from different genres.")

# Write code to insert game types into data structure (LinkedList) here. The data is in data.py
def insert_game_genres():
    game_genre_list = LinkedList()
    for game_genre in games:
        game_genre_list.insert_beginning(game_genre)
    return game_genre_list


# Write code to insert game data into data structure (LinkedList) here. 
def insert_game_data():
    game_data_list = LinkedList()
    for game_genre in games:
        game_sublist = LinkedList()
        for game in games:
            if game[0] == game_genre:
                 game_sublist.insert_beginning(game)
        game_data_list.insert_beginning(game_sublist)
    return game_data_list

my_games_list = insert_game_genres()
my_games_list = insert_game_data()

selected_game_genre = ""

# Code for User instruction
while len(selected_game_genre) == 0:
    user_input = str(input("\nWhat genre of game would you like to play?\nType the name of the genre and press enter to see it it's here.\n")).lower()

    # Search for user_input in game genres data_structure
    matching_genres = []
    genre_list_head = my_games_list.get_head_node()
    while genre_list_head is not None:
        if str(genre_list_head.get_value()).startswith(user_input):
            matching_genres.append(genre_list_head.get_value())
        genre_list_head = genre_list_head.get_next_node()

    # print list of matching game genres
    for game in matching_genres:
        print(game)

    # Check if only one game genre was found, ask user if they would like to select this genre.
    if len(matching_genres) == 1:
        select_genre = str(input("\nThe only matching genre for the specified input is " + matching_genres[0] + ". \nDo you want to look at " + matching_genres[0] + " games? Enter y for yes and n for no\n")).lower()

        # After finding game genre write code for retrieving game data here
        if select_genre == 'y':
            selected_game_genre = matching_genres[0]
            print("Selected Game Genre: " + selected_game_genre)
            game_list_head = my_games_list.get_head_node()
            while game_list_head.get_next_node() is not None:
                sublist_head = game_list_head.get_value().get_head_node()
                if sublist_head.get_value()[0] == selected_game_genre:
                    while sublist_head.get_next_node() is not None:
                        print("---------------------------------")
                        print("Name: " + sublist_head.get_value()[1])
                        print("Developer: " + sublist_head.get_value()[2])
                        print("Released On: " + sublist_head.get_value()[3])
                        print("Release Year: " + sublist_head.get_value()[4])
                        print("--------------------------\n")
                        sublist_head = sublist_head.get_next_node()
                game_list_head = game_list_head.get_next_node()

            # Ask user if they would like to search for other genres of games
            repeat_loop = str(input("\nDo you want to find other game genres? Enter y for yes and n for no.\n")).lower()
            if repeat_loop == 'y':
                selected_game_genre = ""
            else:
                print("Thank you for using Michael's Video Game Recommendation program.")