# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 19:13:13 2019

@author: guvnc
"""
import operator

class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []
     
     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def size(self):
         return len(self.items)

def ControlOperation(operation):
    
    usableChar = ['+','-','/','*']
    stack = Stack()
    
    for i in operation:
        if i == "(":
            stack.push(i)
        elif i == ")":
            stack.pop()
        elif i in usableChar or isNumber(i):
            continue
        else:
            return False
        
    if stack.isEmpty():
        return True
    else:
        return False
    
    
def Operation(postfixString):
    
    stack = Stack()
    
    currentNum = ""
    
    i = 0
    
    while i < len(postfixString): 
        if postfixString[i] == "|":
            i+=1
        elif isNumber(postfixString[i]):
            while True:
                currentNum += postfixString[i]
                i+=1
                if isNumber(postfixString[i]):
                    break
                else:
                    stack.push(currentNum)
                    currentNum = ""
                    break
        else:
            num2 = float(stack.pop())
            num1 = float(stack.pop())
            result = doMath(num1, postfixString[i], num2)
            stack.push(result)
            i+=1
       
        
    print("Result: ",stack.pop())
        
def Translation(opString):
    
    opString += '?'
    
    stack = Stack()
    postfix = ""

    for i in opString:
        if i == ' ':
            continue
        elif i == '(':
            stack.push(i)            
        elif i == ')' or i == '?':
            for j in range(0,stack.size()):
                temp = stack.pop()
                if temp == "(":
                    break
                else:
                    postfix += temp
        elif not isNumber(i):
            postfix += "|"
            for j in range(0,stack.size()):
                if isWeak(i,stack): 
                    temp = stack.pop()
                    postfix += temp
            stack.push(i)
            continue
        else:
            postfix += i
    
    print("Postfix: ", postfix)
    Operation(postfix)
        
def get_operator(op):
    return {
        '+' : operator.add,
        '-' : operator.sub,
        '*' : operator.mul,
        '/' : operator.truediv,
        }[op]

def doMath(num1, oper, num2):
    return get_operator(oper)(num1, num2)

def isWeak(character,stack):
            
    temp = ""
    if not stack.isEmpty():
        temp += stack.pop()
    
    if character == '*' or character == '/' or stack.isEmpty():
        stack.push(temp)
        return False

    if character == '+' or character == '-':
        if temp == '*' or temp == '/':
            stack.push(temp)
            return True
        else:
            stack.push(temp)
            return False

def isNumber(character):
    
    numberArray = ['0','1','2','3','4','5','6','7','8','9']
    
    if character in numberArray:
        return True
    else:
        return False

operation = input("Enter the operation: ")

if ControlOperation(operation):
    print("Operation: ",operation)
    Translation(operation)
else:
    print("Wrong Operation")