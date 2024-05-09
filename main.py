from app.note_manager import NoteManager


def main():
    filename = "notes.json"  # Имя файла для сохранения заметок
    note_manager = NoteManager(filename)

    while True:
        print("\nВыберите команду:")
        print("1. Вывести список всех заметок")
        print("2. Добавить новую заметку")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Выйти из приложения")

        choice = input("Введите номер команды: ")

        if choice == "1":
            print("\nСписок всех заметок:")
            for note in note_manager.get_all_notes():
                print(f"{note.note_id}. {note.title} - {note.timestamp}")

        elif choice == "2":
            title = input("Введите заголовок заметки: ")
            body = input("Введите тело заметки: ")
            note_manager.add_note(title, body)
            print("Заметка успешно добавлена.")

        elif choice == "3":
            note_id = int(input("Введите ID заметки для редактирования: "))
            title = input("Введите новый заголовок заметки: ")
            body = input("Введите новое тело заметки: ")
            note_manager.edit_note(note_id, title, body)
            print("Заметка успешно отредактирована.")

        elif choice == "4":
            note_id = int(input("Введите ID заметки для удаления: "))
            note_manager.delete_note(note_id)
            print("Заметка успешно удалена.")

        elif choice == "5":
            print("Выход из приложения.")
            break

        else:
            print("Некорректный ввод. Попробуйте еще раз.")


if __name__ == "__main__":
    main()

