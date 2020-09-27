# Flag of Life

Author: [roerohan](https://github.com/roerohan)

## Source

```
Help our adventurer in attaining the Flag of Life by defeating the Demon Guard Flageon.


nc flagoflife.darkarmy.xyz 7001
```

## Expliot

Upon connection, you get:

```sh
$ nc flagoflife.darkarmy.xyz 7001

'Demon Guard Flageon: Who dares to disturb my slumber?
...
A human?
what is your name human?

You: 1337

Demon Guard Flageon: Listen close, 1337.
        To pass through you must give me a key of certain shape and size.
        I do not expect mere mortals to pass this test and win the Flag of Life.
        So here is a hint: the shape of the key is a square.
        But I will not tell you the size.
        You have 3 tries!


        | How lucky! Look in your backpack. You have a square-key-making device.
        | huh... weird thing to carry around if you ask me.
        | Anyways.
        | The problem is the device needs the edge length as input to make the key...
```

And it asks you to input `edge length`.

```
Input edge length: 5

*mechanical whirring*
...
*pop*

Demon Guard Flageon: The size of your key is off by 25 sq cm.
        You have 2 more attempts left
```

Whatever edge lenght you input, it says that the size is off by the square of your input.

Also, we find that the program stores edge length in a variable of type `integer` since it overflows on inputs greater than 4 bytes in size.

Now the motive is clear, we have to pass a number as input so that it's square overflows exactly to give 0. We know that the size of `int` is `2^32 - 1`. So, `2^32` is going to overflow to become `0`. Therefore, we must pass `2^16` as input, which is `65536`.

```sh
Input edge length: 65536

*mechanical whirring*
...
*pop*

Demon Guard Flageon: Congratulation! You have completed this task.
        The Flag of Life is now your's

                ===============================================
                | darkCTF{-2147483648_c0m3s_aft3r_2147483647} |
                ===============================================
```

The flag is:

```
darkCTF{-2147483648_c0m3s_aft3r_2147483647}
```