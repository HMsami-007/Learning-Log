FilePath=r'E:\Python Crash Course\Sample Texts\SampleText.txt'
with open(FilePath) as File:
    Contents=File.read()
    print(Contents.rstrip())


##Add an r prefix before your string to fix the SyntaxWarning: invalid escape sequence warning.In Python, a backslash (\) inside standard strings is interpreted as the start of an escape sequence (like \n or \t). Because \P and \S are not valid escape sequences, Python 3.12+ triggers a warning.
##Option 1: Use a Raw String (Recommended)Add an r directly before the opening quotation mark to tell Python to treat backslashes as literal characters.
##Option 2: Use Forward SlashesPython natively accepts forward slashes for file paths on Windows.
##Option 3: Double the BackslashesEscape each backslash with a second backslash.
