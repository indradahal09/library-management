import json

with open("books.json") as f:
    books = json.load(f)

def view_books():
    if(len(books) == 0):
        print("books unavailable")
        return

    print("============================")
    print("          Books")
    print("============================")

    for i in books:
        
        print(f"ID: {i['id']}")
        print(f"TITLE: {i['title']}")
        print(f"AUTHOR: {i['author']}")
        print(f"CATEGORY: {i['category']}")
        if(i['available']):
            print(f"STATUS: Available")
        else:
            print("STATUS: Borrowed")

def search_book():
    usr_input = input("enter the book title")
    found = False

    for i in books:
        if usr_input.upper() == i['title'].upper():
            found = True
            print("============================")
            print("          Books")
            print("============================")
            print(f"ID: {i['id']}")
            print(f"TITLE: {i['title']}")
            print(f"AUTHOR: {i['author']}")
            print(f"CATEGORY: {i['category']}")
            if(i['available']):
                print(f"STATUS: Available")
            else:
                print("STATUS: Borrowed")
            

    if not found:
        print('book not found')

def add_book():
    usr_input = 'Yes'
    while usr_input.lower() == 'yes':
        book_title = input('enter the book title')
        author = input('enter the name of author')
        category = input('enter the category of the book')
        
        new_id = len(books) + 1
        book_dict = {
            'id' : new_id,
            'title': book_title,
            'author': author,
            'category': category,
            'available': True
        }
        books.append(book_dict)
        usr_input = input("enter yes/no")

def borrow_book():
    input_id = int(input("enter the book id"))
    found = False
    for i in books:
        if(input_id == i['id']):
            found = True
            if(i['available']):
                i['available'] = False
                print('book borrowed successfully')
            else:
                print('book borrowed already')

            break

    if not found:
        print('book id not found')

def return_book():
    input_id = int(input('enter the book id'))
    found = False
    for i in books:
        if(input_id == i['id']):
            found = True
            if(i['available']):
                print('book not borrowed yet')

            else:
                print('book returned successfully')
                i['available'] = True
            break

    if not found:
        print('book id not found')

def delete_book():
    input_id = int(input('enter the book id'))
    found = False
    for i in books:
        if(input_id == i['id']):
            found = True
            print(i['title'])
            validation = input('do you want to delete it?(yes/no)')
            if(validation.lower() == 'yes'):
                books.remove(i)
                print('book deleted successfully')
                new_id = 1
                for i in books:
                    i['id'] = new_id
                    new_id+=1
                break

    if not found:
        print('book id not found')

    

def save_changes():
    with open('books.json', 'w') as f:
        json.dump(books, f, indent=4)

print("============================")
print("      Library Management")
print("============================")

while True:
    print(f"1. View Books \n2. Search Book \n3. Add Book \n4. Borrow Book \n5. Return Book \n6. Delete Book \n7. Exit")
    try:
        user_choice = int(input('enter your choice'))
        if(user_choice == 1):
            view_books()
        elif(user_choice == 2):
            search_book()
        elif(user_choice == 3):
            add_book()
            save_changes()
        elif(user_choice == 4):
            borrow_book()
            save_changes()
        elif(user_choice == 5):
            return_book()
            save_changes()
        elif(user_choice == 6):
            delete_book()
            save_changes()
        elif(user_choice == 7):
            break
        else:
            print('enter the correct choice')

    except ValueError:
        print('enter a number')