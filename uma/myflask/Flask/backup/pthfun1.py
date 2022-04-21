
def gtstdnt(fname,sname):
    print("select * from students where name is " + fname +  " and surname is "  + sname )


fname = input('enter your name:')
sname = input('enter your surname:')
gtstdnt(fname,sname)
