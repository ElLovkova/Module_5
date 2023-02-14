class StringVar:

    strng = ''

    def set(self, str):
        StringVar.strng = str


    def get(self):
        print(StringVar.strng)


newstr = StringVar()
strg = input("введите строку: ")
newstr.set(strg)
newstr.get()
