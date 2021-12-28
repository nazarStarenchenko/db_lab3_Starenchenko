select * from players;
create table players_copy as select * from players; 
select * from players_copy;


DO $$
DECLARE
    player_id     		players_copy.player_id%TYPE;
    player_name   		players_copy.player_name%TYPE;
	player_family_name  players_copy.player_family_name%TYPE;
	team_id				players_copy.team_id%TYPE;
	college_id			players_copy.college_id%TYPE;
	player_height		players_copy.player_height%TYPE;
	player_weight		players_copy.player_weight%TYPE;
	country				players_copy.country%TYPE;
	age					players_copy.age%TYPE;
	pts					players_copy.pts%TYPE;
	reb					players_copy.reb%TYPE;	
	ast					players_copy.ast%TYPE;
BEGIN
    player_id := 50;
    player_name := 'Player_name #';
	player_family_name := 'Family_name #';
	team_id := 0;
	college_id := 0;
	player_height := 180;
	player_weight := 150;
	ast := 0;
	age := 20;
	pts := 20;
	reb := 8;
	country := 'Ukraine';
	
	
    FOR counter IN 1..10
        LOOP
            INSERT INTO players_copy(player_id, 
									 player_name, 
									 player_family_name,
									 team_id,
									 college_id,
									 player_height,
									 player_weight,
									 ast,
									 reb,
									 age,
									 pts,
									 country)
            VALUES (player_id + counter, 
					player_name || counter, 
					player_family_name || counter,
				    team_id,
				   	college_id,
				    player_height + counter,
				    player_weight + counter*5,
				    ast + counter*2,
				    reb + counter,
				   	age + counter,
				    pts - counter,
				    country);
        END LOOP;
END;
$$