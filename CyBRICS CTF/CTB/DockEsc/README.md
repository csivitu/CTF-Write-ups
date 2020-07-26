# DockEsc

Author: [roerohan](https://github.com/roerohan) and [thebongy](https://github.com/thebongy)

# Requirements

- Docker

# Source

```
Hey, check it out: i've just shoulder-surfed CyBRICS organizers and got the command they run to deploy new service on every connection!

Looks like they are planning to give you the flag if you Escape the Docker!

Alas, my camera broke the JPEG at the very sweet spot. I wonder if we can somehow get that --detach-keys value

ssh dockesc@109.233.57.94
Password: B9Go9eGS
```

# Exploitation

When you connect to the server using `ssh`, you land in a docker container executing `sleep infinity`. The image provided in the challenge shows a part of the `--detach-keys` which is `ctrl-p,p,i,c,t,u`. Now when you start typing something on the container, you notice that it doesnt show anything on your terminal if you keep writing the correct thing. As soon as it's incorrect, it displays it. So, our plan was to try all combinations using a script, but we figured we could try manually for a bit, and we got lucky and got third blood `:)`.

When you type `ctrl-ppictureisworthathousandwords`, it escapes the container and you get the flag.

The flag is:

```
cybrics{y0u_h4V3_k1LL3D_the_INFINITY}
```
