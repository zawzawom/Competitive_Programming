
def main():
    testCase = int(input("\n"))
    name = list()
    anotherlist = list()
    for i in range(testCase*2):
        name.append(input())
        anotherlist.append((name[i][9:]))
    for i in range(testCase):
        print("Uh! ",anotherlist[i+i+1],'-',anotherlist[i+i],"!",sep='')
    return 0
if __name__ == "__main__":
    main()