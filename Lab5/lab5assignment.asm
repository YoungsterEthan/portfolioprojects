

.ORIG x3000
START   LEA R0, PROMPT          ;LOAD PROMPT STRING
        PUTS                    ;DISPLAY
        GETC                    ;GET CHARACTER FROM USER
        ADD R4, R0, x0          ;Clear R5
        ADD R5, R5, #15         ;load #-57 ito R w/ 2's comp    
        ADD R5, R5, #15         ; OFFSET 30
        ADD R5, R5, #15         ;OFFSET 45
        ADD R5, R5, #12         ;OFFSET 57
        NOT R5, R5
        ADD R5, R5, x1          ;2S COMP

        ADD R5, R5, R4          ;R5 = INPUT -R5
        BRp ERROR               ;BRANCH POSITIVE: INPUT ASCII HIGHER THAN ASCII '9'
        AND R5, R5, x0          ;CLEAR R5

        ADD R5, R5, #15         ;LOAD #48 UNTO R5 W/2S COMP
        ADD R5, R5, #15
        ADD R5, R5, #15 
        ADD R5, R5, #3      
        NOT R5, R5
        ADD R5, R5, x1 

        ADD R5, R5, R4          ;R5 = INPUT - R5
        BRn ERROR               ;BRANCH NEGATIVE: INPUT HAD ASCII VALUE LOWER THAN ASCII '0'
        ADD R1, R5, x0          ;COPY R5 TO R1:THIS IS THE NUMERIC VALUE OF THE ASCII NUMBER CHAR ENTERED

        LEA R0 NUM              ;LOAD NUM CHARACTERS TO R0
        ADD R3, R5, x0          ;COPY R5 TO R3 FOR CHARACTER DISPLAYING PURPOSES
        ADD R3, R3, x0          ;R3 = 0, SET UP ZERO BRANCHING, INITIALIZE LOOP BEGIN AT ZERO
MIRROR1 BRz DISPM1              ;LOOP LABEL, IF = 0, GO TO DISPLAY
        ADD R0, R0, #2          ;R0 += #2, 11 CHARACTER FOR NUMBERS INCLUDING NULL TERMINATED
        ADD R3, R3, #-1         ;R3 = OFFSET 1, UPDATE VALUE FOR INCREMENT IN LOOP
        BR MIRROR1              ;GO BACK TO MIRROR1 START
DISPM1  PUTS                    ;SHOW FIRST NUMBER ON CONSOLE
        GETC                    ;GET SECOND NUMBER
        ADD R4, R0, x0          ;COPY INPUT TO R4
        AND R5, R5, x0          ;CLEAR R5

        ADD R5, R5, #15         ;LOAD #-57 INTO R5 W/ 2'S COMP
        ADD R5, R5, #15
        ADD R5, R5, #15
        ADD R5, R5, #12
        NOT R5, R5
        ADD R5, R5, x1

        ADD R5, R5, R4      ;R5 = INPUT - R5
        BRn CHKENTER         ;BRANCH NEGATIVE: INPUT HAD ASCII VALUE LOWER THAN ASCII '0', CHECK IF 'ENTER' WAS PRESSED
        ADD R2, R5, x0      ;COPY R5 TO R2: THIS IS THE NUMERIC VALUE OF THE ASCII NUMBER CHAR ENTERED IN THE "ONE'S" PLACE

        LEA R0, NUM         ;LOAD NUM CHARACTERS TO R0
        ADD R3, R5, x0      ;COPY R5 TO R3 FOR CHARACTER DISPLAYING PURPOSES
        ADD R3, R3, X0      ;R3 = 0, SET UP ZERO BRANCHING, INITIALIZE LOOP BEGIN AT ZERO
MIRROR2 BRz DISPM2          ;LOOP LABEL, IF = 0, GO TO DISPLAY
        ADD R0, R0, #2      ;R0 += #2, 11 CHARACTERS FOR NUMBERS INCLUDING NULL TERMINATED
        ADD R3, R3, #-1     ;R3 OFFSET 1, UPDATE VALUE FOR INCREMENT INLOOP
        BR MIRROR2          ;LOOP
DISPM2  PUTS                ;SHOW SECOND NUMBER ON CONSOLE
        BR LOOP1

CHKENTER 
        AND R5, R5, x0     ;clear R5
        ADD  R5, R5, XA     ; LOAD XA INTO R5
        NOT R5, R5
        ADD R5, R5, X1
        ADD R5, R4, R5
        BRnp ERROR
        ADD R2, R1, X0
        ADD R2, R1, X0
        AND R1, R1, X0

LOOP1   ADD R1, R1, X0        ;CHECK VALUE OF TENS PLACE
        BRZ PREPM
        BRN ERROR
        ADD R2, R2, XA
        NOT R1, R1
        ADD R1, R1, X1
        BR LOOP1
PREPM   LEA R0, LF
        PUTS
        AND R0, R0, X0
        ADD R0, R0, XB
        NOT R0, R0
        ADD R0, R0 X1
        ADD R0, R0, R2
        BRNZ GOODIN
        LEA R0, ERRNUM
        PUTS
        LEA R0 LF
        PUTS
        BR START

GOODIN  LEA R0, MONTHS
        AND R3, R3, X0
        ADD R3, R2, X0
LOOP2   BRZ DISPLAY
        ADD R0, R0, #10
        ADD R3, R3, #-1
        BR LOOP2
DISPLAY PUTS
        LEA R0, LF
        PUTS
        BR START
ERROR   LEA R0, LF
        PUTS
        LEA R0, ERRSTR
        PUTS
        HALT

PROMPT  .STRINGZ "Enter a number and ENTER or two numbers 0-11: "
NUM     .STRINGZ "0"
        .STRINGZ "1"
        .STRINGZ "2"
        .STRINGZ "3"
        .STRINGZ "4"
        .STRINGZ "5"
        .STRINGZ "6"
        .STRINGZ "7"
        .STRINGZ "8"
        .STRINGZ "9"

MONTHS  .STRINGZ "January  "
        .STRINGZ "February "
        .STRINGZ "March    "
        .STRINGZ "April    "
        .STRINGZ "May      "
        .STRINGZ "June     "
        .STRINGZ "July     "
        .STRINGZ "August   "
        .STRINGZ "September"
        .STRINGZ "October  "
        .STRINGZ "November "
        .STRINGZ "December "
ERRSTR  .STRINGZ "Input was not an integer. Exiting..."
LF      .STRINGZ "\n"
ERRNUM  .STRINGZ "Invalid index entered. Try again."
.END