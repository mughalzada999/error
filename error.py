# Coding=utf-8
#Coding by Lukman-xd
#Note : jangan di ubah lagi! nanti error, script udah enak
###----------[ IMPORT MODULE AND INGREDIENT ]---------- ###
import os, sys, re, time, requests, datetime, calendar, random, bs4, subprocess, uuid, json, threading,platform,string
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser
from datetime import date,datetime
from time import sleep
ses = requests.Session()
device = platform.platform()

###----------[ IMPORT RICH AND INGREDIENT ]---------- ###
from rich.panel import Panel
from rich.tree import Tree
from rich import print as prints
from rich.console import Console
from rich.table import Table
from rich.columns import Columns
from rich import pretty
console = Console()

###----------[ USER AGENT ]---------- ###
ugen2=[]
ugen=[]
princp=[]

###----------[ APPEND AND MORE ]---------- ###
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
pwpluss,pwnya=[],[]

###----------[ COLOR FOR PRINT ]---------- ###
p = '\x1b[1;97m' # PUTIH
m = '\x1b[1;91m' # MERAH
h = '\x1b[1;92m' # HIJAU
k = '\x1b[1;93m' # KUNING
b = '\x1b[1;94m' # BIRU
u = '\x1b[1;95m' # UNGU
o = '\x1b[1;96m' # BIRU MUDA
n = '\x1b[0m'	# WARNA MATI
xy = random.choice([m,k,h,u,o,n])

###----------[ COLOR FOR RICH ]---------- ###
Z = "[#000000]" # HITAM
M = "[#FF0000]" # MERAH
H = "[#00FF00]" # HIJAU
K = "[#FFFF00]" # KUNING
B = "[#00C8FF]" # BIRU
U = "[#AF00FF]" # UNGU
N = "[#FF00FF]" # PINK
O = "[#00FFFF]" # BIRU MUDA
P = "[#FFFFFF]" # PUTIH
J = "[#FF8F00]" # JINGGA
A = "[#AAAAAA]" # ABU-ABU
XY = random.choice([M,K,H,B,O,N])
balmond = P+"["+O+"*"+P+"]"

###----------[ GLOBAL NAME ]---------- ###
ses = requests.Session()
reset = "[/]"
IP = requests.get("http://ip-api.com/json/").json()["query"]
negara = requests.get("http://ip-api.com/json/").json()["country"]
zxc = "fbkey"
ff = "lukmanul"
xv = "hakim"

###----------[ CHECK THEME COLOR ]---------- ###
try:
	color_rich = open("data/color_rich.txt","r").read()
except FileNotFoundError:
	color_rich = "[#FFFFFF]"
try:
	color_table = open("data/color_table.txt","r").read()
except FileNotFoundError:
	color_table = "#FFFFFF"

###----------[ CLEAR TERMINAL ]---------- ###
def clear_screen():
	if "linux" in sys.platform.lower():
		try:os.system("clear")
		except:pass
	elif "win" in sys.platform.lower():
		try:os.system("cls")
		except:pass
	else:
		try:os.system("clear")
		except:pass

###----------[ BULAN]---------- ###
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.now().day
bln = dic[(str(datetime.now().month))]
thn = datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
sekarang = str(tgl)+"-"+str(bln)+"-"+str(thn)

###----------[ LOADING ]---------- ###
def loading():

    animation = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
    for i in range(50):
        time.sleep(0.1)
        sys.stdout.write(f"\r{p}[{o}•{p}] {h}proses...{n} " + animation[i % len(animation)] +"\x1b[0m ")
        sys.stdout.flush()
    print("")		

###----------[ JALAN ]---------- ###
def jalan(keliling):
	for mau in keliling + '\n':
		sys.stdout.write(mau)
		sys.stdout.flush();sleep(0.03)

###----------[ DELETE LOGIN ]---------- ###
def delete():
	try:os.remove("data/token.txt")
	except:pass
	try:os.remove("data/cookie.txt")
	except:pass

###----------[ LOGO ]---------- ###
def logo():
	clear_screen()
	prints(Panel(f'''{U}  ____             _         ______                   {M}______ ____{U}
 |  _ \           | |       |  ____|                 {M}|  ____|  _ \ {U}
 | |_) |_ __ _   _| |_ ___  | |__ ___  _ __ ___ ___  {M}| |__  | |_) | {U}
 |  _ <| '__| | | | __/ _ \ |  __/ _ \| '__/ __/ _ \ {M}|  __| |  _ < {U}
 | |_) | |  | |_| | ||  __/ | | | (_) | | | (_|  __/ {M}| |    | |_) | {U}
 |____/|_|   \__,_|\__\___| |_|  \___/|_|  \___\___| {M}|_|    |____/ {M} 
\t\t\tBY LUKMAN-XD @2022''',width=71,style=f"{color_table}"))

###----------[ NEW ]---------- ###
def new():
	try:
		name = open('data/pengguna.txt','r').read()
	except FileNotFoundError:
		logo()
		prints(Panel(f"{P}[{H}•{P}] Sepertinya anda pengguna baru tols Brute FB \n[{H}•{P}] Nama kamu belom terdaftar sebagai pengguna tols Brute FB\n[{H}•{P}] Siapa nama kamu ?",width=71,title=f"{M}•{K}•{H}• INFO {H}•{K}•{M}•",padding=(0,2),style=f"{color_table}"))
		nama = input(f'{p}[{o}?{p}] Nama : {n}')
		if nama in['']:
			prints(Panel(f"\t{P}[{M}>{P}] Isi dengan nama jangan kosong cok [{M}<{P}]",width=71,style=f"{color_table}"))
			exit()
		else:
			open('data/pengguna.txt','w').write(nama)
			logo()
			prints(Panel(f'{P}[{O}*{P}] Selamat datang {nama} di tols Brute FB.\n[{O}*{P}] Kalau ada bug atau error silahkan hubungi admin\n[{O}*{P}] Gunakan tols ini dengan bijak :)\n[{O}*{P}] Tekan enter untuk lanjut',width=71,title=f"{M}•{K}•{H}• INFO {H}•{K}•{M}•",padding=(0,2),style=f"{color_table}"))
			input('');login()
	login()

###----------[ LOGIN]---------- ###
def login():
	try:
		token = open("data/token.txt","r").read()
		cok = open("data/cookie.txt","r").read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=name,id,birthday&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			sy4 = json.loads(sy.text)['birthday']
			menu(sy2,sy3,sy4)
		except KeyError:
			login_lagi334()
		except requests.exceptions.ConnectionError:
			prints(Panel(f"""{P2}[{O2}*{P2}]. Koneksi internet leg cok. Silahkan cek dan cobal lagi""",width=71,style=f"{color_table}"));exit()
	except IOError:
		login_lagi334()
		
def login_lagi334():
	name = open('data/pengguna.txt','r').read()
	try:
		logo()
		prints(Panel(f'''\t{P}[{H}•{P}] masukkan cookie facebook anda [{H}•{P}]''',width=71,style=f"{color_table}"))
		cookie = input(f"{p}[{o}?{p}]. cookie fb : {h}")
		data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookie}) 
		find_token = re.search("(EAAG\w+)", data.text)
		ken=open("data/token.txt", "w").write(find_token.group(1))
		cok=open("data/cookie.txt", "w").write(cookie)
		print('')
		loading()
		prints(Panel(f'{P}[{H}✓{P}] Selamat {H}{name} {P}cookie punya kamu valid!\n[{M}>{P}] Gunakan dengan bijak yah tols nya',width=71,style=f"{color_table}"))
		print(f'{p}[{m}!{p}] Jalankan ulang perintahnya dengan ketik python 17.py')
		exit()
	except Exception as e:
		os.system("rm -f data/token.txt data/cookie.txt")
		print(f"{P}[{M}×{P}]. Login checkpoint {N}");exit()
		
new()
