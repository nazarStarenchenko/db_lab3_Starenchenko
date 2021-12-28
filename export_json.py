import psycopg2
import pandas as pd
import json


username = 'postgres'
password = '3220'
database = 'test_DB'
host = 'localhost'
port = '5432'

con = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)


query1 = """select player_id, TRIM(player_name), TRIM(player_family_name), team_id, college_id, player_height,
			player_weight, ast, reb, age,pts, TRIM(country) from players;"""

query2 = """select college_id, TRIM(college_name) from colleges;"""
query3 = """select team_id, TRIM(team_name) from teams;"""
json_paths_list = ["json_files/test1.json", "json_files/test2.json","json_files/test3.json"]

with con:
    cur = con.cursor()
    cur.execute(query1)
    df = pd.DataFrame(cur)
    df.columns = ["player_id", "player_name", "player_family_name", "team_id", "college_id", "player_height",
			"player_weight", "ast", "reb", "age","pts", "country"]
    df.to_json(json_paths_list[0], orient="records")
    print(df.head())


    cur.execute(query2)
    df = pd.DataFrame(cur)
    df.columns = ["college_id", "college_name"]
    df.to_json(json_paths_list[1],orient="records")
    print(df.head())

    cur.execute(query3)
    df = pd.DataFrame(cur)
    df.columns = ["team_id", "team_name"]
    df.to_json(json_paths_list[2],orient="records")
    print(df.head())



result = []
for f1 in json_paths_list:
    with open(f1, 'r') as infile:
        result.append(json.load(infile))

print(result)
with open('test.json', 'w') as output_file:
    json.dump(result, output_file)

