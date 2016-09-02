; hello.asm - a "hello, world" program using NASM

section .text

; tell the assembler about library functions are used and the linker will resolve them
extern mywrite
extern myexit

global mystart                ; make the main function externally visible

mystart:                      ; write our string to standard output

; boilerplate to save sacred registers

    push ebp
    mov ebp, esp
    push ebx
    push esi
    push edi

; 1 print "hello, world"

    ; 1a prepare arguments
    push dword mylen           ; message length                           
    push dword mymsg           ; message to write
    push dword 1               ; file descriptor value
    ; 1b make call
    call mywrite
    ; 1c clean up stack
    add esp, 12                ; 3 args * 4 bytes/arg = 12 bytes

; boilerplate to restore sacred registers

    pop edi
    pop esi
    pop ebx
    mov esp, ebp
    pop ebp

; 2 exit the program

    ; 2a prepare arguments
    push dword 0              ; exit code
    ; 2b make call
    call myexit
    ; 2c no need to clean up because no code here would executed...already exited!
    
section .data

  mymsg db "hello, world", 0xa  ; string with a carriage-return
  mylen equ $-mymsg             ; string length in bytes
