import psycopg2
import pandas as pd

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

with con:
    cur = con.cursor()
    cur.execute(query1)
    df = pd.DataFrame(cur)
    df.columns = ["player_id", "player_name", "player_family_name", "team_id", "college_id", "player_height",
			"player_weight", "ast", "reb", "age","pts", "country"]
    df.to_csv("players.csv", index=False)
    print(df.head())


    cur.execute(query2)
    df = pd.DataFrame(cur)
    df.columns = ["college_id", "college_name"]
    df.to_csv("colleges.csv", index=False)
    print(df.head())

    cur.execute(query3)
    df = pd.DataFrame(cur)
    df.columns = ["team_id", "team_name"]
    df.to_csv("teams.csv", index=False)
    print(df.head())