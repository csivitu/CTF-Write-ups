# Hunt

Author: [roerohan](https://github.com/roerohan)

# Requirements

- Browser Devtools

# Source

- http://109.233.57.94:54040/

# Exploitation

In this challenge, you see a bunch of captcha's floating around on your screen, and the goal is to successfully get 5 captchas. There's many ways to solve this, here's what I did:
<br />

When you see the source, this is the function which creates the captchas and makes them move:

```javascript
function addCaptcha() {
    const captchaBox = document.createElement('div');
    const widgetId = grecaptcha.render(captchaBox, {
        'sitekey' : '6Ld0sCEUAAAAAKu8flcnUdVb67kCEI_HYKSwXGHN',
        'theme' : 'light',
        'callback': 'good',
    });

    captchaBox.className = 'captcha';
    document.body.appendChild(captchaBox);

    count ++;
    updateStatus();

    let dividerA = (Math.random() * 250) + 250;
    let dividerB = (Math.random() * 250) + 250;
    let dividerC = (Math.random() * 25) + 25;

    function loop() {
        const height = window.innerHeight - captchaBox.offsetHeight;
        captchaBox.style.top = Math.sin(Date.now()/dividerA) * (height/2) + (height/2);

        const width = window.innerWidth - captchaBox.offsetWidth;
        captchaBox.style.left = Math.sin(Date.now()/dividerB) * (width/2) + (width/2);

        captchaBox.style.transform = `rotate(${Math.sin(Date.now()/dividerC) * 10}deg)`;

        setTimeout(loop, 1);
    }
    loop();
}
```

Just modify this function using your devtools, remove the part where it runs loop.

```js
function addCaptcha() {
    const captchaBox = document.createElement('div');
    const widgetId = grecaptcha.render(captchaBox, {
        'sitekey' : '6Ld0sCEUAAAAAKu8flcnUdVb67kCEI_HYKSwXGHN',
        'theme' : 'light',
        'callback': 'good',
    });

    captchaBox.className = 'captcha';
    document.body.appendChild(captchaBox);

    count ++;
    updateStatus();
}
```

Now, you can manually add 5 captchas and get them. Just call the function `addCaptcha()` and keep clicking the boxes. When you're done with 5, click on `GET FLAG`, and copy the flag from the screen!

The flag is:

```
cybrics{Th0se_c4p7ch4s_c4n_hunter2_my_hunter2ing_hunter2}
```
