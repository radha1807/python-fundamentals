def get_user():
    name = input("enter name: ")
    age = input("enter age : ")
    return {"name": name, "age": age}

def display_user(user):
    print("\nUser Info:")
    print(f"Name: {user['name']}")
    print(f"Age: {user['age']}")


def main():
    user = get_user()
    display_user(user)


if __name__ == "__main__":
    main()
