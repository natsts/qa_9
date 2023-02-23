from dataclasses import dataclass


@dataclass
class User:
    name: str
    last_name: str
    email: str
    phone: str
    address: str
    month: int
    year: int
    day: int
    gender: str
    subject: str
    hobby: str
    image: str
    state: str
    city: str


test_user = User(
    name='Test',
    last_name='Testovych',
    email='test123@mail.ru',
    phone='9617778558',
    address='Moscow',
    subject='English',
    month=5,
    year=1996,
    day=20,
    gender='Female',
    hobby='Reading',
    image='cat.jpg',
    state='NCR',
    city='Delhi')
