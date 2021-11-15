
# Copyright AGRVibes. 
# This script is ued to generate source and header files for c and c++.
# It may be extended to other as well. The script generates a class files.
# Opionally it will be added to support from xml file generation.
# For example you will specify in a xml file the type of file and describe
# the functions or classes and methods with data fields.
#
# How to run?
# python generate.py {className} {language}
#
# If you type python generate.py Horse c++ 
# It will make 2 files horse.cpp and horse.h with default class members.

import sys

policy = "<--AGRVibes-->"


def languageExtension(language):
    extensions = []
    match language:
        case "c++":
            extensions.append("cpp")
            extensions.append("h")
            return extensions
        case "c":
            extensions.append("cc")
            extensions.append("h")
        case _:
            return extensions

def cHeaderFile(className):
    headerCode = ""
    headerCode += "/////////////////////////////////////////////////////////////////////////\n" +     \
                   "///////// " + policy + "\n" +                                                     \
                   "///////// @file: " + className.lower() + ".h\n" +                                 \
                   "/////////////////////////////////////////////////////////////////////////\n"
    headerCode += "\n"
    headerCode += "#ifndef " + className.upper() + "_" + "H\n"
    headerCode += "#define " + className.upper() + "_" + "H\n\n"

    headerCode += "class " + className + " {\n"

    headerCode += "\tpublic:\n"
    headerCode += "\t\t" + className + "();\n"
    headerCode += "\t\t~" + className + "();\n"
    headerCode += "\tprivate:\n"

    headerCode += "};\n"

    headerCode += "\n#endif // " + className.upper() + "_" + "H\n"
    return headerCode

def cppHeaderFile(className):
    headerCode = ""
    headerCode += "/////////////////////////////////////////////////////////////////////////\n" +     \
                   "///////// " + policy + "\n" +                                                     \
                   "///////// @file: " + className.lower() + ".h\n" +                                 \
                   "/////////////////////////////////////////////////////////////////////////\n"
    headerCode += "\n"
    headerCode += "#pragma once\n\n"

    headerCode += "class " + className + " {\n"

    headerCode += "\tpublic:\n"
    headerCode += "\t\t" + className + "();\n"
    headerCode += "\t\t~" + className + "();\n"
    headerCode += "\tprivate:\n"

    headerCode += "};\n"

    return headerCode


def cppSourceFile(className):
    sourceCode = ""
    sourceCode += policy + "\n"

    sourceCode += "/////////////////////////////////////////////////////////////////////////\n" +     \
                   "/// " + policy + "\n" +                                                     \
                   "/// @file: " + className.lower() + ".cpp\n" +                               \
                   "/////////////////////////////////////////////////////////////////////////\n"
    sourceCode += "\n"
    sourceCode += "#include \"" + className.lower() + ".h\"\n\n"

    sourceCode += "/////////////////////////////////////////////////////////////////////////\n" + \
                   "/// Constructor: " + className + "()\n" +                                     \
                   "/////////////////////////////////////////////////////////////////////////\n"
    sourceCode += className + "::" + className + "() {}\n\n"

    sourceCode += "/////////////////////////////////////////////////////////////////////////\n" + \
                   "/// Destructor: ~" + className + "()    \n" +                                 \
                   "/////////////////////////////////////////////////////////////////////////\n" 
    sourceCode += className + "::~" + className + "() {}\n\n"


    return sourceCode

def generateClassFileData(className, extension):
    match extension:
        case "h":
            return cppHeaderFile(className)
        case "cpp":
            return cppSourceFile(className)
        case _:
            print("Error: Not a valid extension: %s", extension)
            

#__main__
if len(sys.argv) != 3:
    sys.exit("Error: Provide name for class and programming language.")    

className = sys.argv[1]
language = sys.argv[2]

languageExtension = languageExtension(language)

if (len(languageExtension) == 0):
    sys.exit("Error: No valid extensions returned.")


for ext in languageExtension:
    fileName = className.lower() + "." + ext
    f = open(fileName,mode='w')
    f.write(generateClassFileData(className, ext))
    f.close()

sys.exit(0)