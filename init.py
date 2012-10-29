"""
Excuse me Mr. Google
Author: Nick Depinet nick@csh.rit.edu
Version: 0.1 10/28/2012
Usage: Type "Excuse me Mr. Google, {query}"
"""
import sys
import webbrowser

def parseInput(question):
    """
    parse the input, return true/false and query
    """
    question = question.strip()
    ok = False
    query = ""
    try:
        if question[:22] == "Excuse me Mr. Google, ":
            ok = True
            query = question[22:]
        else:
            pass
    except IndexError:
        ok = False
    return ok, query  

def badInput():
    """
    Bad Input, tell the user and quit
    """
    print("Your input was bad, remember to ask Mr. Google nicely!")
    sys.exit(0)
    
def bingCheck(query):
    """
    Do we want Mr. Google to bing it for us?
    """
    bing = False
    query = query
    try:
        if query[:25] == "please bing this for me: ":
            bing = True
            query = query[25:]
        else:
            pass
    except IndexError:
        bing = False
    return bing, query

def main():
    """
    main command line, fancy frontend later
    """
    ok, query = parseInput(input("Please Enter your Query: "))
    if ok == False:
        badInput()
        return
    else:
        bing, query = bingCheck(query)
        if bing == True:
            webbrowser.open(''.join(["http://www.bing.com/search?q=", query]), 2)
        else:
            webbrowser.open(''.join(["http://www.google.com/search?q=", query]), 2)
    


if __name__ == "__main__":
    main()    
