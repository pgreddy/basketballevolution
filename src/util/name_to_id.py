import sys
import csv

# Script to go from player name to player id

name_col = 13
id_col   = 12

def search(data):
    
    for player_entry in data:
        player = player_entry[name_col].lower()
        #print(target_player + ":" + player)
    
        if target_player == player:
            print(player_entry[id_col])
            sys.exit()

    return

def open_file(path):
    with open(path, 'r') as f:
            reader = csv.reader(f)
            data = list(reader)

    return data


target_player = str(sys.argv[1]).lower() + " " + str(sys.argv[2]).lower()
print(target_player)

print("Parsing in raw data, please wait...")

data = open_file("./data/raw_data/2000-01_pbp.csv")
search(data)

data = open_file("./data/raw_data/2001-02_pbp.csv")
search(data)

data = open_file("./data/raw_data/2002-03_pbp.csv")
search(data)

data = open_file("./data/raw_data/2003-04_pbp.csv")
search(data)

data = open_file("./data/raw_data/2004-05_pbp.csv")
search(data)

data = open_file("./data/raw_data/2005-06_pbp.csv")
search(data)

data = open_file("./data/raw_data/2006-07_pbp.csv")
search(data)

data = open_file("./data/raw_data/2007-08_pbp.csv")
search(data)

data = open_file("./data/raw_data/2008-09_pbp.csv")
search(data)

data = open_file("./data/raw_data/2009-10_pbp.csv")
search(data)

data = open_file("./data/raw_data/2010-11_pbp.csv")
search(data)

data = open_file("./data/raw_data/2011-12_pbp.csv")
search(data)

data = open_file("./data/raw_data/2012-13_pbp.csv")
search(data)

data = open_file("./data/raw_data/2013-14_pbp.csv")
search(data)

data = open_file("./data/raw_data/2014-15_pbp.csv")
search(data)

data = open_file("./data/raw_data/2015-16_pbp.csv")
search(data)

data = open_file("./data/raw_data/2016-17_pbp.csv")
search(data)

data = open_file("./data/raw_data/2017-18_pbp.csv")
search(data)
