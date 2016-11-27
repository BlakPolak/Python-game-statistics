import csv
import operator


def count_games(data_file_name):
    """Return number_of_games in list"""
    read_file = open(data_file_name, 'r')
    number_of_games = 0
    for row in read_file:
        number_of_games += 1
    return number_of_games


def decide(data_file_name, year):
    """Checks if Gamelist contains game from given year"""
    with open(data_file_name) as f:
        file_reader = csv.reader(f, delimiter='\t')
        game_list = list(file_reader)
    for indx, line in enumerate(game_list):
        if str(year) in line[2]:
            return True


def get_latest(data_file_name):
    """Return name of the latest game from list"""
    with open(data_file_name) as f:
        file_reader = csv.reader(f, delimiter='\t')
        sortedlist = sorted(file_reader, key=lambda row: row[2], reverse=True)
        return str(sortedlist[0][0])


def count_by_genre(data_file_name, genre):
    """Returns a number of games by given genre"""
    with open(data_file_name) as f:
        file_reader = csv.reader(f, delimiter='\t')
        game_list = list(file_reader)
    n = 0
    for row in range(len(game_list)):
        if genre in game_list[row][3]:
            n += 1
    return n


def get_line_number_by_title(data_file_name, title):
    """Returns line number where given title is on the list"""
    with open(data_file_name) as f:
        file_reader = csv.reader(f, delimiter='\t')
        game_list = list(file_reader)
    for indx, line in enumerate(game_list):
        if title in line[0]:
            return indx+1
    if title not in line[0]:
        raise ValueError
