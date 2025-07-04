import requests
from bs4 import BeautifulSoup

def check_sql_injection(url):
    payload = "' OR '1'='1"
    response = requests.get(url + payload)
    return "error" in response.text.lower()  # Simplified check

def check_xss(url):
    payload = "<script>alert('XSS')</script>"
    response = requests.get(url + payload)
    return payload in response.text

def scan_url(url):
    print(f"Scanning {url} for vulnerabilities...")
    sql_injection = check_sql_injection(url)
    xss = check_xss(url)

    if sql_injection:
        print("SQL Injection vulnerability found!")
    else:
        print("No SQL Injection vulnerability found.")

    if xss:
        print("XSS vulnerability found!")
    else:
        print("No XSS vulnerability found.")

if __name__ == "__main__":
    target_url = input("Enter the URL to scan: ")
    scan_url(target_url)
