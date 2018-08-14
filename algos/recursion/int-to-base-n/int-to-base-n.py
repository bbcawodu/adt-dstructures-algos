def convert_int_to_variable_base_string(n,base):
   baseDigitsString = "0123456789ABCDEF"
   if n < base:
      return baseDigitsString[n]
   else:
      return convert_int_to_variable_base_string(n//base,base) + baseDigitsString[n%base]


def main():
    pass


"""
When the interpreter reads a python file, it executes all the code found in it.
Before executing the code, the interpreter defines some special variables(environment, etc.)
If the python interpreter is running the python file as the main program(eg. when being called from the command line),
It sets the __name__ variable to "__main__". If the python file is being imported from another module, __name__ will
be set to the module's name.
By doing the __main__ check, you can control when parts of code execute.
"""
if __name__ == "__main__":
    main()

