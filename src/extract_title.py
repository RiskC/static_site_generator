


def extract_title(markdown):
    splitter = markdown.split("\n")
   
    for s in splitter:
        if s.startswith("# "):
            return s.removeprefix("# ")
    raise ValueError("no h1 header")





# open -> open file and return a corresponding file object oepn(file, mode = r)
                  #  with open(file, r) as f:
                   #     text = f.read()
# .read() -> a method that reads a file where the file is f and the object being read -> f.read()
# .write() -> writes the contents of a string to the file, returning the number of characters written -> f.write(string)
# .close() -> f.close() closes the file if you arent using with loop to use the open method 
# .replace() -> str.replace(old, new) 
# os.path.dirname(path)-> return the directory name of pathname path
# os.makedirs(name) -> recursive directory creation function, like mkdir() but makes all intermediate level directories needed to contain the leaf directory 
# .startswith() -> str.startswith(prefix , start, end)
# .split() -> str.split(separator)




