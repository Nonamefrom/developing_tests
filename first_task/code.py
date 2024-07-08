# Задание «Проверка возраста»
def check_age(age):
    if isinstance(age, str):
        if not age.strip():
            return 'Возраст не должен быть пустым'
        return 'Введен текст'
    elif isinstance(age, int):
        if 18 <= age <= 125:
            return 'Доступ разрешён'
        elif 0 <= age < 18:
            return 'Доступ запрещён'
        else:
            return 'Введено некорректное значение возраста'
    else:
        return 'Введено некорректное значение возраста'


# Задание «Проверка логина и пароля»
def check_auth(login: str, password: str):
    if isinstance(login, str) and isinstance(password, str):
        if not login or not password:
            return 'Логин и пароль не должны быть пустыми'
        elif login == 'admin' and password == 'password':
            return 'Добро пожаловать'
        else:
            return 'Доступ ограничен'
    else:
        return 'Данные авторизации получены форматом int'


# Задание «Проверка логина и пароля»
def check_email(email: str) -> bool:
    if not email:  # Проверка на пустое значение
        return False
    if email.count("@") == 1 and email.count(".") == 1:
        if " " in email:
            return False
        else:
            return True
    else:
        return False
