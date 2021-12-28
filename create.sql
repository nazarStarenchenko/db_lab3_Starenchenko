
CREATE TABLE Players
(
player_id			int			UNIQUE NOT NULL,
player_name			char(50)	NOT NULL,
player_family_name	char(50)	NOT NULL,
team_id				int			NOT NULL,
college_id 			int			NOT NULL,
age					int			NOT NULL,	
player_height 		int			NOT NULL,
player_weight 		int			NOT NULL,
country				char(50)	NOT NULL,
pts					int			NOT NULL,
reb					int			NOT NULL,
ast					int			NOT NULL


);

CREATE TABLE Teams
(
  team_id       int           UNIQUE NOT NULL,
  team_name     char(50)      UNIQUE NOT NULL
);

CREATE TABLE Colleges
(
  college_id       int           UNIQUE NOT NULL,
  college_name     char(50)      UNIQUE NOT NULL
);

ALTER TABLE Players ADD CONSTRAINT PK_Players PRIMARY KEY (player_id);
ALTER TABLE Teams ADD CONSTRAINT PK_Teams PRIMARY KEY (team_id);
ALTER TABLE Colleges ADD CONSTRAINT PK_Colleges PRIMARY KEY (college_id);

ALTER TABLE Players ADD CONSTRAINT FK_Players_Teams FOREIGN KEY (team_id) REFERENCES Teams (team_id);
ALTER TABLE Players ADD CONSTRAINT FK_Players_Colleges  FOREIGN KEY (college_id) REFERENCES Colleges (college_id);