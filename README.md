# PortSwigger Web Security Academy - Labs
Hands-on solutions and custom scripts from PortSwigger Web Security Academy.
All work is performed on intentionally vulnerable lab environments provided by PortSwigger.


## Structure

``` 
PortSwigger Labs/
├── SQLi/
│   ├── blind_sqli.py
│   ├── blind_sqli_error_based.py
│   ├── blind_sqli_time_delays.py
│   └── README.md
├── XSS/
│   └── README.md
└── README.md
```

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

| 14 | Exploiting XSS to bypass CSRF defenses | XSS | ✅ Solved |
| 15 | Reflected XSS into HTML context with nothing encoded | XSS | ✅ Solved |
| 16 | Stored XSS into HTML context with nothing encoded | XSS | ✅ Solved |
| 17 | DOM XSS in document.write sink using source location.search | XSS | ✅ Solved |
| 18 | DOM XSS in innerHTML sink using source location.search | XSS | ✅ Solved |
| 19 | DOM XSS in jQuery anchor href attribute sink using location.search source | XSS | ✅ Solved |
| 20 | DOM XSS in jQuery selector sink using a hashchange event | XSS | ✅ Solved |
| 21 | Reflected XSS into attribute with angle brackets HTML-encoded | XSS | ✅ Solved |
| 22 | Stored XSS into anchor href attribute with double quotes HTML-encoded | XSS | ✅ Solved |


## Custom Scripts

| Script | Description |
|---|---|
| `SQLi/blind_sqli.py` | Automates boolean-based blind SQLi — finds password length and extracts credentials character by character |
| `SQLi/blind_sqli_error_based.py` | Automates error-based blind SQLi — finds password length and extracts credentials character by character |
| `SQLi/blind_sqli_time_delays.py` | Automates time-based blind SQLi using pg_sleep() and binary search |


## Disclaimer

All labs are performed on intentionally vulnerable environments provided by PortSwigger Web Security Academy.
This repository is for educational purposes only. Never use these techniques on systems without explicit permission.



## Author

[BishalKumarBaishya](https://github.com/Bishal-Kumar-Baishya) — B.Tech CSE | Cybersecurity