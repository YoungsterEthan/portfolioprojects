;Class: CIS11
.ORIG x3000
RESTART LEA R0, PROMPT      ;Prompt on console "ENTER NUMBER 0-6"
        PUTS                ;SHOW on console
        GETC                ; read CHARACTER input
        ADD R3, R0, x0      ;copy R0 to R3, R3 = R0
        ADD R3, R3, #-16    ;offset at 16
        ADD R3, R3, #-16    ;offset at 32
        ADD R3, R3, #-16    ;offset at 48
        ADD R4, R3, #-6     ;R4 = OFFSET 6 from R3, THIS IS DONE FOR INPUT VALIDATION 0-6
        BRp ERROR           ;GO TO ERROR IF INPUT IS LARGER THAN 6
        LEA R0, DAYS        ;LOAD DAYS to R0
        ADD R3, R3, x0      ;R3 = 0, SET UP ZERO BRANCHING, INITIALIZE LOOP BEGIN AT ZERO
LOOP    BRz DISPLAY         ;LOOP LABELm IF - 0, GO TO DISPLAY
        ADD R0, R0, #10     ;R0 = #10, 10 CHARACTERS FOR DAYS INCLUDING NULL TERMINATED
        ADD R3, R3, #-1     ;R# = OFFSET 1, UPDATE ALUE FOR INCREMENT IN LOOP
        BR LOOP             ;GO TO LOOP
DISPLAY PUTS                ;SHOW ON SCREEN
        LEA R0, LF          ;LOAD LF TO R0, LF HOLD DAYS AS STRINGS
        PUTS                ;SHOW ON SCREEN
        BR RESTART          ;RELOOP BACK TO PROMPT
ERROR
        LEA R0, ERMS        ;LOAD ERMS WHEN INPUT IS INVALID
        PUTS                ;SHOWS "INVALID INPUT"
        HALT                ;IF INPUT IS WRONG, STOP THE PROGRAM


PROMPT  .STRINGZ "PLEASE ENTER NUMBER 0 - 6: "
DAYS    .STRINGZ "Sunday   "
        .STRINGZ "Monday   "
        .STRINGZ "Tuesday  "
        .STRINGZ "Wednesday"
        .STRINGZ "Thursday "
        .STRINGZ "Friday   "
        .STRINGZ "Saturday  "
ERMS    .STRINGZ "INVALID INPUT"
LF      .FILL x000A
        .END