# Mobile One

Author: [roerohan](https://github.com/roerohan)

# Requirements

- strings

# Source

```
The one true mobile app.
```

- [mobile_one.apk](./mobile_one.apk)

# Exploitation

Download the apk. Run strings on it. That's it.

```bash
$ strings mobile_one.apk | grep flag
##flag{strings_grep_and_more_strings}
flag
```

The flag is:
```
flag{strings_grep_and_more_strings}
```