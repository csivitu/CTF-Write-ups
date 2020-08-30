# Secret Array

Author: [roerohan](https://github.com/roerohan)

# Requirements

- Python

# Source

```
Randomness is a power ! You don't have a chance to face it.

nc twistwislittlestar.fword.wtf 4445

Author: Semah BA
```

# Exploitation

The exploit is based on the Mersene Twister vulnerability, as the name suggests. For that, we need 624 consecutive primes.

```py
from pwn import remote
  
r = remote('twistwislittlestar.fword.wtf', 4445)

arr = list(map(lambda x: x.split(': ')[1], list(filter(lambda x: 'Random Number is' in x, r.recvuntil('Your Prediction For the next one : ').decode().split('\n')))))
print(arr)

for _ in range(624):
    r.sendline('1')

    arr.append(r.recvuntil('Your Prediction For the next one : ').decode().split('was : ')[1].split('\n')[0])
    print('running...')

arr += [str(i) for i in range(20)]

open('./data.txt','w').write('\n'.join(arr))
r.interactive()
```

In this, we have 627 consecutive random numbers followed by 1-20. Pass this `data.txt` to the following code (in stdin). It will predict the correct values for 1-20. You could enter them manually from here (since it's just 20 numbers).

```py
#!/usr/bin/env python
#
# Mersenne Twister predictor
#
# Feed this program the output of any 32-bit MT19937 Mersenne Twister and
# after seeing 624 values it will correctly predict the rest.
#
# The values may come from any point in the sequence -- the program does not
# need to see the first 624 values, just *any* 624 consecutive values.  The
# seed used is also irrelevant, and it will work even if the generator was
# seeded from /dev/random or any other high quality source.
#
# The values should be in decimal, one per line, on standard input.
#
# The program expects the actual unsigned 32 bit integer values taken directly
# from the output of the Mersenne Twister.  It won't work if they've been
# scaled or otherwise modified, such as by using modulo or
# std::uniform_int_distribution to alter the distribution/range.  In principle
# it would be possible to cope with such a scenario if you knew the exact
# parameters used by such an algorithm, but this program does not have any
# such knowledge.
#
# For more information, refer to the original 1998 paper:
#
#  "Mersenne Twister: A 623-dimensionally equidistributed uniform pseudorandom
#   number generator", Makoto Matsumoto, Takuji Nishimura, 1998
#
#   http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.215.1141
#
# This code is not written with speed or efficiency in mind, but to follow
# as closely as possible to the terminology and naming in the paper.
#
# License: CC0 http://creativecommons.org/publicdomain/zero/1.0/

from __future__ import print_function
import sys
import collections

class Params:
    # clearly a mathematician and not a programmer came up with these names
    # because a dozen single-letter names would ordinarily be insane
    w = 32              # word size
    n = 624             # degree of recursion
    m = 397             # middle term
    r = 31              # separation point of one word
    a = 0x9908b0df      # bottom row of matrix A
    u = 11              # tempering shift
    s = 7               # tempering shift
    t = 15              # tempering shift
    l = 18              # tempering shift
    b = 0x9d2c5680      # tempering mask
    c = 0xefc60000      # tempering mask

def undo_xor_rshift(x, shift):
    ''' reverses the operation x ^= (x >> shift) '''
    result = x
    for shift_amount in range(shift, Params.w, shift):
        result ^= (x >> shift_amount)
    return result

def undo_xor_lshiftmask(x, shift, mask):
    ''' reverses the operation x ^= ((x << shift) & mask) '''
    window = (1 << shift) - 1
    for _ in range(Params.w // shift):
        x ^= (((window & x) << shift) & mask)
        window <<= shift
    return x

def temper(x):
    ''' tempers the value to improve k-distribution properties '''
    x ^= (x >> Params.u)
    x ^= ((x << Params.s) & Params.b)
    x ^= ((x << Params.t) & Params.c)
    x ^= (x >> Params.l)
    return x

def untemper(x):
    ''' reverses the tempering operation '''
    x = undo_xor_rshift(x, Params.l)
    x = undo_xor_lshiftmask(x, Params.t, Params.c)
    x = undo_xor_lshiftmask(x, Params.s, Params.b)
    x = undo_xor_rshift(x, Params.u)
    return x

def upper(x):
    ''' return the upper (w - r) bits of x '''
    return x & ((1 << Params.w) - (1 << Params.r))

def lower(x):
    ''' return the lower r bits of x '''
    return x & ((1 << Params.r) - 1)

def timesA(x):
    ''' performs the equivalent of x*A '''
    if x & 1:
        return (x >> 1) ^ Params.a
    else:
        return (x >> 1)

seen = collections.deque(maxlen=Params.n)

print('waiting for {} previous inputs'.format(Params.n))
for _ in range(Params.n):
    val = untemper(int(sys.stdin.readline()))
    seen.append(val)

num_correct = num_incorrect = 0
print('ready to predict')

while True:
    # The recurrence relation is:
    #
    #     x[k + n] = x[k + m] ^ timesA(upper(x[k]) | lower(x[k + 1]))
    #
    # Substituting j = k + n gives
    #
    #     x[j] = x[j - n + m] ^ timesA(upper(x[j - n]) | lower(x[j - n + 1]))
    #
    # The 'seen' deque holds the last 'n' seen values, where seen[-1] is the
    # most recently seen, therefore letting j = 0 gives the equation for the
    # next predicted value.

    next_val = seen[-Params.n + Params.m] ^ timesA(
                        upper(seen[-Params.n]) | lower(seen[-Params.n + 1]))
    seen.append(next_val)
    predicted = temper(next_val)

    actual = sys.stdin.readline()
    if not actual:
        print('end of input -- {} predicted correctly, {} failures'.format(
                    num_correct, num_incorrect))
        sys.exit(0)

    actual = int(actual)
    if predicted == actual:
        status = 'CORRECT'
        num_correct += 1
    else:
        status = 'FAIL'
        num_incorrect += 1

    print('predicted {} got {} -- {}'.format(predicted, actual, status))
```

Here's what you get as output (in this case, varies everytime):

```bash
$ cat data.txt | python3 mer_twis.py
waiting for 624 previous inputs
ready to predict
predicted 2630305257 got 2630305257 -- CORRECT
predicted 2597663602 got 2597663602 -- CORRECT
predicted 1795123759 got 1795123759 -- CORRECT
predicted 306338802 got 0 -- FAIL
predicted 2955851394 got 1 -- FAIL
predicted 1106083444 got 2 -- FAIL
predicted 1852587916 got 3 -- FAIL
predicted 259036002 got 4 -- FAIL
predicted 4098119175 got 5 -- FAIL
predicted 1412275791 got 6 -- FAIL
predicted 545371933 got 7 -- FAIL
predicted 2098379118 got 8 -- FAIL
predicted 2550571293 got 9 -- FAIL
predicted 2691429539 got 10 -- FAIL
predicted 470431618 got 11 -- FAIL
predicted 1731687872 got 12 -- FAIL
predicted 499518855 got 13 -- FAIL
predicted 1368988182 got 14 -- FAIL
predicted 767634446 got 15 -- FAIL
predicted 1065878028 got 16 -- FAIL
predicted 1428656079 got 17 -- FAIL
predicted 3030198656 got 18 -- FAIL
predicted 1804758619 got 19 -- FAIL
end of input -- 3 predicted correctly, 20 failures
```

Now send the actual values to the netcat server and obtain the flag.
<br />

The flag is:

```
FwordCTF{R4nd0m_isnT_R4nd0m_4ft3r_4LL_!_Everyhthing_is_predict4bl3_1f_y0u_kn0w_wh4t_Y0u_d01nGGGG}
```