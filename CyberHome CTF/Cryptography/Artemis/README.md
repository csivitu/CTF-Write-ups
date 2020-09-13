# Artemis

Author: [roerohan](https://github.com/roerohan)

This is another `file` challenge.

# Requirements

- Linux `file` command.
- HTML

# Source

- [Artemis](./Artemis)

# Exploitation

When you run `file` on the `Artemis` file, you see it's a `rar` file.

```
$ file Artemis 
Artemis: RAR archive data, v5
```

Now, when you extract this compressed file, you get a folder `artemis_fichiers` and a file [`artemis.htm`](./artemis.htm). When you analyze that file, you may find:

```html
valign="center"><img src="artemis_fichiers/C.GIF" alt="c" width="31"><img src="artemis_fichiers/B.GIF" alt="b" width="37"><img src="artemis_fichiers/R.GIF" alt="r" width="20"><img src="artemis_fichiers/H.GIF" alt="h" width="31"><img src="artemis_fichiers/SPACE.GIF" alt="space" width="19"><img src="artemis_fichiers/T.GIF" alt="t" width="28"><img src="artemis_fichiers/H.GIF" alt="h" width="31"><img src="artemis_fichiers/SPACE.GIF" alt="space" width="19"><img src="artemis_fichiers/A.GIF" alt="a" width="30"><img src="artemis_fichiers/R.GIF" alt="r" width="20"><img src="artemis_fichiers/T.GIF" alt="t" width="28"><img src="artemis_fichiers/M.GIF" alt="m" width="17"><img src="artemis_fichiers/I.GIF" alt="i" width="22"><img src="artemis_fichiers/S.GIF" alt="s" width="34"><img src="artemis_fichiers/SPACE.GIF" 
```

Notice the `alt`s of all the image tag. They spell out the flag. So you can write them down sequencially:
```
c b r h space t h space a r t m i s space f o w l space s r i s e e e e e space b y space o i n space c o l f r space e
```

Now, place the `e`s in the correct places, replace the `space`s with `_`s (underscores), and add `{...}`. The flag is:

```
cbrh{the_artemis_fowl_series_by_eoin_colfer}
```
