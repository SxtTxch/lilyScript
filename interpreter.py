class Lexer():
    def __init__(self) -> None:
        self.pos = 0
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


def parse(file):
    contents = open(file, 'r').read()
    tokens = Lexer.tokenize(contents)
    return tokens