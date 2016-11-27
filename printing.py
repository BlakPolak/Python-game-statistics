from reports import *


def count_games_print(data_file_name):
    print ('In file is ' + str(count_games(data_file_name)) + ' games.')


def decide_print(data_file_name, year):
    if decide(data_file_name, year) is True:
        print ('Yes, there is a game from ' + str(year) + '.')
    else:
        print ('No, there is no game from ' + str(year) + '.')


def get_latest_print(data_file_name):
    print ('The latest game is: ' + str(get_latest(data_file_name)) + '.')


def count_by_genre_print(data_file_name, genre):
    print ('On the list is ' + str(count_by_genre(data_file_name, genre)) + ' ' + genre + ' games.')


def get_line_number_by_title_print(data_file_name, title):
    try:
        print ('Game ' + str(title) + ' is on the line ' + str(get_line_number_by_title(data_file_name, title)) + ' in Gamelist.')
    except ValueError:
        print (str(title) + ' in not in Gamelist.')
