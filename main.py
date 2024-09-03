contact_list = []

def add():
    name = input("Insira o nome do novo contato: ")
    phone_number = input("Insira o número de telefone do novo contato: ")
    email = input("Insira o email do novo contato: ")
    is_favorite = input("O novo contato é um de seus favoritos? (s/n): ")

    if is_favorite != "s" and is_favorite != "n":
        print("Dados inválidos!")
        return

    new_contact = {
        "name": name,
        "phone_number": phone_number,
        "email": email,
        "is_favorite": True if is_favorite == "s" else False
    }

    contact_list.append(new_contact)

    return

def view():
    for index, contact in enumerate(contact_list):
        print(f"{index + 1}: ("
              f"\n  Nome: {contact["name"]}"
              f"\n  Telefone: {contact["phone_number"]}"
              f"\n  Email: {contact["email"]}"
              f"\n  Favorito: {"✓" if contact["is_favorite"] else "x"}"
              f"\n)")
    return

def edit():
    contact_number = int(input("Insira o número do contato para editar: "))
    contact_index = contact_number - 1

    if contact_index < 1 or contact_index > len(contact_list):
        print("Número de contato inválido!")
        return

    name = input("Insira o nome do contato: ")
    phone_number = input("Insira o número de telefone contato: ")
    email = input("Insira o email do contato: ")
    is_favorite = input("O contato é um de seus favoritos? (s/n): ")

    new_contact = {
        "name": name,
        "phone_number": phone_number,
        "email": email,
        "is_favorite": True if is_favorite == "s" else False
    }

    contact_list[contact_index] = new_contact

    return

def switch_favorite():
    contact_number = int(input("Insira o número do contato para marcar/desmarcar como favorito: "))
    contact_index = contact_number - 1

    if contact_index < 1 or contact_index > len(contact_list):
        print("Número de contato inválido!")
        return

    contact_list[contact_index]["is_favorite"] = not contact_list[contact_index]["is_favorite"]

    return

def view_favorites():
    for index, contact in enumerate(contact_list):
        if contact["is_favorite"]:
            print(f"{index + 1}: ("
                  f"\n  Nome: {contact["name"]}"
                  f"\n  Telefone: {contact["phone_number"]}"
                  f"\n  Email: {contact["email"]}"
                  f"\n)")
    return

def delete():
    contact_number = int(input("Insira o número do contato para remover: "))
    contact_index = contact_number - 1

    if contact_index < 1 or contact_index > len(contact_list):
        print("Número de contato inválido!")
        return

    del contact_list[contact_index]
    return

while True:
    print("1. Adicionar contato")
    print("2. Ver contatos")
    print("3. Editar contato")
    print("4. Marcar/desmarcar contato como favorito")
    print("5. Ver contatos favoritos")
    print("6. Apagar contato")
    print("7. Sair")

    selected_option = input("Insira a opção desejada: ")

    if selected_option == "7":
        print("Saindo...")
        break

    options = {
        "1": add,
        "2": view,
        "3": edit,
        "4": switch_favorite,
        "5": view_favorites,
        "6": delete
    }

    target_function = options[selected_option]

    target_function()
