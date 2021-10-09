class Tree:
    class Node:
        def __init__(self,key):
            self.key=key
            self.left= None
            self.right= None

    def __init__(self, data):
        self.data= data
        self.root= self.buildTree(data,0)

    def buildTree(self, data, i):
        if i >= len(data): return None
        next = self.Node(data[i]);
        next.left = self.buildTree(data, 2 * i + 1)
        next.right = self.buildTree(data, 2 * i + 2)
        return next

    def printTree(self,node,level):
        if node != None:
            self.printTree(node.left, level + 1)
            print(' ' * 4 * level + '->', node.key)
            self.printTree(node.right, level + 1)

    def printFullTree(self):
        print("_"*30)
        print(" : TREE :")
        self.printTree(self.root,0)
        print("_"*30)

def readMorseTree(currentNode,code,x):
    a=""
    if currentNode: 
        if currentNode.left:
            a= x+ "."
            code[currentNode.left.key]= a
            code= readMorseTree(currentNode.left,code,a)
        if currentNode.right:
            a= x+ "-"
            code[currentNode.right.key]= a
            code= readMorseTree(currentNode.right,code,a)
    return code

def getMorseCode(tree):
    return readMorseTree(tree.root,{},"")

def getMorseTree():
    letters= "0ETIANMSURWDKGOHVF L PJBXCYZQ"
    tree= Tree(list(letters))
    return tree

def convetToMorse(code,msg):
    morse=""
    msg= list(msg.upper())
    for i in msg:
        if i==" ":
            morse=morse+"|"
        else:
            try:
                morse= morse + code[i] + "/"
            except:
                morse= morse + "*" + "/"
    return morse

def printCode(code):
    def line(c):
        return "| '{0}' : {1}{2}".format( c, code[c], " "*(10-len(code[c])))
    
    for i in range(65,87,3) :
        print(line(chr(i))+line(chr(i+1))+line(chr(i+2))+"|")
    print(line(chr(89))+line(chr(90)))

if __name__ == "__main__":
    title= "MORSE CODE WITH BINARY TREE"
    print("_"*50)
    print("\t"+title)
    print("\t"+"-"*len(title))
    print("\n | Generating Morse Code Binary Tree")
    tree= getMorseTree()
    print(" | Done generating tree")
    print("\n\n | Generating morse code")
    code= getMorseCode(tree)
    print(" | Done generating morse code")
    choice=1
    while(choice):
        print("\n"+"-"*20)
        print(" MENU")
        print(" 1. Show binary tree\t2. Show morse code")
        print(" 3. Convert text to morse code\t4. Exit")
        choice= input(" Enter choice: ")
        try :
            choice=int(choice)
        except:
            print("\n Invalid input. Try again.")
            continue
        if choice ==1 :
            print("\n\tMORSE CODE BINARY TREE")
            print("\t-----------------------")
            tree.printFullTree()
        elif choice==2 :
            print("\n\tMORSE CODE")
            print("\t----------")
            printCode(code)
        elif choice ==3 :
            print("\n\tCONVERT TO MORSE CODE")
            print("\t---------------------")
            msg= input(" Enter message: ")
            morse=convetToMorse(code,msg)
            print(" Morse Code: " + morse)
        elif choice ==4:
            print("\n Exiting.")
            break
        else:
            print("\n Invalid input.")
    print("_"*50)