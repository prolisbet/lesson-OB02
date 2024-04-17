# Разработай систему управления учетными записями пользователей для небольшой компании.
# Компания разделяет сотрудников на обычных работников и администраторов.
# У каждого сотрудника есть уникальный идентификатор (ID), имя и уровень доступа.
# Администраторы, помимо обычных данных пользователей, имеют дополнительный уровень доступа
# и могут добавлять или удалять пользователя из системы.
#
# Требования:
#
# 1.Класс `User*: Этот класс должен инкапсулировать данные о пользователе:
# ID, имя и уровень доступа ('user' для обычных сотрудников).

# 2.Класс `Admin`: Этот класс должен наследоваться от класса `User`.
# Добавь дополнительный атрибут уровня доступа, специфичный для администраторов ('admin').
# Класс должен также содержать методы `add_user` и `remove_user`, которые позволяют добавлять
# и удалять пользователей из списка (представь, что это просто список экземпляров `User`).
#
# 3.Инкапсуляция данных: Убедись, что атрибуты классов защищены от прямого доступа
# и модификации снаружи. Предоставь доступ к необходимым атрибутам через методы
# (например, get и set методы).


user_list = []


class User():
    def __init__(self, user_id, name):
        self.__id = user_id
        self.__name = name
        self.__access_level = 'user'
        # user_list.append(self) - не нужно, т. к. юзер добавляется в список вручную админом

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_access(self):
        return self.__access_level


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self.__access_level = 'admin'

    def add_user(self, user):
        user_list.append(user)
        print(f'Администратор добавил в список пользователей: {user.get_name()}.')

    def remove_user(self, user):
        user_list.remove(user)
        print(f'Администратор удалил из списка пользователей: {user.get_name()}.')


def show_user_list(list):
    for i, user in enumerate(list, start=1):
        print(f'{i}. {user.get_name()}')


admin1 = Admin('8976341', 'Иванов Дмитрий Евгеньевич')
user1 = User('5489230', 'Павлова Софья Сергеевна')
user2 = User('4312895', 'Афанасьев Иван Георгиевич')
user3 = User('1245783', 'Новикова Наталья Олеговна')
user4 = User('9034187', 'Лопаткин Даниил Игоревич')

admin1.add_user(user1)
admin1.add_user(user2)
admin1.add_user(user3)
admin1.add_user(user4)

show_user_list(user_list)

admin1.remove_user(user2)

show_user_list(user_list)


try:
    user1.__id
except AttributeError:
    print(None)

try:
    user1.__name
except AttributeError:
    print(None)

try:
    user1.__access_level
except AttributeError:
    print(None)

print(f'Уникальный идентификатор (ID) - {user1.get_id()}')
print(f'Имя пользователя - {user1.get_name()}')
print(f'Уровень доступа - {user1.get_access()}')
