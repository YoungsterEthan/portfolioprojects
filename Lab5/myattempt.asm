;MONTHS ARRAY

.ORIG x3000

START   LEA R0, PROMPT          ;Load prompt int R0
        PUTS                    ;Display
        GETC                    ;Read character
        ADD R2, R0, x0          ;Copy  input into Register 2
        ;offset digit in 10s place
        ADD R2, R2, #-16        ;offset at 16
        ADD R2, R2, #-16        ;offset at 32
        ADD R2, R2, #-16        ;offset at 48
        OUT                     ;ouput to user
        ADD R4, R2, #-1         ;R4 = OFFSET 1 from R2, THIS IS DONE FOR INPUT VALIDATION 0-1 for 10s place
        BRp ERROR               ;GO TO ERROR IF INPUT IS LARGER THAN 1
        
        AND R4, R4, x0          ;Clearing R4 to use Again

        GETC                    ;reading 1s place
        ADD R3, R0, x0          ;Copy into register 3
        ;offset digit in 1s place
        ADD R3, R3, #-16        ;offset at 16
        ADD R3, R3, #-16        ;offset at 32
        ADD R3, R3, #-16        ;offset at 48
        OUT                     ;ouput to user
        ADD R4, R3, #-9         ;R4 = OFFSET 9 from R3, THIS IS DONE FOR INPUT VALIDATION 0-9 for 1s place
        BRp ERROR               ;GO TO ERROR IF INPUT IS LARGER THAN 9

        AND R4, R4, x0      ;Clearing R4 to use Again

        LD R4, TEN          ; used to multiply by 10
        AND R1, R1, x0      ;initialize register 1
        
BY10    ADD R1, R1, R2          ;Multiplying by 10
        ADD R4, R4, #-1
        BRP BY10


        AND R5, R5, x0          ;clearing register 5
        ADD R5, R1, R3          ; R1 + R3 = R5
        
        AND R0, R0, x0          ;clear register 0

        LEA R0, MONTHS        ;LOAD DAYS to R0
        ADD R5, R5, x0      ;R5 = 0, SET UP ZERO BRANCHING, INITIALIZE LOOP BEGIN AT ZERO

LOOP    BRz DISPLAY         ;LOOP LABELm IF - 0, GO TO DISPLAY
        ADD R0, R0, #11     ;R0 = #10, 10 CHARACTERS FOR DAYS INCLUDING NULL TERMINATED
        ADD R5, R5, #-1     ;R# = OFFSET 1, UPDATE ALUE FOR INCREMENT IN LOOP
        BR LOOP             ;GO TO LOOP

ERROR   LEA R0, ERMS        ;LOAD ERMS WHEN INPUT IS INVALID
        PUTS                ;SHOWS "INVALID INPUT"
        HALT                ;IF INPUT IS WRONG, STOP THE PROGRAM

DISPLAY PUTS                ;SHOW ON SCREEN
        LEA R0, LF          ;LOAD LF TO R0, LF HOLD DAYS AS STRINGS
        PUTS                ;SHOW ON SCREENHALT
        BR START




PROMPT  .STRINGZ "Enter a number 00 - 11:"
PRP     .STRINGZ "Register is Empty"
TEN     .FILL x000A

ERMS    .STRINGZ "INVALID INPUT"

LF      .STRINGZ "\n"
MONTHS  .STRINGZ " January  "
        .STRINGZ " February "
        .STRINGZ " March    "
        .STRINGZ " April    "
        .STRINGZ " May      "
        .STRINGZ " June     "
        .STRINGZ " July     "
        .STRINGZ " August   "
        .STRINGZ " September"
        .STRINGZ " October  "
        .STRINGZ " November "
        .STRINGZ " December "
.END