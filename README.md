# PortSwigger Web Security Academy - Labs
Hands-on solutions and custom scripts from PortSwigger Web Security Academy.
All work is performed on intentionally vulnerable lab environments provided by PortSwigger.


## Structure

``` 
PortSwigger Labs/
├── SQLi/
│   ├── blind_sqli.py
│   ├── blind_sqli_error_based.py
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


## Custom Scripts

| Script | Description |
|---|---|
| `SQLi/blind_sqli.py` | Automates boolean-based blind SQLi — finds password length and extracts credentials character by character |
| `SQLi/blind_sqli_error_based.py` | Automates error-based blind SQLi — finds password length and extracts credentials character by character |


## Disclaimer

All labs are performed on intentionally vulnerable environments provided by PortSwigger Web Security Academy.
This repository is for educational purposes only. Never use these techniques on systems without explicit permission.


## Author

[BishalKumarBaishya](https://github.com/Bishal-Kumar-Baishya) — B.Tech CSE | Cybersecurity