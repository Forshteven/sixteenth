def send_email(message, recipient, sender = "university.help@gmail.com"):
    a = "@"
    b = ".com"
    c = ".ru"
    d = ".net"
    e = sender
    f = recipient
    if e.find(a) == -1 or f.find(a) == -1:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}.')
    elif e.find(b) == -1 and e.find(c) == -1 and e.find(d) == -1:
            print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}.')
    elif f.find(b) == -1 and f.find(c) == -1 and f.find(d) == -1:
            print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}.')
    elif sender == recipient:
        print(f"Нельзя отправить письмо самому себе!")
    elif sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")


send_email("Это сообщение для проверки связи", "vasyok1337@gmail.com")
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru',
           'urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', 'urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', 'urban.teacher@mail.ru')

