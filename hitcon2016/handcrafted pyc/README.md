# Handcrafted pyc

238 Teams solved.

# Description

Can your brain be a Python VM? (Please use Python 2.7)

[crackme.py](crackme.py_bc552f58fe2709225ca0768c131dd14934a47305)

Hint: None

# Solution

I did not particpate in Hitcon 2016 when it was "live". Instead, I decided I wanted to work some challenges and came across the website and picked on that looked like fun.  So, here's my solution.


The contents of the python (with manual line breaks) is shown below.

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import marshal, zlib, base64

exec(marshal.loads(zlib.decompress(base64.b64decode('eJyNVktv00AQXm/eL0i
giaFA01IO4cIVCUGFBBJwqRAckLhEIQmtRfPwI0QIeio/hRO/hJ/CiStH2M/prj07diGRP43
Hs9+MZ2fWMxbnP6mux+oK9xVMHPFViLdCTB0xkeKDFEFfTIU4E8KZq8dCvB4UlN3hGEsdddX
U9QTLv1eFiGKGM4cKUgsFCNLFH7dFrS9poayFYmIZm1b0gyqxMOwJaU3r6xs9sW1ooakXuRv
+un7Q0sIlLVzOCZq/XtsK2oTSYaZlStogXi1HV0iazoN2CV2HZeXqRQ54TlJRb7FUlKyUatI
Ssdzo+P7UU1Gb1POdMruckepGwk9tIXQTftz2yBaT5JQovWvpSa6poJPuqgao+b9l5Aj/R+m
LQIP4f6Q8Vb3g/5TB/TJxWGdZr9EQrmn99fwKtTvAZGU7wzS7GNpZpDm2JgCrr8wrmPoo54U
qGampFIeS9ojXjc4E2yI06bq/4DRoUAc0nVnng4k6p7Ks0+j/S8z9V+NZ5dhmrJUM/y7JTJe
RtnJ2TSYJvsFq3CQt/vnfqmQXt5KlpuRcIvDAmhnn2E0t9BJ3SvB/SfLWhuOWNiNVZ+h28g4
wlwUp00w95si43rZ3r6+fUIEdgOZbQAsyFRRvBR6dla8KCzRdslar7WS+a5HFb39peIAmG7u
ZTHVm17Czxju4m6bayz8e7J40DzqM0jr0bmv9PmPvk6y5z57HU8wdTDHeiUJvBMAM4+0CpoA
Z4BPgJeAYEAHmgAUgAHiAj4AVAGORtwd4AVgC3gEmgBBwCPgMWANOAQ8AbwBHgHuAp4D3gLu
ARwoGmNUizF/j4yDC5BWM1kNvvlxFA8xikRrBxHIUhutFMBlgQoshhPphGAXe/OggKqqb2ci
bxwuEXjUcQjccxi5eFRL1fDSbKrUhy2CMb2aLyepkegDWsBwPlrVC0/kLHmeCBQ=='))))
```

So, it's a string where we need to base64 decode, zlib uncompress, and unmarshal it.  When we do so, we get a python code object. Well, we
could just run it and see what happens.

import marshal, zlib, base64, dis

```python

r = zlib.decompress(base64.b64decode('eJyNVktv00AQXm/eL0igiaFA01IO4cIVCUGFBBJwqRAckLhEIQmtRfPwI0QIeio/hRO/hJ/CiStH2M/prj07diGRP43Hs9+MZ2fWMxbnP6mux+oK9xVMHPFViLdCTB0xkeKDFEFfTIU4E8KZq8dCvB4UlN3hGEsdddXU9QTLv1eFiGKGM4cKUgsFCNLFH7dFrS9poayFYmIZm1b0gyqxMOwJaU3r6xs9sW1ooakXuRv+un7Q0sIlLVzOCZq/XtsK2oTSYaZlStogXi1HV0iazoN2CV2HZeXqRQ54TlJRb7FUlKyUatISsdzo+P7UU1Gb1POdMruckepGwk9tIXQTftz2yBaT5JQovWvpSa6poJPuqgao+b9l5Aj/R+mLQIP4f6Q8Vb3g/5TB/TJxWGdZr9EQrmn99fwKtTvAZGU7wzS7GNpZpDm2JgCrr8wrmPoo54UqGampFIeS9ojXjc4E2yI06bq/4DRoUAc0nVnng4k6p7Ks0+j/S8z9V+NZ5dhmrJUM/y7JTJeRtnJ2TSYJvsFq3CQt/vnfqmQXt5KlpuRcIvDAmhnn2E0t9BJ3SvB/SfLWhuOWNiNVZ+h28g4wlwUp00w95si43rZ3r6+fUIEdgOZbQAsyFRRvBR6dla8KCzRdslar7WS+a5HFb39peIAmG7uZTHVm17Czxju4m6bayz8e7J40DzqM0jr0bmv9PmPvk6y5z57HU8wdTDHeiUJvBMAM4+0CpoAZ4BPgJeAYEAHmgAUgAHiAj4AVAGORtwd4AVgC3gEmgBBwCPgMWANOAQ8AbwBHgHuAp4D3gLuARwoGmNUizF/j4yDC5BWM1kNvvlxFA8xikRrBxHIUhutFMBlgQoshhPphGAXe/OggKqqb2cibxwuEXjUcQjccxi5eFRL1fDSbKrUhy2CMb2aLyepkegDWsBwPlrVC0/kLHmeCBQ=='))

r = marshal.loads(r)

print dir()
exec(r)
print dir()
```

```python
['__builtins__', '__doc__', '__file__', '__name__', '__package__', 'base64', 'dis', 'marshal', 'r', 'zlib']
password: Wrong password... Please try again. Do not brute force. =)
['__builtins__', '__doc__', '__file__', '__name__', '__package__', 'base64', 'dis', 'main', 'marshal', 'r', 'zlib']
```

The `dir` statements show the names of variables in the current frame before and after executing the encoded code. A new object has been created called `main`.

```python
>>> main
<function main at 0x10521c848>
```

Fortunately, python has a disassembler:

```python
>>> dis.dis(main)
  1           0 LOAD_GLOBAL              0 (chr)
              3 LOAD_CONST               1 (108)
              6 CALL_FUNCTION            1
              9 LOAD_GLOBAL              0 (chr)
             12 LOAD_CONST               1 (108)
             15 CALL_FUNCTION            1
             18 LOAD_GLOBAL              0 (chr)
             21 LOAD_CONST               2 (97)
             24 CALL_FUNCTION            1
             27 LOAD_GLOBAL              0 (chr)
             30 LOAD_CONST               3 (67)
             33 CALL_FUNCTION            1
             36 ROT_TWO
			 
			...
        >>  744 LOAD_GLOBAL              1 (raw_input)
            747 JUMP_ABSOLUTE         1480
        >>  750 LOAD_FAST                0 (password)
            753 COMPARE_OP               2 (==)
			...
           2211 BINARY_ADD          
        >> 2212 PRINT_ITEM          
           2213 PRINT_NEWLINE       
           2214 LOAD_CONST               0 (None)
           2217 RETURN_VALUE        
```

Hmm, 977 lines of python virtual machine code. Let's save off some
useful data (you'll see why later).  We'll save off the names of globals
used by `main`, its constants and the names of variables used local to
main.

```python
with open('vars.marshal', 'wb') as f:
    marshal.dump(main.__code__.co_names, f)
    marshal.dump(main.__code__.co_consts, f)
    marshal.dump(main.__code__.co_varnames, f)
```

In the assembly above, it appears to be comparing two strings (the one we typed and another one stored in the `password` local variable). `password` is built up by main character by character with a several low level operations.

I tried modifying the code object of main, but python marks that part of the structure readonly. Ok, well, how complicated is the disassemly:

```
$ cut -c 16-38 disassembly | sort | uniq -c | sort -rn
 205  LOAD_CONST
 204  LOAD_GLOBAL
 204  CALL_FUNCTION
 199  BINARY_ADD
 145  ROT_TWO
   6  JUMP_ABSOLUTE
   1  STORE_FAST
   1  RETURN_VALUE
   1  PRINT_NEWLINE
   1  PRINT_ITEM
   1  POP_TOP
   1  POP_JUMP_IF_FALSE
   1  NOP
   1  LOAD_FAST
   1  COMPARE_OP
```
   
16 operations? Why not just write our own interpreter? What we really want to do is to print the arguments to the `COMPARE_OP` call and provide that as raw input and see what happens.  My implementation of the virtual machine is
(here)[vm.py]
and it's mostly based on the documentation for
(Python's `dis` module)[https://docs.python.org/2/library/dis.html].

It reads the textual representation of the disassembled python and executes it (including control flow like jumps, etc.).  All in all it's pretty easy to follow. Note how `co_names`, `co_consts`, and `co_varnames` are used from the saved unmarshaling.

(This shell script)[x.sh] runs though the solution.

This was a thoroughly fun challenge and I am very much appreciate the HITCON 2016 web site remaining up.
