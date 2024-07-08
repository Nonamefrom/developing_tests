import pytest
from first_task.code import check_age, check_auth, check_email


decline_ages = [0, 1, 16, 17]
accepted_ages = [18, 19, 124, 125]
error_ages = [-2, 100000000, -100000000]
text_ages = ['Twenty', 'Тридцать два']
empty_ages = ['', ' ']

confirm_login_data = [('admin', 'password')]
decline_login_data = [('admin', 'admin'),
                      ('password', 'password'),
                      ('admin', '132'),
                      ('999', 'password')]
int_login_data = [(555, 'password'),
                  ('admin', 666)]
empty_login_data = [
    ('', ''),
    ('admin', ''),
    ('', 'password')
]

valid_emails = [
    "user@example.com",
    "user_name@domain.com"
]
invalid_emails = [
    "example@@mail.com",
    "user.name@list.com",
    "user@domaincom",
    "userdomain.com",
    "user@domain. com"
]
empty_emails = ["", " "]


@pytest.mark.parametrize("age", decline_ages)
def test_age_declined(age):
    check = check_age(age)
    assert check == 'Доступ запрещён', f"Expected 'Доступ запрещён' but got '{check}'"


@pytest.mark.parametrize("age", accepted_ages)
def test_age_accepted(age):
    check = check_age(age)
    assert check == 'Доступ разрешён', f"Expected 'Доступ разрешён' but got '{check}'"


@pytest.mark.parametrize("age", error_ages)
def test_age_error(age):
    check = check_age(age)
    assert check == 'Введено некорректное значение возраста', \
        f"Expected 'Введено некорректное значение возраста' but got '{check}'"


@pytest.mark.parametrize("age", text_ages)
def test_age_text_format(age):
    check = check_age(age)
    assert check == 'Введен текст', f"Expected 'Введен текст' but got '{check}'"


@pytest.mark.parametrize("age", empty_ages)
def test_age_empty(age):
    check = check_age(age)
    assert check == 'Возраст не должен быть пустым', f"Expected 'Возраст не должен быть пустым' but got '{check}'"


@pytest.mark.parametrize("login, password", confirm_login_data)
def test_auth_accepted(login, password):
    check = check_auth(login, password)
    assert check == 'Добро пожаловать', f"Expected 'Добро пожаловать' but got '{check}'"


@pytest.mark.parametrize("login, password", decline_login_data)
def test_auth_declined(login, password):
    check = check_auth(login, password)
    assert check == 'Доступ ограничен', f"Expected 'Доступ ограничен' but got '{check}'"


@pytest.mark.parametrize("login, password", int_login_data)
def test_auth_with_int(login, password):
    check = check_auth(login, password)
    assert check == 'Данные авторизации получены форматом int', \
        f"Expected 'Данные авторизации получены форматом int' but got '{check}'"


@pytest.mark.parametrize("login, password", empty_login_data)
def test_auth_empty(login, password):
    check = check_auth(login, password)
    assert check == 'Логин и пароль не должны быть пустыми', \
        f"Expected 'Логин и пароль не должны быть пустыми' but got '{check}'"


@pytest.mark.parametrize("email", valid_emails)
def test_check_email_valid(email):
    assert check_email(email) == True, f"Expected True but got False for email: {email}"

@pytest.mark.parametrize("email", invalid_emails)
def test_check_email_invalid(email):
    assert check_email(email) == False, f"Expected False but got True for email: {email}"

@pytest.mark.parametrize("email", empty_emails)
def test_check_email_empty(email):
    assert check_email(email) == False, f"Expected False but got True for email: {email}"
