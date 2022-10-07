class Person:
    def __init__(self, name, surname, phone_dict):
        self.name = name
        self.surname = surname
        self.phone_dict = phone_dict

    def get_phone(self):
        return self.phone_dict.get('private')

    def get_name(self):
        return f'{self.name} {self.surname}'

    def get_work_phone(self):
        return self.phone_dict.get('work')

    def get_sms_text(self):
        return f'Уважаемы {self.name} {self.surname}! Примите участие в нашем беспроигрышном конкурсе для физ. лиц'


class Company:
    def __init__(self, name_company, type_company, phone_dict, *person_list):
        self.name = name_company
        self.type = type_company
        self.phone_dict = phone_dict
        self.person = person_list

    def get_phone(self):
        if self.phone_dict.get('contact') is not None:
            return self.phone_dict.get('contact')
        else:
            for i in self.person:
                if i.get_work_phone() is not None:
                    return i.get_work_phone()
            return None

    def get_name(self):
        return f'{self.name}'

    def get_sms_text(self):
        return f'Для компании {self.name} есть суперпредложение! Примите участие в ' \
               f'нашем беспроигрышном конкурсе для {self.type}'


def send_sms(*args):
    lst = args
    for i in lst:
        if type(i) is Person or type(i) is Company:
            if i.get_phone() is not None:
                print(
                    f'Отправлено СМС на номер {i.get_phone()} с текстом {i.get_sms_text()}')
            else:
                print(f'Не удалось отправить сообщение абоненту: {i.get_name()}')


person1 = Person('Иван', 'Иванов', {'private' : 123, 'work' : 456})
person2 = Person('Иван', 'Петров', {'private' : 123})
person3 = Person('Иван', 'Сидоров', {'work' : 456})
person4 = Person('Джохон', 'Дое', {})
company1 = Company('Beel', 'ООО', {'contact' : 111}, person3, person4)
company2 = Company('Ceel', 'АО', {'non_contact' : 222}, person2, person3)
company3 = Company('Deel', 'Ltd', {'non_contact' : 333}, person2, person4)
print()
send_sms(person1, person2, person3, person4, company1, company2, company3)  


person1 = Person('Степан', 'Джобсов', {'private' : 555})
person2 = Person('Боря', 'Гейтсов', {'private' : 777, 'work' : 888})
person3 = Person('Семен', 'Возняцкий', {'work' : 789})
person4 = Person('Леонид', 'Торвальдсон', {})
company1 = Company('Яблочный комбинат', 'ООО', {'contact' : 111}, person3, person4)
company2 = Company('ПластОкно', 'АО', {'non_contact' : 222}, person2)
company3 = Company('Пингвинья ферма', 'Ltd', {'non_contact' : 333}, person4)
print()
send_sms(person1, person2, person3, person4, company1, company2, company3)  