import requests
from threading import Thread
import sys
import os

# Scriptin bulunduğu dizini çalışma dizini olarak ayarla
os.chdir(os.path.dirname(os.path.abspath(__file__)))

x = 0
target_url = "https://google.com"
banner = '''
///-----\033[38;2;165;42;42mSUBFINDER\033[0m-----///
v:0.1 beta
c[ ] here is your \033[38;2;165;42;42mcoffee\033[0m
'''



the_wordlist_list = '''
----------------------------
wordlist1     = directory_list_1.0     
wordlist2     = medium wordlist
wordlist3     = directory_list_lowercase_2.3_small
wordlist4     = common 
wordlist5     = apache_user_enum_2.0
wordlist6     = directory_list_2.3_small
wordlist7     = wordpress 
-------wordlists for subdomains------
wordist8
wordist9
wordist10
wordist11
wordist12
wordist13
wordist14           langlist
----------------------------
'''
wordlist1 = []
wordlist2 = []
wordlist3 = []
wordlist4 = []
wordlist5 = []
wordlist6 = []
wordlist7 = []
wordlist8 = []
wordlist9 = []
wordlist10 = []
wordlist11 = []
wordlist12 = []
wordlist13 = []
wordlist14 = ["tr", "eng"]

helptext = '''
version:0.1
subfinder is a scanner for finding subdomains/web paths
usage:

*enter your URL with http://-https://
use https://example.com
'''

optionstext ='''
start: start for web path scan
help: display help page
logs: display logs
console: start findconsole
exit: exit the tool
'''



def internetcheck(timeout=1):
    """Internet baglantisini kontrol eder."""
    try:
        requests.head("http://www.google.com", timeout=timeout)
        return True
    except requests.ConnectionError:
        return False

consolehelptext = '''
console help text
ch/consolehelp: display this page
ic/internetcheck: check the internet connection
wordlists: list all of the wordlists
'''


def consolefunction(console):

        if console == "ch" or console == "consolehelp":
            print(consolehelptext)
        elif console == "exit":
            print("quiting...")
            sys.exit("see you later")
        elif console == "ic" or console =="internetcheck":
            internetcheck()
            if internetcheck():
                print("connected")
            else:
                print("not connected")
        elif console == "wordlists":
            print(the_wordlist_list)
        else:
            print("command not found")
        return console


def send_request(target):
    global x
    try:
        response = requests.get(target)
        if response.status_code == 200:
            print(f"\033[32m[+] host founded:\033[0m {target}")
            x = 1
        else:
            print(f"\033[91m[-] host didnt found:\033[0m {target}")
    except requests.RequestException as e:
        print(f"\033[93m[!] error:\033[0m {e}")
        

def scan_with_wordlist(target_url, wordlist):
    global target
    target = target_url
    threads = []
    for word in wordlist:
        url_to_test = f"{target_url}/{word}"
        thread = Thread(target=send_request, args=(url_to_test,))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()




def scanforsubdomains(target_url, wordlist):
    global target
    if target.startswith("http://"):
        target_url = target[7:] 
        protocol = ("https://")
    elif target.startswith("https://"):
        target_url = target[8:]
        protocol= ("http://")
    else:
        print("wrong usage for targeting a url ")

    threads = []
    for word in wordlist:
        url_to_test = f"{protocol}www.{word}.{target_url}"
        thread = Thread(target=send_request, args=(url_to_test,))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()


# Kodun başlangıcı burada
print(banner)
print(optionstext)
select = input("select a option:").lower()  # Kullanıcı girişini küçük harfe çeviriyoruz


if select in ["start", "s"]:
    internetcheck(timeout=1)
    if internetcheck():
        print("\033[32m internet connection enable\033[0m")

    else:
        print("please check the internet connection")
        sys.exit("quiting...")
    target = input("URL for scanning: ")
    if not target.startswith("http"):
        print("this URL identification didn't exist. Please use http:// or https:// instead of www -- example: https://examplewebsite.org")
    else:
        print(f"the target is {target}")
        print("Ready for scanning")
        print("%0 complated")
        send_request(target)
        if x == 1:
            print("host is up")
            print(the_wordlist_list)
            
            sellectWordlist = input("sellect which wordlist do you want to use:"  )
            print("preparing for domain path search")
            theloglist = (target + "host is up" + "sellected wordlist is:" + sellectWordlist )
            writelogs = str(theloglist)
            print(writelogs)
            with open('logs.txt', 'a') as dosya:
                dosya.write(writelogs)
            if sellectWordlist == "wordlist1" or sellectWordlist == "1":
                with open('directory_list_1.0.txt', 'r', encoding='utf-8') as dosya:
                    icerik_listesi = dosya.readlines()
                    wordlist1 = icerik_listesi
                scan_with_wordlist(target,wordlist1)
                print("domain path scan complated")
            elif sellectWordlist == "wordlist2" or sellectWordlist == "2":
                with open('wordlist2text.txt', 'r', encoding='utf-8') as dosya:
                    icerik_listesi = dosya.readlines()
                    wordlist2 = icerik_listesi
                scan_with_wordlist(target,wordlist2)
                print("scaned for domain path")
            elif sellectWordlist == "wordlist3" or sellectWordlist == "3":
                with open('directory_list_1.0.txt', 'r', encoding='utf-8') as dosya:
                    icerik_listesi = dosya.readlines()
                    wordlist3 = icerik_listesi
                scan_with_wordlist(target,wordlist3)
                print("domain path scan complated")
            elif sellectWordlist == "wordlist4" or sellectWordlist == "4":
                with open('common.txt', 'r', encoding='utf-8') as dosya:
                    icerik_listesi = dosya.readlines()
                    wordlist4 = icerik_listesi
                scan_with_wordlist(target,wordlist4)
                print("domain path scan complated")
            elif sellectWordlist == "wordlist5" or sellectWordlist == "5":
                with open('apache_user_enum_2.0.txt', 'r', encoding='utf-8') as dosya:
                    icerik_listesi = dosya.readlines()
                    wordlist7 = icerik_listesi
                    scan_with_wordlist(target,wordlist5)
                    print("domain path scan complated")
                print("domain path scan complated")
            elif sellectWordlist == "wordlist6" or sellectWordlist == "6":
                with open('directory_list_2.3_small.txt', 'r', encoding='utf-8') as dosya:
                    icerik_listesi = dosya.readlines()
                    wordlist7 = icerik_listesi
                    scan_with_wordlist(target,wordlist6)
                    print("domain path scan complated")
            elif sellectWordlist == "wordlist7" or sellectWordlist == "7":
                with open('wordpress.txt', 'r', encoding='utf-8') as dosya:
                    icerik_listesi = dosya.readlines()
                    wordlist7 = icerik_listesi
                    scan_with_wordlist(target,wordlist7)
                print("domain path scan complated")
            else:
                print("there is no list like that. I will use your words as a list.")
                scan_with_wordlist(target,sellectWordlist)
            
            subscanselect = input("do you want to make subdomain scan?(this wont be quick) (y/n) ")
            if subscanselect == "y" or subscanselect == "Y":
                print(the_wordlist_list)
                sellectWordlist2 = input("sellect which wordlist do you want to use:"  )
                if sellectWordlist2 == "8" or sellectWordlist2 == "wordlist8":
                    scanforsubdomains(target_url, wordlist8)
                elif sellectWordlist2 == "9" or sellectWordlist2 == "wordlist9":
                    scanforsubdomains(target_url, wordlist9)
                elif sellectWordlist2 == "10" or sellectWordlist2 == "wordlist10":
                    scanforsubdomains(target_url, wordlist10)
                elif sellectWordlist2 == "11" or sellectWordlist2 == "wordlist11":
                    scanforsubdomains(target_url, wordlist11)
                elif sellectWordlist2 == "12" or sellectWordlist2 == "wordlist12":
                    scanforsubdomains(target_url, wordlist12)
                elif sellectWordlist2 == "13" or sellectWordlist2 == "wordlist13":
                    scanforsubdomains(target_url, wordlist13)
                elif sellectWordlist2 == "14" or sellectWordlist2 == "wordlist14":
                    scanforsubdomains(target_url, wordlist14)
                else:
                    print("no such dictionary founded")
        else:
            print("scan complated")
            print("host is down. If it is realy up probably wrong url")
            print("%100 complated")
        

elif select in ["help", "h"]:
    print(helptext)
elif select in ["exit", "e", "quit", "q"]:
    print("Have a great day pentester")
    print("exiting...")
elif select in ["logs", "l"]:
    print("here is your logs:")
elif select in ["console", "c", "subconsole", "conssol"]:
    print("starting console")
    consoledisplay = '''
---Subfinder console---
subconsole v:0.1
ch or consolehelp for console help
'''
    print(consoledisplay)
    while True:
            console = input("subconsole>>> ")
            consolefunction(console)
else:
    print("invalid parameter. Please change the parameter")