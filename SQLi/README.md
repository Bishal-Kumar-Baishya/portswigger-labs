# SQL injection
SQL injection (SQLi) is a technique where attackers insert malicious SQL commands into entry fields, allowing them to manipulate or retrieve data from a backend database without authorization.

## Labs completed

| # | Lab Name | Category | Status |
|---|---|---|---|
| 1 | SQL injection vulnerability in WHERE clause allowing retrieval of hidden data | SQLi | ✅ Solved |
| 2 | SQL injection vulnerability allowing login bypass | SQLi | ✅ Solved |
| 3 | SQL injection UNION attack, determining the number of columns | SQLi | ✅ Solved |
| 4 | SQL injection UNION attack, finding a column containing text | SQLi | ✅ Solved |
| 5 | SQL injection UNION attack, retrieving data from other tables | SQLi | ✅ Solved |
| 6 | Blind SQL injection with conditional responses | SQLi | ✅ Solved |

## Built with
- Python 3
- requests module
- string module

## How to run

1. Install dependencies:
``` 
    pip install requests
```

2. Open the lab in your browser, go to DevTools -> Applications -> Cookies and copy the TrackingId and session cookie values

3. Run the script:
``` 
    python SQLi/blind_sqli.py
```

4. Enter the lab URL (with a category e.g. /filter?category=Gifts), TrackingId, and session ID when prompted


## Disclaimer
This script is for educational use only on legal, intentionally vulnerable 
environments such as PortSwigger Web Security Academy labs.