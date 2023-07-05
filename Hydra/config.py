import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
    
if os.path.exists("Internal"):
    load_dotenv("Internal")

aiohttpsession = aiohttp.ClientSession()
admins = {}
que = {}

API_ID = int(getenv("API_ID", "1020199"))
API_HASH = getenv("API_HASH", "3672885f650c19ef18d53548bb641d5f")
BOT_TOKEN = getenv("BOT_TOKEN", "6379441643:AAEk8B1U7a3Ut7LXQQCWH0rcXwlH7_sFX88")
STRING_SESSION = getenv("STRING_SESSION", "BQCVtcu0xaEGYHlkT9GRybq-L08sewIpO9TnbTkHvpza1B-tjLz6U_MSq_a-zRIwgq5dhXI4bYxPEl4mXfGIhyduWK8P2XeoIOnfwSZwV-rrgTm9Ur_fjRJDeK9c9Sf0tfBkaJ9BJCfOOe_ZNJSOdJS8Hbchwja44kk5smmvo0OBdgBmEfQPKJcaIGlvWE2qhQr3ibggAlSUszKxiqKTgkBOiwtXXv0qxRr3fES5xG5HWJBNZ1xiT1-15S9LRHa_im6Bib_Y0smxm7Y5X9kBF3SCsLPpDpSCTuMYR1TASVgxzlepapsWMtYyxBdMF5o4Y-xnwySP6NLrVQLunne6849LAAAAAWlI6v8A")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", ". ! /").split())
MONGO_DB_URL = getenv("MONGO_DB_URL", "mongodb+srv://EXONTESTMONGO:EXONTESTMONGO@cluster0.bviw7ic.mongodb.net/?retryWrites=true&w=majority")
OWNER_ID = list(map(int, getenv("OWNER_ID", "5715764478").split()))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001849819947"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5715764478 5348193047").split()))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/Otazuki004/Hypdra-V7.50")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
                       
