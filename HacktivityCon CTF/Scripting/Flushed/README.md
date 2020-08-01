# Flushed

Author: [roerohan](https://github.com/roerohan)

# Requirements

- Python

# Source

```
It is like Rescue Mission all over again! Except this time... the flag was flushed down the toilet!

Connect here:
nc jh2i.com 50015
```

# Exploitation

This challenge is similar to `Rescue Mission`. There's a `flag.png` on the server, but standard out always executes the `toilet` command on linux, hence the output is in the form of some ASCII art.

```bash
$ nc jh2i.com 50015
user@flushed:/home/user$ ls
ls
                                                        
   m""  ""#                                             
 mm#mm    #     mmm    mmmm         mmmm   m mm    mmmm 
   #      #    "   #  #" "#         #" "#  #"  #  #" "# 
   #      #    m"""#  #   #         #   #  #   #  #   # 
   #      "mm  "mm"#  "#m"#    #    ##m#"  #   #  "#m"# 
                       m  #         #              m  # 
                        ""          "               ""  
user@flushed:/home/user$
```

However, `stderr` is not running the `toilet` command. 

```bash
user@flushed:/home/user$ ls 1>&2          
ls 1>&2
flag.png
```

You can convert the flag to base64 using:

```bash
$ nc jh2i.com 50015
user@flushed:/home/user$ cat flag.png | base64 1>&2
cat flag.png | base64 1>&2
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
7/PfAAAAAElFTkSuQmCC
```

Store this base64 string in a file called `flag.txt`. Now decrypt it and store it in `flag.png`.

```bash
$ cat flag.txt | base64 -d > flag.png
```

Open `flag.png` and read the flag.
<br />

The flag is:

```
flag{flushed_down_the_toilet_but_rescued_again}
```