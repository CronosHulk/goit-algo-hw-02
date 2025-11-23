import queue
import time
import random


request_queue = queue.Queue()

request_id_counter = 0


def generate_request():
    global request_id_counter
    request_id_counter += 1
    request_data = f"Заявка #{request_id_counter}"
    request_queue.put(request_data)

    print(f"Створено та додано до черги: {request_data}")


def process_request():
    if not request_queue.empty():
        request_to_process = request_queue.get()

        print(f"Обробка: {request_to_process}")

        time.sleep(random.uniform(0.5, 1.5))

        print(f"Завершено обробку: {request_to_process}")
    else:
        print("Черга пуста. Немає заявок для обробки.")


def main():
    print("Сервісний центр розпочав роботу.")
    print("Натисніть Enter, щоб генерувати заявки, або введіть 'exit'.")

    try:
        while True:
            user_input = input()
            if user_input.lower() == 'exit':
                print("Завершення роботи сервісного центру.")
                break

            generate_request()

            time.sleep(random.uniform(0.2, 0.8))

            process_request()

    except KeyboardInterrupt:
        print("\nПрограму перервано користувачем. Завершення роботи.")


if __name__ == "__main__":
    main()
