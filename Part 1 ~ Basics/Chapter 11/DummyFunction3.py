def GetFormattedName(First,Last,Middle=""):
    if Middle:    
        FullName=First+" "+Middle+" "+Last
    else:
        FullName=First+" "+Last
    return FullName.title()