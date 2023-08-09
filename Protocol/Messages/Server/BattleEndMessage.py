from ByteStream.Writer import Writer
from DataBase.DBManager import DB

class BattleEndMessage(Writer):

    def __init__(self, client, player, type, result, players, db: DB):
        super().__init__(client)
        self.id = 23456
        self.player  = player
        self.type    = type
        self.result  = result
        self.players = players
        self.db = db

    def encode(self):
        self.writeVInt(self.type)
        self.writeVInt(self.result)
        if self.type == 0 and self.result == 0:
        	trophies = 8
        	tokens = 30
        else:
        		trophies = -8
        		tokens = 0
        self.writeVInt(tokens)#z
        self.writeVInt(trophies)#v
        self.writeVInt(0) # Unknown
        self.writeVInt(0) # Doubled Tokens
        self.writeVInt(0) # Double Token Event
        self.writeVInt(0) # Token Doubler Remaining
        self.writeVInt(0) # Championship Lose 
        self.writeVInt(0) # Unknown
        self.writeVInt(0) # Championship Level Passed
        self.writeVInt(0) # Challenge Reward Type (0 = Star Tokens, 1 = Star Tokens)
        self.writeVInt(0) #C hallenge Reward Ammount
        self.writeVInt(0) # Championship Losses Left
        self.writeVInt(0) # Championship Maximun Losses
        self.writeVInt(8) # Coin Shower Event
        self.writeVInt(0) #Underdog (But I Didn't Coded Yet)
        self.writeVInt(50) #Battle Result Type ((-16)-(-1) = Power Play Battle End, 0-15 = Practice and Championship Battle End, 16-31 = Matchmaking Battle End, 32-47 = Friendly Game Battle End, 48-63  = Spectate and Replay Battle End, 64-79 = Championship Battle End)
        self.writeVInt(-64) # Championship Type
        self.writeVInt(0) # Unused Star Token (Beta Brawl Pass Stuff?)

        # Players in Game Array
        self.writeVInt(len(self.players))

        for player in self.players:
            self.brawler  = self.players[player]['Brawler']
            self.skin     = self.players[player]['Skin']
            self.team     = self.players[player]['Team']
            self.username = self.players[player]['Name']

            if self.type == 5:
                self.writeVInt(player) if self.team == 1 else self.writeVInt(2)
            else:
                self.writeVInt(2 if self.team != 1 else 1) if self.type == 2 else self.writeVInt(self.team if self.team != 1 else 2)
                if self.type == 5:
                	self.player.DuoVictories += 1
                	self.db.update_player_account(self.player.token, 'DuoVictories', self.player.DuoVictories)
                
                if self.type == 2:
                	self.player.SoloVictories += 1
                	self.db.update_player_account(self.player.token, 'SoloVictories', self.player.SoloVictories)
                	
                	if self.type == 1:
                		self.player.triVictories += 1
                		self.db.update_player_account(self.player.token, 'triVictories', self.player.triVictories)

            self.writeDataReference(16, self.brawler)if self.brawler != -1 else self.writeVInt(0) # Player Brawler SCID
            self.writeDataReference(29, self.skin)   if self.skin    != -1 else self.writeVInt(0) # Player Skin SCID

            self.writeVInt(0) # Player Trophies
            self.writeVInt(0) # Player Highest Trophies
            self.writeVInt(10)    # Player Power Level

            self.writeBoolean(True)
            self.writeInt(0)
            self.writeInt(1)

            self.writeString(self.username) # Player Name

            self.writeVInt(100)      # Unknown
            self.writeVInt(28000000) # Player Profile Icon ID
            self.writeVInt(43000001) # Player Name Color ID
            self.writeVInt(0)


        # Experience Array
        self.writeVInt(2) # Count
        self.writeVInt(0) # Normal Experience ID
        self.writeVInt(1) # Normal Experience Ammount
        self.writeVInt(8) # Star Player Experience ID
        self.writeVInt(2) # Star Player Experience Ammount

        # Rank Up and Level Up Bonus Array
        self.writeVInt(2) # Count
        self.writeVInt(39) # Milestone CsvID
        self.writeVInt(33) # Milestone Row (row 33 is rank 35)
        self.writeVInt(39) # Milestone CsvID
        self.writeVInt(34) # Milestone Row


        # Trophies and Experience Bars Array
        self.writeVInt(2) # Count
        self.writeVInt(1) # Ranks Milestone ID
        self.writeVInt(0) # Brawler Trophies Bar
        self.writeVInt(0) # Brawler Trophies for Rank
        self.writeVInt(5) # Experience Milestone ID
        self.writeVInt(0) # Total Experience Bar
        self.writeVInt(0) # ???
        
        self.writeVInt(0)  # Unknown
        self.writeBoolean(True)  # Play Again
        self.writeVInt(1) # Count

        for x in range(1):
            self.writeVInt(1)

            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeUInt8(0)

            self.writeDataReference(16, 0)

            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            
            self.player.trp = trophies
            self.player.tokens = tokens
            
            self.player.tokens += tokens
            self.db.update_player_account(self.player.token, 'tokens', self.player.tokens)
            self.player.trophies += trophies
        self.player.high_trophies += trophies
        self.player.brawlers_trophies[str(self.player.home_brawler)] += trophies
        self.player.brawlers_high_trophies[str(self.player.home_brawler)] += trophies
        self.db.update_player_account(self.player.token, 'Trophies',  self.player.trophies)
        self.db.update_player_account(self.player.token, 'HighestTrophies',  self.player.high_trophies)
        self.db.update_player_account(self.player.token, 'BrawlersTrophies',  self.player.brawlers_trophies)
        self.db.update_player_account(self.player.token, 'BrawlersHighestTrophies',  self.player.brawlers_high_trophies)
