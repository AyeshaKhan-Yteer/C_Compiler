import re

f = open('Read.py','r')

operators = { '=': 'Assignment Operator','+': 'Addition Operator', '-' : 'Substraction Operator', '/' : 'Division Operator', '*': 'Multiplication Operator', '++' : 'increment Operator', '--' : 'Decrement Operator'}
optr_keys = operators.keys()

comments = {r'//' : 'Single Line Comment',r'/*' : 'Multiline Comment Start', r'*/' : 'Multiline Comment End', '/**/' : 'Empty Multiline comment'}
comment_keys = comments.keys()

header = {'.h': 'header file'}
header_keys = header.keys()

sp_header_files = {'<stdio.h>':'Standard Input Output Header','<string.h>':'String Manipulation Library','<conio.h>':'Console Input Output'}

datatype = {'int': 'Integer','float' : 'Floating Point', 'char': 'Character','long': 'long int'}
type_spec = datatype.keys()

keyword = {'return' : 'keyword that returns a value from a block','ForLoop': 'Control Flow Statement Repeatedly','WhileLoop':'Condition True And Then Body Of Loop Is Executed','If':'More Than One Flow Of Control','If-else':'Based On Specific Conditions','Break':'Break Statement','Continue':'Continues','Switch': 'Switch Case','Case':'Case Statement','Void':'Void Statement','Size of':'Tells Size Of Type','Double':'Double Int Type','Float':'Decimal Digits','Int':'Integer Type','Signed':'Signed Int','Unsigned':'Unsigned Int','Long':'Long Int','Char':'Chararcter Type'}
keyword_keys = keyword.keys()

delimiter = {';':'terminator symbol semicolon (;)'}
delim_keys = delimiter.keys()

builtin_func = {'printf':'printf prints its argument on the console'}

non_identifiers = ['_','-','+','/','*','`','~','!','@','#','$','%','^','&','*','(',')','=','|','"',':',';','{'
,'}','[',']','<','>','?','/']

numerals = ['0','1','2','3','4','5','6','7','8','9','10']

# Flags
dataFlag = False


i = f.read()

count = 0
program =  i.split('\n')

for line in program:
    count = count+1
    print ("Line #",count,"\n",line)
    
     
    tokens = line.split(' ')
    print ("Tokens are",tokens)
    print ("Line #",count,'properties \n')
    for token in tokens:
        
        if '\r' in token:
            position = token.find('\r')
            token=token[:position]
        # print 1
        
        if token in optr_keys:
            print ("Operator is: ", operators[token])
        if token in comment_keys:
            print ("Comment Type: ", comments[token])

        if '.h' in token:
            print ("Header File is: ",token, sp_header_files[token])
        if '()' in token:
            print ("Function named", token)
        
        if dataFlag == True and (token not in non_identifiers) and ('()' not in token):
            print ("Identifier: ",token)
        if token in type_spec:
            print ("type is: ", datatype[token])
            dataFlag = True
        
        if token in keyword_keys:
            print( keyword[token])
            
        if token in delimiter:
            print ("Delimiter" , delimiter[token])

        if token in numerals:
            print (token,type(int(token)))
            
    dataFlag = False   
            
    
    print ("________________________")
    

f.close()

