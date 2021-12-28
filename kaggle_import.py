import psycopg2
import pandas as pd

username = 'postgres'
password = '3220'
database = 'test_DB'
host = 'localhost'
port = '5432'

con = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)




#opening team csv file and
#writing it into created erlier a data base tables
df = pd.read_csv("teams.csv")
with con:
    cur = con.cursor()
    cur.execute("DELETE FROM teams;")
    for ind in df.index:    
        query = f'''
INSERT INTO Teams(team_id,
                    team_name)
VALUES ({df['id'][ind]}, '{df['team'][ind]}');

'''
        cur.execute(query)

#opening college csv file and
#writing it into created erlier a data base tables
df = pd.read_csv("colleges.csv")
with con:
    cur = con.cursor()
    cur.execute("DELETE FROM colleges;")
    for ind in df.index:    
        query = f'''
INSERT INTO Colleges(college_id,
                    college_name)
VALUES ({df['id'][ind]}, '{df['college'][ind]}');

'''
        cur.execute(query)



#opening palyers csv file and
#writing it into created erlier a data base tables
df = pd.read_csv("players.csv")
with con:
    cur = con.cursor()
    cur.execute("DELETE FROM players;")
    for ind in df.index:    
        query = f'''
INSERT INTO Players(player_id,
                    player_name,
                    player_family_name,
                    team_id,
                    college_id,
                    age,   
                    player_height,
                    player_weight,
                    country,
                    pts,
                    reb,
                    ast)
VALUES ({df['id'][ind]}, '{df['player_name'][ind]}','{df['player_family_name'][ind]}' ,{df['team_id'][ind]}, {df['college_id'][ind]},
 {df['age'][ind]}, {df['player_height'][ind]}, {df['player_weight'][ind]}, '{df['country'][ind]}', {df['pts'][ind]},
  {df['reb'][ind]}, {df['ast'][ind]});

'''
        cur.execute(query)

