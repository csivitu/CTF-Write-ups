# Rescue Mission

Author: [roerohan](https://github.com/roerohan)

# Requirements

- Python

# Source

```
Oh no! The flag has been lost in the most disconcerting places! Can you save the flag??

Connect here:
nc jh2i.com 50013
```

# Exploitation

You can probably do solve this task without scripting anything. 

```bash
$ nc jh2i.com 50013

Connecting...
PowerShell 7.0.2
Copyright (c) Microsoft Corporation. All rights reserved.

https://aka.ms/powershell
Type 'help' to get help.

PS /c_drive>
```

Upon connecting, you find yourself in a powershell terminal. You can find the folders in the current directory using `dir`.

```
PS /c_drive> dir
dir


    Directory: /c_drive

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d----          07/29/2020    01:52                stuck_in
```

`cd` into `stuck_in/the_ocean`, you see a `flag.png`.

```
PS /c_drive/stuck_in/the_ocean> dir
dir


    Directory: /c_drive/stuck_in/the_ocean

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-----          07/25/2020    01:57           2197 flag.png

```

You can now convert this to base64 and copy the image to your machine, where you decrypt it with base64.

```powershell
PS /c_drive/stuck_in/the_ocean> [Convert]::ToBase64String([IO.File]::ReadAllBytes("stuck_in/the_ocean/flag.png"))
[Convert]::ToBase64String([IO.File]::ReadAllBytes("stuck_in/the_ocean/flag.png"))

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
```

Store this in a file called `flag.txt`. Decrypt it with base64 and store it in `flag.png`. 

```bash
$ cat flag.txt | base64 -d > flag.png
```

Open `flag.png` and get the flag.
<br />

The flag is:

```
flag{thanks_you_saved_me}
```
