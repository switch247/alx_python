def multiple_returns(sentence):
    if not sentence:
        return (0,None)
    else:
        return (len(sentence),sentence[0])
    
if __name__ == "__main__":
   print( multiple_returns("hello") )