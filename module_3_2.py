def send_email(message, recipient='university@mail.ru', sender='university.help@gmail.com'):
    if sender == recipient:
        print(f'Нельзя отправить письмо самому себе!')
    elif '@' not in recipient and sender:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif sender.endswith('.com' or '.ru' or '.net') == -1:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif recipient.endswith('.com' or '.ru' or '.net') == -1:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif sender != 'university.help@gmail.com':
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
    else:
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')

send_email("Это сообщение для проверки связи", "vasyok1337@gmail.com")
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru',
           'urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', 'urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', 'urban.teacher@mail.ru')

