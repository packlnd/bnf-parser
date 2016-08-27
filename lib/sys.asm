; sys.asm - system call wrapper procedures

section .text

; make the library API externally visible
global mywrite
global myexit

mywrite:
    mov eax, 0x4              ; sys call write code
    int 0x80                  ; make system call
    ret

myexit:
    mov eax, 0x1              ; sys call exit code
    int 0x80                  ; make system call
