my_string = """Strings are amongst the most popular data types in Python.
We can create the strings by enclosing characters in quotes.
Python treats single quotes the same as double quotes."""

m2 = my_string.upper()
print("1)",m2.count("STRING"))


def count_words(strn):
    words = strn.replace(".","").split()
    t1,t2=0,0
    for i in words:
        if i.endswith("ON"):
            t1 = t1+1
        if "ON" in i[1:len(i)-1]:
            t2 = t2+1
    print("2)",t1)
    print("3)",t2)

count_words(m2)
