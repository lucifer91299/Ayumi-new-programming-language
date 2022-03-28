
from ast import keyword
from cmd import Cmd
from texttable import Texttable

class MyPrompt(Cmd):
    prompt = 'HELP > '
    intro = "Welcome! Type ? to list commands help <type>  for more info type help more  "
 
    def do_exit(self, inp):
        print("Bye")
        return True

       
    def help_exit(self):
        print('exit the application. Shorthand: x q Ctrl-D.')
        
    def do_Keywords(self, inp):
                # Function to convert number into string
        # Switcher is dictionary data type here
        def numbers_to_strings(argument):
            try:
                switcher = {
                1: """VAR variable_name = value """,
                2: """VAR variable_name = INPUT()""",
                3: """VAR variable_name = INPUT_INT()""",
                4: """IF a > B AND B != 0 THEN; PRINT("hi")END""",
                5: """Returns True if one of the statements is true. ex IF a > B OR B != 0 THEN; PRINT("hi")END""",
                6: """Clear is used to clean the terminal window""",
                7: """The 'not' is a Logical operator in Python that will return True if the expression is False. """,
                8: """CLS is used to clean the terminal window""",
                9: """ex:- IF CONDITION THEN; -- statment --END""",
                10: """ It returns true if statement is integer else false""",
                11: """are conditional statements that provide you with the decision making that is required when you want to execute code based on a particular condition.:""",
                12: """It returns true if statement is string else false""",
                13: """ELSE""",
                14: """It returns true if statement is LIST else false. A list is a data structure that is a mutable, or changeable, ordered sequence of elements. Each element or value that is inside of a list is called an item. Just as strings are defined as characters between quotes, lists are defined by having values between square brackets [ ].""",
                15: """for loops are used when you have a block of code which you want to repeat a fixed number of times. The for-loop is always used in combination with an iterable object, like a list or a range. The Python for statement iterates over the members of a sequence in order, executing the block each time.
                one line FOR loop "FOR START = 0 TO END_VALUE THEN; statment  END" 
                multi-line "FOR START = 0 TO END_VALUE THEN
                                 statment  
                                 END""",
                16: """Something went wrong""",
                17: """Something went wrong""",
                18: """append() method adds a single item to the existing list. It doesn’t return a new list of items but will modify the original list by adding the item to the end of the listex:-APPEND(new_elements, INDEX)""",
                19: """STEP 1+ until """,
                20: """""",
                21: """The while loop is used to iterate over a block of code as long as the test expression (condition) is true.
We generally use this loop when we don't know the number of times to iterate beforehand.
""",
                22: """Removes and returns the last value from the List or the given index value.""",
                23: """In Python, a function is a group of related statements that performs a specific task.

Functions help break our program into smaller and modular chunks. As our program grows larger and larger, functions make it more organized and manageable.ex:- FUN join(elements, separator)
	VAR result = ""
	VAR len = LEN(elements)

	FOR i = 0 TO len THEN
		VAR result = result + elements/i #find elements
		IF i != len - 1 THEN VAR result = result + separator
	END

	RETURN result
END""",
                24: """returns the number of items in an object ex : LEN(elements)""",
                25: """THEN statement  """,
                26: """A return statement is used to end the execution of the function call and “returns” the result (value of the expression following the return keyword) to the caller ex : RUN --> RUN("FILE.anythink")""",
                27: """END every statment""",
                28: """function RETURN """,
                29: """CONTINUE""",
                30: """BREAK""",
                31: """MATH_PI
3.141592653589793""",
                32: """In many programming languages, print is a function that sends text, variables, or another object to the screen""",
                33: """In many programming languages, print is a function that sends text, variables, or another object to the screen and return""",
            }
            except:
                print("Something went wrong")
                   
            # get() method of dictionary data type returns
            # value of passed argument if it is present
            # in dictionary otherwise second argument will
            # be assigned as default value of passed argument
            return switcher.get(argument, "Option Not Found")
        
        # Driver program
        if __name__ == "__main__":
            t = Texttable()
            t.add_rows([['Keywords', 'No'], ['VAR', 1], ['INPUT', 2],['AND', 3],['INPUT_INT', 4],['OR', 5],
                         ['CLEAR', 6],['NOT', 7],['CLS', 8],['IF', 9],['IS_NUM', 10],['ELIF', 11],
                         ['IS_STR', 12],['ELSE', 13],['IS_LIST', 14],['FOR', 15],['IS_FUN', 16],['TO', 17],
                         ['APPEND', 18],['STEP', 19],['POP', 20],['WHILE', 21],['EXTEND', 22],['FUN', 23],['LEN', 24],
                         ['THEN', 25],['RUN', 26],['END', 27],['RETURN', 28],['CONTINUE', 29],['BREAK', 30],['MATH_PI', 31],['PRINT', 32],['PRINT_RET', 33]])
            print(t.draw())
            try:
                argument=int(input("Enter an Option\t"))
                print (numbers_to_strings(argument))
            
            except:
                print("Enter a Valid Option ???")
            #print("done")
        
               
    def help_Keywords(self):
        obj = MyPrompt.do_Keywords(self,0)
       
        
    def default(self, inp):
        if inp == 'x' or inp == 'q':
            return self.do_exit(inp)
 
        print("Default: {}".format(inp))
 
    
if __name__ == '__main__':
    MyPrompt().cmdloop()
