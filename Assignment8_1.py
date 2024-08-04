class BookStore:
    NoofBooks = 0

    def __init__(self):
        self.name = '\0'
        self.Author = '\0'

        print("Enter name of book :")
        self.name = str(input())

        print("Enter author name :")
        self.Author = str(input())

        BookStore.NoofBooks += 1

    def Display(self):
        print("Name of book is :",self.name,"published by :",self.Author,":",BookStore.NoofBooks)

def main():
    obj1 = BookStore()
    obj1.Display()

    obj2 = BookStore()
    obj2.Display()
if __name__ == "__main__":
    main()