a = ["1", "2", "3","4"]

for i in a:
    f = open("a"+i+".txt","w")
    #f.write('Write here anything.')
    f.write("This is "+i+".")
