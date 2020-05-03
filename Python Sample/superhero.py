import requests

# Reworked by Reighpuy
# Daftar Superhero : https://github.com/reighpuy/super_hero/blob/master/daftar_super_hero

    # Superhero
    elif cmd.startswith('superhero'):
      try:
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        param1 = sender
        reighpuy.findAndAddContactsByMid(param1) # Bot Mencari MID si pengirim
        res = '╭───「 Superhero 」'
        res += '\n├'
        res += '\n├ Max Number of Hero : 731' # untuk lihat daftar Super hero ada di file daftar_super_hero / https://github.com/reighpuy/super_hero/blob/master/daftar_super_hero.
        res += '\n├ Usage : '
        res += '\n│ • {key}Superhero search (name)'
        res += '\n│ • {key}Superhero num (no)'
        res += '\n│ • {key}Superhero powerstats (no)'
        res += '\n│ • {key}Superhero bio (no)'
        res += '\n│ • {key}Superhero appearance (no)'
        res += '\n│ • {key}Superhero work (no)'
        res += '\n│ • {key}Superhero connections (no)'
        res += '\n│ • {key}Superhero image (no)'
        res += '\n├'
        res += '\n╰───「 Reighpuy 」'
        if cmd == 'superhero':
            reighpuy.sendReplyMessage(msg_id, to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif texttl.startswith('num '): # mencari dengan nomor urut sesuai daftar yang ada di https://github.com/reighpuy/super_hero/blob/master/daftar_super_hero.
            texts = textt[4:]
            textsl = texts.lower()
            r = requests.get("https://www.superheroapi.com/api.php/api_key_mu/{}".format(texts))
            data = r.text
            data = json.loads(data)
            reighpuy.sendReplyMessage(msg_id, to, data["name"])
        elif texttl.startswith('powerstats '): # melihat info Power superhero dengan ID sesuai urut nya.
            texts = textt[11:]
            textsl = texts.lower()
            r = requests.get("https://www.superheroapi.com/api.php/api_key_mu/{}/powerstats".format(texts))
            data = r.text
            data = json.loads(data)
            isi = "ID : {}".format(str(data["id"]))
            isi += "\nName : {}".format(str(data["name"]))
            isi += "\nIntelligence : {}".format(str(data["intelligence"]))
            isi += "\nStrength : {}".format(str(data["strength"]))
            isi += "\nSpeed : {}".format(str(data["speed"]))
            isi += "\nDurability : {}".format(str(data["durability"]))
            isi += "\nPower : {}".format(str(data["power"]))
            isi += "\nCombat : {}".format(str(data["combat"]))
            reighpuy.sendReplyMessage(msg_id, to, isi)
        elif texttl.startswith('bio '): # melihat Bio superhero dengan ID sesuai urut nya.
            texts = textt[4:]
            textsl = texts.lower()
            r = requests.get("https://www.superheroapi.com/api.php/api_key_mu/{}/biography".format(texts))
            data = r.text
            data = json.loads(data)
            isi = "ID : {}".format(str(data["id"]))
            isi += "\nName : {}".format(str(data["name"]))
            isi += "\nFull name : {}".format(str(data["full-name"]))
            isi += "\nAlter egos : {}".format(str(data["alter-egos"]))
            isi += "\nPlace of birth : {}".format(str(data["place-of-birth"]))
            isi += "\nFirst appearance : {}".format(str(data["first-appearance"]))
            isi += "\nPublisher : {}".format(str(data["publisher"]))
            isi += "\nAlignment : {}".format(str(data["alignment"]))
            reighpuy.sendReplyMessage(msg_id, to, isi)
        elif texttl.startswith('appearance '): # Melihat Appearance superhero dengan ID sesuai urut nya.
            texts = textt[11:]
            textsl = texts.lower()
            r = requests.get("https://www.superheroapi.com/api.php/api_key_mu/{}/appearance".format(texts))
            data = r.text
            data = json.loads(data)
            isi = "ID : {}".format(str(data["id"]))
            isi += "\nName : {}".format(str(data["name"]))
            isi += "\nGender : {}".format(str(data["gender"]))
            isi += "\nRace : {}".format(str(data["race"]))
            isi += "\nHeight : {}".format(str(data["height"][1]))
            isi += "\nWeight : {}".format(str(data["weight"][1]))
            isi += "\nEye-color : {}".format(str(data["eye-color"]))
            isi += "\nHair-color : {}".format(str(data["hair-color"]))
            reighpuy.sendReplyMessage(msg_id, to, isi)
        elif texttl.startswith('work '): # Melihat info Work superhero dengan ID sesuai urut nya.
            texts = textt[5:]
            textsl = texts.lower()
            r = requests.get("https://www.superheroapi.com/api.php/api_key_mu/{}/work".format(texts))
            data = r.text
            data = json.loads(data)
            isi = "ID : {}".format(str(data["id"]))
            isi += "\nName : {}".format(str(data["name"]))
            isi += "\nOccupation : {}".format(str(data["occupation"]))
            isi += "\nBase : {}".format(str(data["base"]))
            reighpuy.sendReplyMessage(msg_id, to, isi)
        elif texttl.startswith('connections '): # Melihat Connections superhero dengan ID sesuai urut nya.
            texts = textt[12:]
            textsl = texts.lower()
            r = requests.get("https://www.superheroapi.com/api.php/api_key_mu/{}/connections".format(texts))
            data = r.text
            data = json.loads(data)
            isi = "ID : {}".format(str(data["id"]))
            isi += "\nName : {}".format(str(data["name"]))
            isi += "\nGroup affiliation : {}".format(str(data["group-affiliation"]))
            isi += "\nRelatives : {}".format(str(data["relatives"]))
            reighpuy.sendReplyMessage(msg_id, to, isi)
        elif texttl.startswith('image '): # Mengirim Gambar superhero dengan ID sesuai urut nya.
            texts = textt[6:]
            textsl = texts.lower()
            r = requests.get("https://www.superheroapi.com/api.php/api_key_mu/{}/image".format(texts))
            data = r.text
            data = json.loads(data)
            reighpuy.sendImageWithURL(to, data["url"])
        elif texttl.startswith("search "): # Melihat Info superhero dengan Nama Superhero sesuai urut nya.
            texts = textt[7:]
            textsl = texts.lower()
            r = requests.get("https://www.superheroapi.com/api.php/api_key_mu/search/{}".format(texts))
            data = r.text
            data = json.loads(data)
            isi = "╭───[ Superhero Info ]"
            isi += "\n├"
            isi += "\n├ Nama : {}".format(data["results-for"])
            isi += "\n├ ID : {}".format(data["results"][0]["id"])
            isi += "\n├"
            isi += "\n├ -> Power stats : "
            isi += "\n├ Intelligence : {}".format(data["results"][0]["powerstats"]["intelligence"])
            isi += "\n├ Strength : {}".format(data["results"][0]["powerstats"]["strength"])
            isi += "\n├ Speed : {}".format(data["results"][0]["powerstats"]["speed"])
            isi += "\n├ Durability : {}".format(data["results"][0]["powerstats"]["durability"])
            isi += "\n├ Power : {}".format(data["results"][0]["powerstats"]["power"])
            isi += "\n├ Combat : {}".format(data["results"][0]["powerstats"]["combat"])
            isi += "\n├"
            isi += "\n├ -> Biography : "
            isi += "\n├ Full Name : {}".format(data["results"][0]["biography"]["full-name"])
            isi += "\n├ Alter egos : {}".format(data["results"][0]["biography"]["alter-egos"])
            isi += "\n├ Place of-birth : {}".format(data["results"][0]["biography"]["place-of-birth"])
            isi += "\n├ First appearance : {}".format(data["results"][0]["biography"]["first-appearance"])
            isi += "\n├ Publisher : {}".format(data["results"][0]["biography"]["publisher"])
            isi += "\n├ Alignment : {}".format(data["results"][0]["biography"]["alignment"])
            isi += "\n├"
            isi += "\n├ -> Appearance : "
            isi += "\n├ Gender : {}".format(data["results"][0]["appearance"]["gender"])
            isi += "\n├ Race : {}".format(data["results"][0]["appearance"]["race"])
            isi += "\n├ Height : {}".format(data["results"][0]["appearance"]["height"][1])
            isi += "\n├ Weight : {}".format(data["results"][0]["appearance"]["weight"][1])
            isi += "\n├ Eye color : {}".format(data["results"][0]["appearance"]["eye-color"])
            isi += "\n├ Hair color : {}".format(data["results"][0]["appearance"]["hair-color"])
            isi += "\n├"
            isi += "\n├ -> Work : "
            isi += "\n├ Occupation : {}".format(data["results"][0]["work"]["occupation"])
            isi += "\n├ Base : {}".format(data["results"][0]["work"]["base"])
            isi += "\n├"
            isi += "\n├ -> Connections : "
            isi += "\n├ Group affiliation : {}".format(data["results"][0]["connections"]["group-affiliation"])
            #isi += "\n├ Relatives : {}".format(data["results"][0]["connections"]["relatives"])
            isi += "\n├"
            isi += "\n╰───[ Reighpuy ]"
            reighpuy.sendReplyMessage(msg_id,to, isi)
      except:
          reighpuy.sendReplyMessage(msg_id,to, "# Gagal memuat perintah, Superehero {} Tidak ditemukan.".format(texts))