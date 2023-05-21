import os
import sys
from engine import *
engine = Engine()
class Error():
    def __init__(self, content) -> None:
        self.content = "Error: " + content
    def throw(self):
        print(self.content)
        exit()

class Statements():
    def calc(self, args):
        for arg in range(len(args)):
            if args[arg] in engine.memory:
                args[arg] = engine.memory[args[arg]]
        return eval(''.join(args))
    def write(self, args):
        for arg in range(len(args)):
            if args[arg] in engine.memory:
                args[arg] = engine.memory[args[arg]]
            print(args[arg])
    def let(self, args):
        if len(args) != 2:
            Error(content="improper variable initialization syntax.").throw()
        else:
            engine.memory[args[0]] = args[1]

class Lexer():
    def __init__(self) -> None:
        self.currentline = None
        self.statements = Statements()
        self.loops = Loops()
    def tokenize(text : str):
        arr = text.split('\n')
        alltokens = []
        for line in range(len(arr)):
            chars = list(arr[line])
            tokens = []
            temp = ""
            quote_num = 0
            in_quotes = False
            for char in range(len(chars)):
                if chars[char] == '"' or chars[char] == "'":
                    quote_num += 1
                    if quote_num % 2 == 0:
                        in_quotes = False
                    else:
                        in_quotes = True

                if chars[char] == " " and in_quotes == False:
                    tokens.append(temp)
                    temp = ""
                else:
                    temp += chars[char]
            tokens.append(temp)
            alltokens.append(tokens)
        return alltokens
    def transform(self,alltokens : list):
        for tokenline in range(len(alltokens)):
            self.currentline = alltokens[tokenline]
            for token in range(len(alltokens[tokenline])-1,-1,-1):
                for statement in range(len(dir(self.statements))):
                    if dir(self.statements)[statement] == alltokens[tokenline][token]:
                        method = getattr(self.statements,dir(self.statements)[statement])
                        result = method([arg for arg in alltokens[tokenline] if alltokens[tokenline].index(arg) > alltokens[tokenline].index(alltokens[tokenline][token])])
                        for element in range(len(alltokens[tokenline])-1, token, -1):
                            alltokens[tokenline].pop(element)
                        if result != None:
                            alltokens[tokenline][token] = result
                        break
                        
def parse(file):
    contents = open(file, 'r').read()
    lexer = Lexer()
    tokens = Lexer.tokenize(contents)
    lexer.transform(tokens)
    return tokens