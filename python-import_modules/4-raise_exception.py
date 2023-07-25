def raise_exception():
   try:
     raise NameError('HiThere')
   except NameError:
        print('An exception flew by!')
        raise
if __name__== "__main__":
    raise_exception()
