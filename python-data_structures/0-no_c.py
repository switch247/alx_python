def no_c(my_string):
    new =''
    for i in my_string:
        if i.lower() =='c':
            continue
        new+=i
    return new    

if __name__=="__main__":
    import sys
    print(no_c("testh"))
