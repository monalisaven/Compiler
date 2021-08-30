# TUCALIUC AGNES MONALISA
# IOANNA CHARPANTIDOU

# python cimple.py test.ci : where test.ci out file name
import os
import sys

filename = sys.argv[1]

# OPEN THE CI TEST FILE
try:
    file = open(filename, "r")  # VIA COMMAND LINE ARGUMENT
except IOError:
    print("FILE NOT FOUND")

# INITIALIZATION OF THE CHARACTERS, READ FROM STATE
WHITE_SPACE = 0
LETTER = 1
DIGIT = 2
ADD = 3
SUB = 4
MUL = 5
DIV = 6
LESSER_THAN = 7  # <
GREATER_THAN = 8  # >
EQUAL = 9
COLON = 10
SEMI_COLON = 11
COMMA = 12
RIGHT_BRACKET = 13  # ] BRACKET
LEFT_BRACKET = 14  # [ BRACKET
RIGHT_BRACE = 15  # } BRACE
LEFT_BRACE = 16  # { BRACE
RIGHT_PARENTHESES = 17  # ) RIGHT PARENTHESES
LEFT_PARENTHESES = 18  # ( LEFT PARENTHESES
DOT = 20  #
KAGKELO = 21  # # FOR COMMENT
EOF = 22  # END OF FILE
NEWLINE = 23  # OTHER OR ERROR

# TOKEN_TYPE IS RETURNED WITH STATE
id_TK = 24
constant_TK = 25
plus_TK = 26
sub_TK = 27
multiply_TK = 28
divide_TK = 29
less_than_TK = 30
more_than_TK = 31
equal_TK = 32
different_TK = 33  # <>
assign_TK = 34  # :=
colon_TK = 35
semicolon_TK = 36
comma_TK = 37
left_bracket_TK = 38  # [
right_bracket_TK = 39  # ]
left_parentheses_TK = 40  # (
right_parentheses_TK = 41
left_brace_TK = 42  # {
right_brace_TK = 43  # }
comment_TK = 44  # THE # (THAT REPRESENTS COMMENT) SYMBOL
dot_TK = 45
error_TK = 46
less_equal_TK = 47  # <=
more_equal_TK = 48  # >=
par_mul_TK = 49  # )*

# ERRORS
ERROR_UNKNOWN_SYMBOL = -1
ERROR_COMMENT_SYNTAX = -2
ERROR_NUMLETTER = -3

# STATES
STATE0_START = 0  # START
STATE1_LETTER = 1  # LETTER
STATE2_DIGIT = 2  # DIGIT
STATE3 = 3  # <, <=, <>
STATE4 = 4  # >, >=
STATE5_ASSIGN = 5  # :=
STATE6_COMMENT = 6  # COMMENT
STATE7 = 7

# KEY WORDS TOKEN
program_TK = 60
declare_TK = 61
if_TK = 62
else_TK = 63
while_TK = 64
switchcase_TK = 65
forcase_TK = 66
incase_TK = 67
case_TK = 68
default_TK = 69
not_TK = 70
and_TK = 71
or_TK = 72
function_TK = 73
procedure_TK = 74
call_TK = 75
return_TK = 76
in_TK = 77
inout_TK = 78
input_TK = 79
print_TK = 80

# DICTIONARIES FOR OUR SYMBOLS AND KEY WORDS

key_words = {'program': program_TK, 'declare': declare_TK, 'if': if_TK, 'else': else_TK, 'while': while_TK,
             'switchcase': switchcase_TK, 'forcase': forcase_TK, 'incase': incase_TK, 'case': case_TK,
             'default': default_TK, 'not': not_TK, 'and': and_TK, 'or': or_TK,
             'function': function_TK, 'procedure': procedure_TK, 'call': call_TK, 'return': return_TK,
             'in': in_TK, 'inout': inout_TK, 'input': input_TK, 'print': print_TK}

operators = {'+': ADD, '-': SUB, '*': MUL, '/': DIV, '<>': different_TK, '=': EQUAL, '{': LEFT_BRACE, '}': RIGHT_BRACE,
             '<': LESSER_THAN, '>': GREATER_THAN, ':': COLON, ';': SEMI_COLON, ',': COMMA, '.': DOT, '#': KAGKELO,
             '(': LEFT_PARENTHESES, ')': RIGHT_PARENTHESES, '[': LEFT_BRACKET, ']': RIGHT_BRACKET}

error = {'ERROR_UNKNOWN_SYMBOL': ERROR_UNKNOWN_SYMBOL, 'ERROR_COMMENT_SYNTAX': ERROR_COMMENT_SYNTAX,
         'ERROR_NUMLETTER': ERROR_NUMLETTER}

state_auto = [[0 for x in range(24)] for y in range(7)]

# STARTING FORM SCRATCH AND MOVING THE POINTER
# STATE TO STATE, DEPENDING ON WHAT WE FIND
state_auto[STATE0_START][WHITE_SPACE] = STATE0_START  # FINDS EMPTY SPACE AND STAYS ON THE SAME STATE ,START STATE
state_auto[STATE0_START][LETTER] = STATE1_LETTER  # FINDS LETTER AND GOES TO STATE1
state_auto[STATE0_START][DIGIT] = STATE2_DIGIT  # FINDS DIGIT AND GOES TO STATE2
state_auto[STATE0_START][ADD] = plus_TK
state_auto[STATE0_START][SUB] = sub_TK
state_auto[STATE0_START][MUL] = multiply_TK
state_auto[STATE0_START][DIV] = divide_TK
state_auto[STATE0_START][LESSER_THAN] = STATE3  # WE CHANGE STATE CAUSE MIGHT FOLLOW = OR >
state_auto[STATE0_START][GREATER_THAN] = STATE4  # WE CHANGE STATE CAUSE MIGHT FOLLOW =
state_auto[STATE0_START][EQUAL] = equal_TK
state_auto[STATE0_START][COLON] = STATE5_ASSIGN  # WE CHANGE STATE CAUSE COULD BE FOLLOWED =
state_auto[STATE0_START][SEMI_COLON] = semicolon_TK
state_auto[STATE0_START][COMMA] = comma_TK
state_auto[STATE0_START][RIGHT_BRACKET] = right_bracket_TK  # [
state_auto[STATE0_START][LEFT_BRACKET] = left_bracket_TK  # ]
state_auto[STATE0_START][LEFT_PARENTHESES] = left_parentheses_TK  # (
state_auto[STATE0_START][RIGHT_PARENTHESES] = right_parentheses_TK  # )
state_auto[STATE0_START][LEFT_BRACE] = left_brace_TK  # {
state_auto[STATE0_START][RIGHT_BRACE] = right_brace_TK  # }
state_auto[STATE0_START][KAGKELO] = STATE6_COMMENT  # WE CHANGE STATE FOR THE COMMENT
state_auto[STATE0_START][DOT] = dot_TK
state_auto[STATE0_START][EOF] = error_TK

for i in range(24):  # STRING
    state_auto[STATE1_LETTER][i] = id_TK  # WORD THAT CONTAIN LETTERS OR DIGITS
state_auto[STATE1_LETTER][LETTER] = STATE1_LETTER  # FOR WORD
state_auto[STATE1_LETTER][DIGIT] = STATE1_LETTER  # IF WORD CONTAINS DIGIT

for i in range(24):  # NUMBER
    state_auto[STATE2_DIGIT][i] = constant_TK  # NUMBER
state_auto[STATE2_DIGIT][DIGIT] = STATE2_DIGIT  # ONLY FOR DIGIT

for i in range(24):  # OPERATORS
    state_auto[STATE3][i] = less_than_TK  # LESS,LESS OR EQUAL, DIFFERENT
state_auto[STATE3][EQUAL] = less_equal_TK  # LESS OR EQUAL <=
state_auto[STATE3][GREATER_THAN] = different_TK  # DIFFERENT <>

for i in range(24):  # OPERATORS
    state_auto[STATE4][i] = more_than_TK  # >
state_auto[STATE4][EQUAL] = more_equal_TK  # MORE OT EQUAL >=

for i in range(24):  # ASSIGN
    state_auto[STATE5_ASSIGN][i] = colon_TK  # COLON
state_auto[STATE5_ASSIGN][EQUAL] = assign_TK  # := ASSIGH SYMBOL

for i in range(24):  # COMMENT
    state_auto[STATE6_COMMENT][i] = STATE6_COMMENT  # COMMENT IGNORE EVERYTHING INSIDE THE COMMENT
state_auto[STATE6_COMMENT][KAGKELO] = STATE0_START  # END OF COMMENT #
state_auto[STATE6_COMMENT][NEWLINE] = ERROR_COMMENT_SYNTAX  # THE COMMMENT MUST END WITH # OTHERWISE ERROR

# ------------------------LEX-------------------------------------------------------------------------------#

lineNo = 1  # TO COUNT LINES
tokenString = ""  # TO SAVE OUR VERBAL UNIT
state = None  # OUR TOKEN FOR THE KEYWORDS, OPERATORS, ID
flag = False
char = None  # VARIABLE THAT READS CHARACTERS, SYMBOLS, OPERATORS
column = None  # VARIABLE TO FIND SYMBOL
fun_or_proc = function_TK


# READS NEXT CHAR OR OPERATOR AND CHECKS FOR ERRORS
def readNextSymbol():
    global lineNo, verbal_unit
    if char == ' ' or char == '\t' or char == '\n':
        if char == '\n':
            lineNo = lineNo + 1
            return NEWLINE
        else:
            verbal_unit = STATE0_START
    elif char.isalpha():  # WE CHECK IF THE SYMBOL WE FIND IS A LETTER
        verbal_unit = LETTER
        if state == STATE2_DIGIT:
            print("ERROR %d INVALID SYNTAX AT LINE %d, NUMBER BEFORE LETTER IS NOT ALLOWED" % (ERROR_NUMLETTER, lineNo))
            sys.exit(ERROR_NUMLETTER)
    elif char.isdigit():  # WE CHECK IF THE SYMBOL WE FIND IS A NUMBER
        verbal_unit = DIGIT
    elif char in operators:  # WE CHECK IF THE CHARACTER WE FIND IS IN OPERATOR'S ARRAY
        verbal_unit = operators[char]
    elif char == '':
        flag = True
        verbal_unit = EOF
    else:
        print("ERROR %d UNKNOWN SYMBOL AT LINE : %d" % (
            ERROR_UNKNOWN_SYMBOL, lineNo))  # ERROR IF WE FIND A SYMBOL OUT OF OUR ALPHABET
        sys.exit(ERROR_UNKNOWN_SYMBOL)
    return verbal_unit


# CHECKS IF OUR VERBAL UNIT BELONGS TO OUR KEY WORDS
def isKeyWord(key):
    global verbal_unit
    if key in key_words:
        verbal_unit = key_words[key]
    else:
        verbal_unit = id_TK
    return verbal_unit


# OUR LEX
def lex():
    global state, char, lineNo
    column = 0
    global tokenString
    tokenString = ""
    state = STATE0_START
    while STATE0_START <= state <= STATE6_COMMENT:
        char = file.read(1)  # WE READ ONE BY ONE WORD OR VERBAL UNIT
        if len(tokenString) < 30:  # WE DONT WANT A WORD LONGER THAN 30 CHARACTERS
            tokenString += char
        column = readNextSymbol()  # RETURNS OUR VERBAL UNIT
        state = state_auto[state][column]
        if state == STATE0_START:  # IGNORE WHITE SPACE AND START AGAIN
            col = 0
            tokenString = ""
        if state == ERROR_COMMENT_SYNTAX:  # ERROR IN CASE WE DONT CLOSE THE COMMENT WITH #
            print("ERROR AT LINE %d, WRONG SYNTAX FOR COMMENTS" % lineNo)
            sys.exit(ERROR_COMMENT_SYNTAX)
    if state == id_TK or state == constant_TK or state == less_than_TK or state == more_than_TK or state == colon_TK:
        if not flag:
            index = file.tell() - 1  # SO WE DONT MISS THE READ SYMBOL,BECAUSE WE READ THE NEXT CHAR IN ORDER TO IDENTIFY THE KEY WORD
            file.seek(index, 0)  # POSITION THE CHANGE
            if tokenString[-1] == '\n':  # DECREASE LINE NUMBER IF WE FIND NEWLINE
                lineNo -= 1
            tokenString = tokenString[:-1]
        if state == constant_TK:  # LIMIT FOR HOW BIG OR HOW SMALL CAN BE THE NUMBER
            if tokenString != '':
                number = int(tokenString)
                if -94967295 >= number or number > 94967295:
                    print("THE NUMBER IS OUT OF BOUND AT LINE %d: " % lineNo)
                    sys.exit(error_TK)
    if state == id_TK:  # IF ID BELONGS TO THE KEY WORDS DICTIONARY
        state = isKeyWord(tokenString)
    # print([state, tokenString, lineNo])  # IN CASE YOU WANT TO SEE THE STEPS (WORDS) LEX READS FROM CIMPLE FILE
    # print(tokenString)


# ---------------------------------SYNTAX-------------------------------------------------------#
def program():  # program ID block .
    global name
    lex()
    if state == program_TK:
        lex()
        if state == id_TK:
            name = tokenString  # take the keyword
            lex()
            if state != declare_TK and state != function_TK and state != procedure_TK and state != left_brace_TK:
                print("ERROR AT LINE %d , WRONG SYNTAX AFTER PROGRAM NAME" % lineNo)
                sys.exit(error_TK)
            block(name, 1)
            if state == dot_TK:
                print("THE PROGRAM COMPILES SUCCESSFULLY ")
                lex()
                if state != EOF:
                    with open("test.c") as f:  # WE OPEN THE FILE IN CASE IT IS CREATED FOR FUNCTION/PROCEDURE/CALL
                        content = f.readlines()  # TO DELETE IT CAUSE OUR COMPILER DOESNT CREATE .c FILE IN THIS CASE
                        content = [x.strip() for x in content]
                    f.close()
                    if len(content) < 10:
                        for char in range(4, len(content) - 1):  # checks if labels are linear (L_2,...,L_X)
                            # (sequential 2 in L_2 == 2, 3 in L_3 == 3 etc)
                            if int(content[char][2]) != int(char - 2):  # if not we delete the file
                                os.remove("test.c")
                                print("Warning, dot terminates program if compiles successfully, doesn't read "
                                      "anything further.")
                                sys.exit(0)
                    else:
                        for char in range(4, len(content) - 1):  # checks if labels are linear (L_2,...,L_X)
                            # (sequential 2 in L_2 == 2, 3 in L_3 == 3 etc)
                            if char < 12:
                                if int(content[char][2]) != int(char - 2):  # if not we delete the file
                                    os.remove("test.c")
                                    print("Warning, dot terminates program if compiles successfully, doesn't read "
                                          "anything further.")
                                    sys.exit(0)
                            else:
                                if int(content[char][2] + content[char][3]) != int(
                                        char - 2):  # if not we delete the file
                                    os.remove("test.c")
                                    print("Warning, dot terminates program if compiles successfully, doesn't read "
                                          "anything further.")
                                    sys.exit(0)
                    print("Warning , dot terminates program if compiles successfully, doesn't read anything further.")
                    delete_scope()
                    sys.exit(0)
            else:
                print("ERROR AT LINE %d, PROGRAMME MUST FINISH WITH DOT" % lineNo)
                sys.exit(error_TK)
        else:
            print("ERROR AT LINE %d, INVALID ID NAME FOR THE PROGRAM" % lineNo)
            sys.exit(error_TK)

    else:
        print("ERROR AT LINE %d, KEY WORD 'PROGRAM' WAS NOT FOUND" % lineNo)
        sys.exit(error_TK)


def block(name, kindOfBlock):  # name and kindOfBlock needed to check if it's the main program | procedure | function
    # when kindOfBlock is 1 it's the main program
    # declarations subprograms statements
    new_scope(name)
    if kindOfBlock != 1:
        add_parameters()
    declarations()
    subprograms()
    genquad("begin_block", name, "_", "_")
    writeToFile()  # after every genquad we write it into the .int file

    if kindOfBlock != 1:
        get_firstQuad()

    statements()
    if kindOfBlock == 1:  # it is the main program so end (halt) else continue
        genquad("halt", "_", "_", "_")
        writeToFile()  # after every genquad we write it into the .int file
    else:
        get_frameLen()
    genquad("end_block", name, "_", "_")
    asm_code()
    writeToFile()  # after every genquad we write it into the .int file
    open_cfile()
    write_tableofsymb = open('TableOfSymbols_File.txt', 'w')
    write_table_of_symbols(write_tableofsymb)
    # delete_scope()


def declarations():  # ( declare varlist ; )∗
    while state == declare_TK:
        lex()
        varlist()
        if state == semicolon_TK:
            lex()
        else:
            print("ERROR AT LINE %d, ; EXPECTED AFTER THE DECLARATIONS." % (lineNo - 1))
            sys.exit(error_TK)


def varlist():  # ID ( , ID )∗ | e
    # PARAMETERS FOR THE DECLARATIONS
    if state == id_TK:
        declare_list.append(tokenString)  # list to save the declaration variable(id)
        entity = Record_entity()
        entity.type = 'Variable'
        entity.name = tokenString
        entity.variable.offset = get_offset()
        new_entity(entity)
        lex()
        while state == comma_TK:
            lex()
            if state == id_TK:
                declare_list.append(tokenString)  # save the declaration variables(ids if many)
                entity = Record_entity()
                entity.type = 'Variable'
                entity.name = tokenString
                entity.variable.offset = get_offset()
                new_entity(entity)
                lex()
            else:
                print("ERROR ID FOR THE DECLARATION IS MISSING AT LINE %d" % lineNo)
                sys.exit(error_TK)
    else:
        print("ERROR ID FOR THE DECLARATION IS MISSING AT LINE %d" % lineNo)
        sys.exit(error_TK)


def subprograms():  # ( subprogram )∗
    global fun_or_proc
    while state == function_TK or state == procedure_TK:
        if state == procedure_TK:
            fun_or_proc = procedure_TK
        subprogram(fun_or_proc, name, 1)  # mpainei 0 h 1


def subprogram(var, name, kindofblock):  # function ID ( formalparlist ) block | procedure ID ( formalparlist ) block
    if state == function_TK:
        lex()
        if state == id_TK:
            name = tokenString
            entity = Record_entity()
            entity.type = 'Subprogram'
            entity.name = tokenString
            entity.subProgram.type = 'Function'
            new_entity(entity)
            lex()
            if state == left_parentheses_TK:
                formalparlist(var)
                if state == right_parentheses_TK:
                    lex()
                    if state != left_brace_TK:
                        print("ERROR AT LINE %d, WRONG SYNTAX AFTER RIGHT PARENTHESES" % lineNo)
                        sys.exit(error_TK)
                    block(name, 0)
                else:
                    print("ERROR AT LINE %d, ) EXPECTED" % lineNo)
                    sys.exit(error_TK)
            else:
                print("ERROR AT LINE %d, ( EXPECTED" % lineNo)
                sys.exit(error_TK)
        else:
            print("ERROR AT LINE %d, ID NAME FOR FUNCTION NOT VALID" % lineNo)
            sys.exit(error_TK)
    elif state == procedure_TK:
        lex()
        if state == id_TK:
            name = tokenString
            entity = Record_entity()
            entity.type = 'Subprogram'
            entity.name = tokenString
            entity.subProgram.type = 'Procedure'
            new_entity(entity)
            lex()
            if state == left_parentheses_TK:
                formalparlist(var)
                if state == right_parentheses_TK:
                    lex()
                    block(name, 0)
                else:
                    print("ERROR AT LINE %d, ) EXPECTED" % lineNo)
                    sys.exit(error_TK)
            else:
                print("ERROR AT LINE %d, ( EXPECTED" % lineNo)
                sys.exit(error_TK)
        else:
            print("ERROR AT LINE %d, ID NAME FOR PROCEDURE NOT VALID" % lineNo)
            sys.exit(error_TK)


def formalparlist(var):  # in ID | inout ID | e
    # CHECKS IF THERE ARE COMMAS BETWEEN PARAMETERS IN FUNC AND PROC
    lex()
    if state == right_parentheses_TK:
        return
    formalparitem(var)
    while state == comma_TK:
        lex()
        formalparitem(var)


def formalparitem(var):  # in ID | inout ID
    if var == function_TK:
        if state == in_TK:
            lex()
            if state == id_TK:  # THE ID FOR THE in OR inout
                argument = Record_argument()  # we keep the arguments
                argument.name = tokenString
                argument.parMode = 'CV'
                new_argument(argument)
                lex()
            else:
                print("ERROR AT LINE %d, PARAMETER ID NOT FOUND" % lineNo)
                sys.exit(error_TK)
        else:
            print("ERROR AT LINE %d, FUNCTION NEEDS IN TYPE FOR THE PARAMETER" % lineNo)
            sys.exit(error_TK)
    else:
        if state == inout_TK:
            lex()
            if state == id_TK:  # THE ID FOR THE in OR inout
                argument = Record_argument()  # we keep the arguments
                argument.name = tokenString
                argument.parMode = 'REF'
                new_argument(argument)
                lex()
            else:
                print("ERROR AT LINE %d, PARAMETER ID NOT FOUND" % lineNo)
                sys.exit(error_TK)
        else:
            print("ERROR AT LINE %d, PROCEDURE NEEDS INOUT TYPE FOR THE PARAMETER" % lineNo)
            sys.exit(error_TK)


def statements():  # statement ; | { statement ( ; statement )∗}
    # CHECKS FOR KEY WORD AND GOES TO PROPER FUNCTION
    statement()
    if state == semicolon_TK:
        lex()
    if state == left_brace_TK:
        lex()
        statement()
        if state != semicolon_TK:
            print("ERROR AT LINE %d, ; IS EXPECTED" % lineNo)
            sys.exit(error_TK)
        while state == semicolon_TK:
            lex()
            statement()
        if state == right_brace_TK:
            lex()
        else:
            print("ERROR AT LINE %d , BRACE IS MISSING" % lineNo)
            sys.exit(error_TK)


def statement():  # SYNTAX FUNCTIONS FOR THE KEYWORDS
    if state == id_TK:
        assignState()
        semiError()
    elif state == if_TK:
        ifState()
        semiError()
    elif state == else_TK:
        elseState()
        semiError()
    elif state == while_TK:
        whileState()
        semiError()
    elif state == switchcase_TK:
        switchcaseState()
        semiError()
    elif state == forcase_TK:
        forcaseState()
        semiError()
    elif state == incase_TK:
        incaseState()
        semiError()
    elif state == return_TK:
        returnState()
        semiError()
    elif state == call_TK:
        callState()
        semiError()
    elif state == print_TK:
        printState()
        semiError()
    elif state == input_TK:
        inputState()
        semiError()
    elif state == left_parentheses_TK or state == semicolon_TK:
        print("ERROR AT LINE %d, WRONG SYNTAX AFTER STATEMENT" % lineNo)
        sys.exit(error_TK)
    # return


def semiError():  # IN CASE WE HAVE MULTIPLE STATEMENTS AND SEMICOLON IS MISSING
    if state != semicolon_TK:
        print("ERROR AT LINE %d, ; IS MISSING, NOTE: DO NOT ADD UNNECESSARY PARENTHESIS IN YOUR EXPRESSION" % (
                lineNo - 1))
        sys.exit(error_TK)


# S -> id := E {P1} where {P1} : genQuad(“:=“,E.place,”_”,id)
def assignState():  # ID := expression
    z = tokenString
    lex()
    if state == assign_TK:
        op = tokenString
        E_place = expression()
        genquad(op, E_place, "_", z)
        writeToFile()  # after every genquad we write it into the .int file
    else:
        print("ERROR AT LINE %d ID FOUND SO ASSIGNMENT SIGH := IS EXPECTED" % lineNo)
        sys.exit(error_TK)
    return E_place


# S -> if B then {P1} S1 {P2} TAIL {P3} where TAIL -> else S2 | TAIL -> ε
def ifState():  # if ( condition ) statements elsepart #exw apories des ksana
    if state == if_TK:
        lex()
        if state == left_parentheses_TK:
            isTrue, isFalse = condition()  # returns 2 lists
            if state == right_parentheses_TK:
                lex()
                # expression of {p1}
                backpatch(isTrue, nextquad())  # is list of true
                statements()
                # expression of {p2}
                ifList = makelist(nextquad())
                genquad("jump", "_", "_", "_")
                writeToFile()  # after every genquad we write it into the .int file
                backpatch(isFalse, nextquad())  # is list of false
                elseState()
                # expression of {p3}
                backpatch(ifList, nextquad())
    else:
        print("ERROR AT LINE %d, WRONG SYNTAX FOR IF condition" % lineNo)
        sys.exit(error_TK)
    return isTrue, isFalse


def elseState():  # else statements | e
    if state == else_TK:
        lex()
        statements()


# S -> while {P1} B do {P2} S1 {P3}
def whileState():  # while ( condition ) statements
    lex()
    if state == left_parentheses_TK:
        # expression of {p1}
        Bquad = nextquad()
        whileTrue, whileFalse = condition()
        if state == right_parentheses_TK:
            lex()
            # expression of {p2}
            backpatch(whileTrue, nextquad())
            statements()
            # expression of {p3}
            genquad("jump", "_", "_", Bquad)
            writeToFile()  # after every genquad we write it into the .int file
            backpatch(whileFalse, nextquad())
        else:
            print("ERROR AT LINE %d, ) EXPECTED" % lineNo)
            sys.exit(error_TK)
    else:
        print("ERROR AT LINE %d, ( EXPECTED" % lineNo)
        sys.exit(error_TK)
    return whileTrue, whileFalse


# S -> switch {P1}
# ( (cond): {P2} S1 break {P3} )*
# default: S2 {P4}
def switchcaseState():  # switchcase( case ( condition ) statements )∗ default statements
    lex()
    # expression of {p1}
    exitlist = emptylist()
    p1Quad = nextquad()
    while state == case_TK:
        lex()
        if state == left_parentheses_TK:
            lex()
            cond_true, cond_false = condition()
            # expression of {p2}
            backpatch(cond_true, nextquad())
            if state == right_parentheses_TK:
                lex()
                statements()
                # expression of {p3}
                e = makelist(nextquad())
                genquad("jump", "_", "_", p1Quad)
                p1Quad = nextquad()
                writeToFile()  # after every genquad we write it into the .int file
                mergelist(exitlist, e)
                backpatch(cond_false, nextquad())
                if state == default_TK:
                    lex()
                    statements()
                    # expression of {p4}
                    backpatch(exitlist, nextquad())
            else:
                print("ERROR AT LINE %d, ) IS MISSING" % lineNo)
                sys.exit(error_TK)
        else:
            print("ERROR AT LINE %d, ( IS MISSING" % lineNo)
            sys.exit(error_TK)


# S -> forcase {P1}( when (condition) do {P2}sequence {P3}end do ) *endforcase
# S -> forcase {p1}( case ( condition ){p2} statements {p3})∗ default statements
def forcaseState():  # forcase( case ( condition ) statements )∗ default statements
    # expression of {p1}
    p1Quad = nextquad()
    lex()
    while state == case_TK:
        lex()
        if state == left_parentheses_TK:
            lex()
            # expression of {p2}
            cond_true, cond_false = condition()
            backpatch(cond_true, nextquad())
            if state == right_parentheses_TK:
                lex()
                statements()
                # expression of {p3}
                genquad("jump", "_", "_", p1Quad)
                writeToFile()  # after every genquad we write it into the .int file
                backpatch(cond_false, nextquad())
                if state == default_TK:
                    lex()
                    statements()
                    backpatch(cond_false, nextquad())


# S-> incase ( case ( condition ){p1} statements {p2})∗
def incaseState():  # incase( case ( condition ) statements )∗
    lex()
    while state == case_TK:
        lex()
        if state == left_parentheses_TK:
            lex()
            cond_true, cond_false = condition()
            if state == right_parentheses_TK:
                lex()
                # expression of {p1}
                backpatch(cond_true, nextquad())
                statements()
                # expression of {p2}
                backpatch(cond_false, nextquad())
            else:
                print("ERROR AT LINE %d, ) EXPECTED" % lineNo)
                sys.exit(error_TK)
        else:
            print("ERROR AT LINE %d, ( EXPECTED" % lineNo)
            sys.exit(error_TK)


# S -> return (E) {P1} where {P1}: genquad(“retv”,E.place,”_”,”_”)
def returnState():  # return( expression )
    lex()
    if state == left_parentheses_TK:
        lex()
        if state == constant_TK:
            E_place = tokenString
            genquad("retv", E_place, "_", "_")
            writeToFile()  # after every genquad we write it into the .int file
            lex()
        else:
            # expression of {p1}
            E_place = expression()
            genquad("retv", E_place, "_", "_")
            writeToFile()  # after every genquad we write it into the .int file
        if state == right_parentheses_TK:
            lex()
        else:
            print("ERROR AT LINE %d, ) EXPECTED" % lineNo)
            sys.exit(error_TK)
    else:
        print("ERROR AT LINE %d, ( EXPECTED" % lineNo)
        sys.exit(error_TK)
    return E_place


def callState():  # call ID( actualparlist )
    lex()
    # name = tokenString check later
    if state == id_TK:
        name = tokenString
        lex()
        if state == left_parentheses_TK:
            actualparlist(name)
            if state == right_parentheses_TK:
                lex()
                w = newtemp()
                # -----------------------
                # create entity for the table of symbols
                entity = Record_entity()
                entity.type = 'Temp'
                entity.name = w
                entity.tempVar.offset = get_offset()
                new_entity(entity)
                # ---------------------
                genquad("par", w, "RET", "_")
                writeToFile()  # after every genquad we write it into the .int file
                genquad("call", "_", "_", name)
                writeToFile()  # after every genquad we write it into the .int file
                tempres = w
            else:
                genquad("call", "_", "_", name)
                writeToFile()  # after every genquad we write it into the .int file
                print("ERROR AT LINE %d, ) EXPECTED" % lineNo)
                sys.exit(error_TK)
        else:
            print("ERROR AT LINE %d, ( EXPECTED" % lineNo)
            sys.exit(error_TK)
    else:
        print("ERROR AT LINE %d, ID EXPECTED" % lineNo)
        sys.exit(error_TK)


def actualparlist(name):  # actualparitem ( , actualparitem )∗ |e
    lex()
    actualparitem()
    while state == comma_TK:
        lex()
        actualparitem()


def actualparitem():  # in expression | inout ID
    if state == in_TK:
        a = expression()
        genquad("par", a, "CV", "_")
        writeToFile()  # after every genquad we write it into the .int file
    elif state == inout_TK:
        lex()
        if state == id_TK:
            b = tokenString
            lex()
            genquad("par", b, "REF", "_")
            writeToFile()  # after every genquad we write it into the .int file
        else:
            print("ERROR AT LINE %d, ID EXPECTED" % lineNo)
            sys.exit(error_TK)
    elif state == id_TK:
        print("ERROR AT LINE %d, PARAMETER NAME IS MISSING" % lineNo)
        sys.exit(error_TK)


# S -> print (E) {P2} where {P2}: genquad(“out”,E.place,”_”,”_”)
def printState():  # print( expression )
    lex()
    if state == left_parentheses_TK:
        lex()
        if state == constant_TK:
            E_place = tokenString
            genquad('out', E_place, '_', '_')
            writeToFile()  # after every genquad we write it into the .int file
            lex()
        else:
            # expression of {p2}
            E_place = expression()
            genquad('out', E_place, '_', '_')
            writeToFile()  # after every genquad we write it into the .int file
        if state == right_parentheses_TK:
            lex()
        else:
            print("ERROR AT LINE %d, ) EXPECTED" % lineNo)
            sys.exit(error_TK)
    else:
        print("ERROR AT LINE %d, ( EXPECTED" % lineNo)
        sys.exit(error_TK)


# S->input(id) {P1} where {P1}: genquad(“inp”,id.place,”_”,”_”)
def inputState():  # input( ID )
    lex()
    if state == left_parentheses_TK:
        lex()
        if state == id_TK:
            id_place = tokenString
            lex()
            # expression of {p1}
            genquad("inp", id_place, "_", "_")
            writeToFile()  # after every genquad we write it into the .int file
            if state == right_parentheses_TK:
                lex()
            else:
                print("ERROR AT LINE %d, ) EXPECTED" % lineNo)
                sys.exit(error_TK)
        else:
            print("ERROR AT LINE %d, ID EXPECTED" % lineNo)
            sys.exit(error_TK)
    else:
        print("ERROR AT LINE %d, ( EXPECTED" % lineNo)
        sys.exit(error_TK)


# B -> Q1 {P1} ( or {P2} Q2 {P3})*
def condition():  # boolterm ( or boolterm )∗
    B_true = []
    B_false = []
    Q = boolterm()
    # expression of p1
    B_true = Q[0]
    B_false = Q[1]
    while state == or_TK:
        lex()
        # expression of p2
        backpatch(B_false, nextquad())
        Q = boolterm()
        # expression of p3
        B_true = mergelist(B_true, Q[0])
        B_false = Q[1]
    return B_true, B_false


# Q-> R1{P1} (and {P2} R2 {P3})*
def boolterm():  # boolfactor ( and boolfactor )∗
    Q_true = []
    Q_false = []
    # expression of p1
    R1 = boolfactor()
    # transfer quads from list R1 to list Q
    Q_true = R1[0]
    Q_false = R1[1]
    while state == and_TK:
        lex()
        # expression of p2
        backpatch(Q_true, nextquad())  # fills as many quads as possible
        R2 = boolfactor()
        # expression of p3
        Q_false = mergelist(Q_false, R2[1])  # merging the quads that cant be filled
        Q_true = R2[0]  # contains the right logical expression
    return Q_true, Q_false


# R -> E1 relop E2 {P1} creates a non filled quad and inserts it
# in the list of non filled quads for relop (true or false)
def boolfactor():  # not [ condition ] | [ condition ] | expression REL_OP expression
    R_true = []
    R_false = []
    relop = ""
    E1 = ""
    E2 = ""
    if state == not_TK:
        lex()
        if state == left_bracket_TK:
            lex()
            B = condition()
            if state == right_bracket_TK:
                lex()
                # expression of {p1}
                R_true = B[1]
                R_false = B[0]
            else:
                print("ERROR AT LINE %d, [ EXPECTED" % lineNo)
                sys.exit(error_TK)
        else:
            print("ERROR AT LINE %d, ] EXPECTED" % lineNo)
            sys.exit(error_TK)
    elif state == left_bracket_TK:
        lex()
        C = condition()
        if state == right_bracket_TK:
            lex()
            R_true = C[0]
            R_false = C[1]
        else:
            print("ERROR AT LINE %d, ] EXPECTED" % lineNo)
            sys.exit(error_TK)
    else:
        E1 = expression()
        relop = tokenString
        if state == equal_TK or state == less_than_TK or state == more_than_TK or state == less_equal_TK or state == more_equal_TK or state == different_TK:
            E2 = expression()
            # expression of {p1}
            R_true = makelist(nextquad())
            genquad(relop, E1, E2, "_")
            writeToFile()  # after every genquad we write it into the .int file
            R_false = makelist(nextquad())
            genquad("jump", "_", "_", "_")
            writeToFile()  # after every genquad we write it into the .int file
        else:
            print("ERROR AT LINE %d, COMPARE OPERATOR NOT FOUND" % lineNo)
            sys.exit(error_TK)
    return R_true, R_false


# E-> T1 (+ T2 {P1} )* {P2}
def expression():  # optionalSign term ( ADD_OP term )∗ , NOTE: avoid unnecessary parentheses. cimple does not support it
    global keepers
    op = optionalSign()
    T1_place = term()
    while state == plus_TK or state == sub_TK:
        op = tokenString
        T2_place = term()
        # expression of p1
        w = newtemp()  # keeps the up-to-date result
        if len(keepers) == 2:
            genquad(op, keepers[0], keepers[1], w)
            writeToFile()  # after every genquad we write it into the .int file
            keepers = []
        else:
            genquad(op, T1_place, T2_place, w)
            writeToFile()  # after every genquad we write it into the .int file
        T1_place = w  # in case we have next T2
    # expression of p2
    E_place = T1_place  # in case we don't have next T2
    return E_place


def optionalSign():  # ADD_OP | e
    if state == plus_TK or state == sub_TK:
        lex()


# Τ-> F1 ( x F2 {P1})* {P2}  same logic as expression function
def term():  # factor ( MUL_OP factor )∗
    global keepers
    F1_place = factor()
    while state == multiply_TK or state == divide_TK:
        op = tokenString
        F2_place = factor()
        # expression of p1
        w = newtemp()
        if len(keepers) == 2:
            genquad(op, keepers[0], keepers[1], w)
            writeToFile()  # after every genquad we write it into the .int file
            keepers = []
        else:
            genquad(op, F1_place, F2_place, w)
            writeToFile()  # after every genquad we write it into the .int file
        F1_place = w
    # expression of p2
    T_place = F1_place
    return T_place


# F->(E) {P1}  {P1}: F_place=E_place
# F->id{P1}  {P1}: F_place=id_place
def factor():  # INTEGER | ( expression ) | ID idtail
    global F_place
    if state in key_words.values() and state != in_TK and state != inout_TK:
        print("ERROR, WRONG SYNTAX AT LINE %d " % lineNo)
        sys.exit(error_TK)
    if state != id_TK:
        F_place = tokenString
        lex()
    if state == constant_TK:
        F_place = tokenString
        lex()
    elif state == left_parentheses_TK:
        lex()
        F_place = expression()
        if state == right_parentheses_TK:
            lex()
        else:
            print("ERROR AT LINE %d. ) IS MISSING" % lineNo)
            sys.exit(error_TK)
    elif state == id_TK:
        F_place = tokenString
        lex()
        idtail(F_place)
    else:
        print("ERROR, WRONG SYNTAX FOR THE EXPRESSION AT LINE %d " % lineNo)
        sys.exit(error_TK)
    return F_place


def idtail(name):  # ( actualparlist ) | e
    templist = emptylist()
    global keepers
    if state == left_parentheses_TK:
        templist = actualparlist(name)
        if state == right_parentheses_TK:
            lex()
        else:
            print("ERROR AT LINE %d, ) IS MISSING." % lineNo)
            sys.exit(error_TK)
        w = newtemp()
        keepers.append(w)
        genquad("par", w, "RET", "_")
        writeToFile()  # after every genquad we write it into the .int file
        genquad("call", "_", "_", name)
        writeToFile()  # after every genquad we write it into the .int file
        return w
    return keepers


# ----------------------------Median Code .int and .c files-------------------------------------------------------#

quad_list = []
quad_counter = 1
keepers = []  # this is to keep the T_x when the genquad has operator, to save the idtail variables


def nextquad():  # returns the number of the next created quad
    global quad_counter
    return quad_counter


def genquad(op, x, y, z):  # creates the next quad
    global quad_list
    global quad_counter

    gen_list = [nextquad()]
    gen_list.append(op)
    gen_list.append(x)
    gen_list.append(y)
    gen_list.append(z)

    quad_counter += 1
    quad_list += [gen_list]
    return quad_list


T_x = 1  # temporal variable
temp_list = []  # temporal variable list
declare_list = []  # temporal declare list


def newtemp():  # we create a new temporal variable, T_1, T_2, T_3, ...
    global T_x
    global temp_list
    temp_str = 'T_'
    temp_str += str(T_x)
    T_x += 1
    temp_list += [temp_str]

    # create entity for the table of symbols
    entity = Record_entity()
    entity.type = 'Temp'
    entity.name = temp_str
    entity.tempVar.offset = get_offset()
    new_entity(entity)

    return temp_str


def emptylist():  # creates and returns an empty quad list
    empty_list = []
    return empty_list


def makelist(x):  # creates a list of labels for the quads that contains only x
    make_list = [x]
    return make_list


def mergelist(list1, list2):  # we merge the two list
    merge_list = []
    merge_list += list1
    merge_list += list2
    return merge_list


def backpatch(listt, z):  # has pointers to quads where last op doesnt exists,
    # backpatch visits one by one those quads and puts z
    global quad_list
    for x in range(0, len(listt)):
        for j in range(0, len(quad_list)):
            if listt[x] == quad_list[j][0] and str(quad_list[j][4]) == '_':  # same label and in place 4 _ in quadlist
                quad_list[j][4] = z
                j = len(quad_list)


def intWriteFile(intFile):  # WRITES QUADS TO .int FILE, MEDIAN CODE
    for x in range(len(quad_list)):
        quad = quad_list[x]
        intFile.write(str(quad[0]))
        intFile.write(":  ")  # we separate the enumerations with :
        intFile.write(str(quad[1]))
        intFile.write("  ")
        intFile.write(str(quad[2]))
        intFile.write("  ")
        intFile.write(str(quad[3]))
        intFile.write("  ")
        intFile.write(str(quad[4]))
        intFile.write("\n")


def writeToFile():  # opens file and writes everything
    file = open("test.int", "w")  # file = open(filename+'.int','w+')
    intWriteFile(file)
    file.close()


def cWrite(cFile):  # we add the quads in the .c file in c code
    global temp_list
    intFile = open("test.int", "r")  # we open the .int file to add the comments in the .c file
    cFile.write("int main()\n")
    cFile.write("{\n\t")
    temp_list = temp_list + declare_list
    temp_list = list(dict.fromkeys(temp_list))  # sort the list with parameters
    if len(temp_list) != 0:
        cFile.write("int ")
    for i in range(len(temp_list)):  # we write the temp vars in the .c file
        cFile.write(temp_list[i])
        if len(temp_list) == i + 1:
            cFile.write(";\n\t")  # in the end of every statement we add the semi-colon
        else:
            cFile.write(",")
    intFile.readline()  # we read the first line cause we dont need it in.c file
    for j in range(len(quad_list)):  # we check the genquad to do the proper convert for the .c file
        if quad_list[j][1] == 'begin_block':
            cFile.write("L_" + str(j + 1) + ":\n\t")
        elif quad_list[j][1] == "jump":
            cFile.write(
                "L_" + str(j + 1) + ": " + "goto L_" + str(quad_list[j][4]) + "; // " + intFile.readline() + "\t")
        elif quad_list[j][1] == "+":
            cFile.write("L_" + str(j + 1) + ": " + str(quad_list[j][4]) + " = " + str(quad_list[j][2]) + " + " + str(
                quad_list[j][3]) + "; // " + intFile.readline() + "\t")
        elif quad_list[j][1] == "-":
            cFile.write("L_" + str(j + 1) + ": " + str(quad_list[j][4]) + " = " + str(quad_list[j][2]) + " - " + str(
                quad_list[j][3]) + "; // " + intFile.readline() + "\t")
        elif quad_list[j][1] == "*":
            cFile.write("L_" + str(j + 1) + ": " + str(quad_list[j][4]) + " = " + str(quad_list[j][2]) + " * " + str(
                quad_list[j][3]) + "; // " + intFile.readline() + "\t")
        elif quad_list[j][1] == "/":
            cFile.write("L_" + str(j + 1) + ": " + str(quad_list[j][4]) + " = " + str(quad_list[j][2]) + " / " + str(
                quad_list[j][3]) + "; // " + intFile.readline() + "\t")
        elif quad_list[j][1] == ":=":
            cFile.write("L_" + str(j + 1) + ": " + str(quad_list[j][4]) + " = " + str(
                quad_list[j][2]) + "; // " + intFile.readline() + "\t")
        elif quad_list[j][1] == "<":
            cFile.write("L_" + str(j + 1) + ": " + "if (" + str(quad_list[j][2]) + " < " + str(
                quad_list[j][3]) + ") goto L_" + str(quad_list[j][4]) + "; // " + intFile.readline() + "\t")
        elif quad_list[j][1] == ">":
            cFile.write("L_" + str(j + 1) + ": " + "if (" + str(quad_list[j][2]) + " > " + str(
                quad_list[j][3]) + ") goto L_" + str(quad_list[j][4]) + "; // " + intFile.readline() + "\t")
        elif quad_list[j][1] == "<=":
            cFile.write("L_" + str(j + 1) + ": " + "if (" + str(quad_list[j][2]) + " <= " + str(
                quad_list[j][3]) + ") goto L_" + str(quad_list[j][4]) + "; // " + intFile.readline() + "\t")
        elif quad_list[j][1] == ">=":
            cFile.write("L_" + str(j + 1) + ": " + "if (" + str(quad_list[j][2]) + " >= " + str(
                quad_list[j][3]) + ") goto L_" + str(quad_list[j][4]) + "; // " + intFile.readline() + "\t")
        elif quad_list[j][1] == "=":
            cFile.write("L_" + str(j + 1) + ": " + "if (" + str(quad_list[j][2]) + " == " + str(
                quad_list[j][3]) + ") goto L_" + str(quad_list[j][4]) + "; // " + intFile.readline() + "\t")
        elif quad_list[j][1] == "<>":
            cFile.write("L_" + str(j + 1) + ": " + "if (" + str(quad_list[j][2]) + " != " + str(
                quad_list[j][3]) + ") goto L_" + str(quad_list[j][4]) + "; // " + intFile.readline() + "\t")
        elif quad_list[j][1] == "inp":
            cFile.write("L_" + str(j + 1) + ": " + "scanf(\"" + str(quad_list[j][2]) + " = %d\", &" + str(
                quad_list[j][2]) + "); // " + intFile.readline() + "\t")
        elif quad_list[j][1] == "out":
            cFile.write("L_" + str(j + 1) + ": " + "printf(\"" + str(quad_list[j][2]) + " = %d\", " + str(
                quad_list[j][2]) + "); // " + intFile.readline() + "\t")
        elif quad_list[j][1] == 'halt':
            cFile.write("L_" + str(j + 1) + ": {} // " + intFile.readline())
    cFile.write("}")


def open_cfile():  # we open and create the cFile and we add the converted cCode
    cFile = open("test.c", "w")  # cFile = open(filename+'.c','w+')
    cWrite(cFile)
    cFile.close()


# --------------------------TABLE OF SYMBOLS---------------------------------------------------------#
mainScope = None


# initialize record entity and its fields
class Record_entity():
    def __init__(self):
        self.name = ''
        self.type = ''
        self.variable = self.variable()
        self.subProgram = self.subProgram()
        self.constant = self.constant()
        self.parameter = self.parameter()
        self.tempVar = self.tempVar()

    class variable:
        def __init__(self):
            self.type = 'int'
            self.offset = 0  # distance from the beginning of the activation record

    class subProgram:
        def __init__(self):
            self.type = ''
            self.startQuad = 0  # tag of the quad from subProgram
            self.argument_list = []
            self.frameLength = 0  # length of the activation record

    class constant:
        def __init__(self):
            self.value = 0

    class parameter:
        def __init__(self):
            self.par_mode = ''  # way of passing the parameter
            self.offset = 0  # distance from the top of the stack

    class tempVar:
        def __init__(self):
            self.offset = 0
            self.type = 'int'  # distance from the top of the stack


# record scope is the main program or a procedure/function
class Record_scope():
    def __init__(self):
        self.name = ''
        self.finalScope = None
        self.list_entity = []  # list of Entities
        self.nestingLevel = 0  # depth of the nesting


# initialize record argument based on professor's slides
class Record_argument():
    def __init__(self):
        self.name = ''
        self.parMode = ''  # way of passing the parameter
        self.type = 'int'  # type of the variable


# functions for the activities of the table of symbols
def new_scope(name):  # when we start the compilation of a new subFunction
    global mainScope
    nextScope = Record_scope()
    nextScope.name = name
    nextScope.finalScope = mainScope
    if mainScope == None:
        nextScope.nestingLevel = 0
    else:
        nextScope.nestingLevel = mainScope.nestingLevel + 1
    mainScope = nextScope


def delete_scope():  # after the compilation we delete the record of Scope and all the
    # list with the Entities and the Arguments that depend on it
    global mainScope
    deleteScope = mainScope
    mainScope = mainScope.finalScope
    del deleteScope


def new_entity(object):  # we add new entity whenever we get a new variable, tempVar, new function, var of a func
    global mainScope
    mainScope.list_entity.append(object)


def new_argument(object):  # we add new argument whenever we find a function variable
    global mainScope
    mainScope.list_entity[-1].subProgram.argument_list.append(object)


def get_offset():
    global mainScope
    off_counter = 0
    if mainScope.list_entity is not []:
        for entity in mainScope.list_entity:
            if entity.type == 'Variable' or entity.type == 'Temp' or entity.type == 'Parameter' or entity.type == 'Constant':
                off_counter += 1
    offset = 12 + (off_counter * 4)
    return offset


def get_firstQuad():
    global mainScope
    mainScope.finalScope.list_entity[-1].subProgram.startQuad = nextquad()


def add_parameters():
    global mainScope
    for arg in mainScope.finalScope.list_entity[-1].subProgram.argument_list:
        entity = Record_entity()
        entity.name = arg.name
        entity.type = 'Parameter'
        entity.parameter.par_mode = arg.parMode
        entity.parameter.offset = get_offset()
        new_entity(entity)


def get_frameLen():
    global mainScope
    mainScope.finalScope.list_entity[-1].subProgram.frameLength = get_offset()


def write_table_of_symbols(tableFile):  # we write the table of symbols to a file to check the result
    nowScope = mainScope
    while nowScope != None:
        tableFile.write(
            "| RECORD SCOPE-> " + " Name: " + str(nowScope.name) + ", NestingLevel: " + str(nowScope.nestingLevel))
        tableFile.write("\n")
        tableFile.write("| ENTITIES: \n")
        for entity in nowScope.list_entity:
            if entity.type == 'Variable':
                tableFile.write("\t| RECORD ENTITY-> " + " Name:  " + str(entity.name) + "\t| Type:  " + str(
                    entity.type) + "\t| VarType: " + str(entity.variable.type) + "\t| Offset: " + str(
                    entity.variable.offset) + "|")
                tableFile.write("\n")
            elif entity.type == 'Temp':
                tableFile.write("\t| RECORD ENTITY-> " + " Name:  " + str(entity.name) + "\t| Type:  " + str(
                    entity.type) + "\t| TempType: " + str(entity.tempVar.type) + "\t| Offset: " + str(
                    entity.tempVar.offset) + "|")
                tableFile.write('\n')
            elif entity.type == 'Subprogram':
                if entity.subProgram.type == 'Procedure':
                    tableFile.write("\t| RECORD ENTITY-> " + " Name: " + str(
                        entity.name) + "\t| Type: " + entity.type + "\t| Subprogram type: " + str(
                        entity.subProgram.type) + "\t| Start Quad: " + str(
                        entity.subProgram.startQuad) + "\t| Frame Length: " + str(entity.subProgram.frameLength))
                    for arg in entity.subProgram.argument_list:
                        tableFile.write("\n\t| RECORD ARGUMENT-> " + "Name: " + str(
                            arg.name) + "\t| Type: " + arg.type + "\t| ParMode: " + str(arg.parMode) + "|")
                elif entity.subProgram.type == 'Function':
                    tableFile.write("\t| RECORD ENTITY-> " + " Name: " + str(
                        entity.name) + "\t| Type: " + entity.type + "\t| Subprogram type: " + str(
                        entity.subProgram.type) + "\t| Start Quad: " + str(
                        entity.subProgram.startQuad) + "\t| Frame Length: " + str(entity.subProgram.frameLength) + "|")
                    for arg in entity.subProgram.argument_list:
                        tableFile.write("\n\t| RECORD ARGUMENT-> " + " Name: " + str(
                            arg.name) + "\t| Type: " + arg.type + "\t| ParMode: " + str(arg.parMode) + "|")
                tableFile.write('\n')
            elif entity.type == 'Parameter':
                tableFile.write("\t| RECORD ENTITY-> " + " Name: " + str(entity.name) + "\t| Type: " + str(
                    entity.type) + "\t| Mode: " + str(entity.parameter.par_mode) + "\t| Offset:" + str(
                    entity.parameter.offset) + "|")
                tableFile.write('\n')
        nowScope = nowScope.finalScope


#  ---------------------TELIKOS KWDIKAS .asm----------------------------------------------------------#

# auxiliary functions

asmWrite = open("test.asm", "w")


def get_node(node):  # we get every scope and entity in order to implement the final code
    global mainScope
    Record_scope = mainScope
    while Record_scope != None:
        for entity in Record_scope.list_entity:
            if entity.name == node:
                return Record_scope, entity


# from the symbol table finds how many levels the non-local variable is on and locates it through the access link
def gnvlcode(var):  # moves to $t0 the address of a non-local variable
    global mainScope
    global asmWrite
    asmWrite.write("\tlw $t0, -4($sp)\n")
    scope, entity = get_node(var)
    nestingLoop = mainScope.nestingLevel - scope.nestingLevel
    nestingLoop -= 1
    for i in range(0, nestingLoop):
        asmWrite.write("\tlw $t0, -4($sp)\n")
    if entity.type == 'Variable':
        entity = entity.variable.offset
    elif entity.type == 'Parameter':
        entity = entity.parameter.offset
    asmWrite.write('\tadd $t0,$t0,-' + str(entity))


def loadvr(v, r):  # data transfer to register r
    global mainScope
    global asmWrite
    if v.isdigit():  # if v is constant "li $tr,v"
        asmWrite.write('\tli $t' + str(r) + ',' + str(v) + '\n')
    else:
        (scope1, entity1) = get_node(v)
        # if v is a global variable - that is, it belongs to the main program "lw $tr,-offset($s0)"
        if scope1.nestingLevel == 0 and entity1.type == 'Variable':
            asmWrite.write('\tlw $t' + str(r) + ",-" + str(entity1.variable.offset) + '($s0) \n')
        # if v is a global variable, it belongs to the main program "lw $tr,-offset($s0)"
        elif scope1.nestingLevel == 0 and entity1.type == 'Temp':
            asmWrite.write('\tlw $t' + str(r) + ",-" + str(entity1.tempVar.offset) + '($s0) \n')
        elif scope1.nestingLevel == mainScope.nestingLevel:
            # if v is declared in the function that is currently running and is a local variable,
            # or a standard parameter that passes with a value, or a temporary variable "lw $tr,-offset($sp)"
            if entity1.type == 'Variable':
                asmWrite.write('\tlw $t' + str(r) + ",-" + str(entity1.variable.offset) + '($sp) \n')
            elif entity1.type == 'Temp':
                asmWrite.write('\tlw $t' + str(r) + ",-" + str(entity1.tempVar.offset) + '($sp) \n')
            elif entity1.type == 'Parameter' and entity1.parameter.par_mode == 'REF':
                asmWrite.write('\tlw $t0,-' + str(entity1.parameter.offset) + '($sp) \n')
                asmWrite.write('\tlw $t' + str(r) + ",($t0)\n")
            elif entity1.type == 'Parameter' and entity1.parameter.par_mode == 'CV':
                asmWrite.write('\tlw $t' + str(r) + ",-" + str(entity1.parameter.offset) + '($sp) \n')
        elif scope1.nestingLevel < mainScope.nestingLevel:
            # if v has been declared to an ancestor and there is a local variable,
            # or a standard parameter that passes with a value "lw $tr,($t0)"
            if entity1.type == 'Variable':
                gnvlcode(v)
                asmWrite.write('\tlw $t' + str(r) + ',($t0)\n')
            elif entity1.type == 'Parameter' and entity1.parameter.par_mode == 'REF':
                gnvlcode(v)
                asmWrite.write('\tlw $t0,($t0)\n')
                asmWrite.write('\tlw $t' + str(r) + ",($t0)\n")
            elif entity1.type == 'Parameter' and entity1.parameter.par_mode == 'CV':
                gnvlcode(v)
                asmWrite.write('\tlw $t' + str(r) + ',($t0)\n')


def storerv(r, v):  # data transfer from register r to memory (variable v)
    global mainScope
    global asmWrite
    (scope1, entity1) = get_node(v)
    # if v is a universal variable - that is, it belongs to the main program "sw $tr,-offset($s0)"
    if scope1.nestingLevel == 0 and entity1.type == 'Variable':
        asmWrite.write('\tsw $t' + str(r) + ",-" + str(entity1.variable.offset) + '($s0) \n')
    elif scope1.nestingLevel == 0 and entity1.type == 'Temp':
        asmWrite.write('\tsw $t' + str(r) + ",-" + str(entity1.tempVar.offset) + '($s0) \n')
    elif scope1.nestingLevel == mainScope.nestingLevel:
        if entity1.type == 'Variable':
            asmWrite.write('\tsw $t' + str(r) + ",-" + str(entity1.variable.offset) + '($sp) \n')
        elif entity1.type == 'Temp':
            asmWrite.write('\tsw $t' + str(r) + ",-" + str(entity1.tempVar.offset) + '($sp) \n')
        elif entity1.type == 'Parameter' and entity1.parameter.par_mode == 'REF':
            asmWrite.write('\tlw $t0,-' + str(entity1.parameter.offset) + '($sp) \n')
            asmWrite.write('\tsw $t' + str(r) + ",($t0)\n")
        elif entity1.type == 'Parameter' and entity1.parameter.par_mode == 'CV':
            asmWrite.write('\tsw $t' + str(r) + ",-" + str(entity1.parameter.offset) + '($sp) \n')
    elif scope1.nestingLevel < mainScope.nestingLevel:
        # if v is a local variable, or a standard parameter that passes with a value
        # and nesting depth equal to the current, or a temporary variable "sw $tr,-offset($sp)"
        if entity1.type == 'Variable':
            gnvlcode(v)
            asmWrite.write('\tsw $t' + str(r) + ',($t0)\n')
        elif entity1.type == 'Parameter' and entity1.parameter.par_mode == 'REF':
            gnvlcode(v)
            asmWrite.write('\tlw $t0,($t0)\n')
            asmWrite.write('\tsw $t' + str(r) + ",($t0)\n")
        elif entity1.type == 'Parameter' and entity1.parameter.par_mode == 'CV':
            gnvlcode(v)
            asmWrite.write('\tsw $t' + str(r) + ',($t0)\n')


def asm_code():
    # writing to the test.asm the appropriate code based on professor's slides
    global mainScope
    global asmWrite
    global quad_list

    x = len(quad_list)
    if mainScope.nestingLevel >= 0:
        asmWrite.write('L0: b L' + mainScope.name + '\n')
    for i in range(0, x):
        asmWrite.write('\nL' + str(quad_list[i][0]) + ': \n')
        if quad_list[i][1] == 'jump':
            asmWrite.write('\n\tj L' + str(quad_list[i][4]))
        elif quad_list[i][1] == '>':
            loadvr(quad_list[i][2], 1)
            loadvr(quad_list[i][3], 2)
            asmWrite.write('\tbgt $t1,$t2,L' + str(quad_list[i][4]))
        elif quad_list[i][1] == '<':
            loadvr(quad_list[i][2], 1)
            loadvr(quad_list[i][3], 2)
            asmWrite.write('\tblt $t1,$t2,L' + str(quad_list[i][4]))
        elif quad_list[i][1] == '>=':
            loadvr(quad_list[i][2], 1)
            loadvr(quad_list[i][3], 2)
            asmWrite.write('\tbge $t1,$t2,L' + str(quad_list[i][4]))
        elif quad_list[i][1] == '<=':
            loadvr(quad_list[i][2], 1)
            loadvr(quad_list[i][3], 2)
            asmWrite.write('\tble $t1,$t2,L' + str(quad_list[i][4]))
        elif quad_list[i][1] == '<>':
            loadvr(quad_list[i][2], 1)
            loadvr(quad_list[i][3], 2)
            asmWrite.write('\tbne $t1,$t2,L' + str(quad_list[i][4]))
        elif quad_list[i][1] == ':=':
            loadvr(quad_list[i][2], 1)
            storerv(1, quad_list[i][4])
        elif quad_list[i][1] == '+':
            loadvr(quad_list[i][2], 1)
            loadvr(quad_list[i][3], 2)
            asmWrite.write('\tadd $t1,$t1,$t2' + '\n')
            storerv(1, quad_list[i][4])
        elif quad_list[i][1] == '*':
            loadvr(quad_list[i][2], 1)
            loadvr(quad_list[i][3], 2)
            asmWrite.write('\tmul $t1,$t1,$t2' + '\n')
            storerv(1, quad_list[i][4])
        elif quad_list[i][1] == '/':
            loadvr(quad_list[i][2], 1)
            loadvr(quad_list[i][3], 2)
            asmWrite.write('\tdiv $t1,$t1,$t2' + '\n')
            storerv(1, quad_list[i][4])
        elif quad_list[i][1] == '-':
            loadvr(quad_list[i][2], 1)
            loadvr(quad_list[i][3], 2)
            asmWrite.write('\tsub $t1,$t1,$t2' + '\n')
            storerv(1, quad_list[i][4])
        # Passing print: out “_”, “_”, x
        elif quad_list[i][1] == 'out':
            asmWrite.write('\tli $v0, 1' + '\n')  # label op, x, y, z
            loadvr(quad_list[i][2], 0)
            asmWrite.write('\tmove $a0,$t1' + '\n')
            asmWrite.write('\tsyscall' + '\n')
        # Passing return: retv “_”, “_”, xs
        elif quad_list[i][1] == 'retv':
            loadvr(quad_list[i][2], 1)
            asmWrite.write('\tlw $t0, -8(&sp)' + '\n')
            asmWrite.write('\tsw $t1, ($t0)' + '\n')
        # Passing input: inp “_”, “_”, x
        elif quad_list[i][1] == 'inp':
            asmWrite.write('\tli $v0, 5' + '\n')
            asmWrite.write('\tsyscall\n')
            storerv(0, quad_list[i][2])
        # Passing PAR with REF
        elif quad_list[i][1] == 'par' and quad_list[i][3] == 'REF':
            asmWrite.write('\taddi $t0,$sp,-' + str(get_offset()) + '\n')
            asmWrite.write('\tsw $t0, -'+str(12+4*i)+'($fp)\n')
            i = i +1
        # Passing PAR with CV: par,x,CV, _
        elif quad_list[i][1] == 'par' and quad_list[i][3] == 'CV':
            loadvr(quad_list[i][2], 0)
            asmWrite.write('\tsw $t0, -'+str(12+4*i)+'($fp)\n')
            i = i + 1
        # Passing PAR with RET: par,x,RET, _
        elif quad_list[i][1] == 'par' and quad_list[i][3] == 'RET':
            asmWrite.write('\taddi $t0,$sp,-' + str(get_offset()) + '\n')
            asmWrite.write('\tsw $t0,-8($fp)\n')
        # Passing call
        elif quad_list[i][1] == 'call':
            if mainScope.name == quad_list[i][4]:
                if mainScope.nestingLevel == Record_scope().nestingLevel:
                    asmWrite.write('\tlw $t0, -4($sp)\n')
                    asmWrite.write('\tsw $t0, -4($sp)\n')
                else:
                    asmWrite.write('\tsw $sp, -4($fp)\n')
        elif quad_list[i][1] == 'begin_block' and mainScope.nestingLevel >= 0:
            asmWrite.write('\tadd $sp,$sp,' + str(get_offset()) + '\n')
            asmWrite.write('\tmove $s0,$sp\n')
        elif quad_list[i][1] == 'end_block' and mainScope.nestingLevel >= 0:
            asmWrite.write('\tlw $ra,($sp)\n')
            asmWrite.write('\tjr $ra\n')

program()
filename.close()
