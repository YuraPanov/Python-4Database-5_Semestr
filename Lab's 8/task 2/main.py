# -*- coding: utf-8 -*-
from sqlalchemy import ForeignKey, create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

# Объект Engine, отвечающий за все соединения
engine = create_engine("sqlite:///delivery.db", echo=True)

# Базовый класс
Base = declarative_base()


# Определение таблиц
class Courier(Base):
    __tablename__ = 'couriers'

    id = Column(Integer, primary_key=True)
    surname = Column(String)
    name = Column(String)
    second_name = Column(String)
    passport_number = Column(String)
    date_of_birth = Column(String)
    date_of_employment = Column(String)
    clock_in_time = Column(String)
    clock_out_time = Column(String)
    city = Column(String)
    street = Column(String)
    house_number = Column(Integer)
    apartment_number = Column(Integer)
    phone_number = Column(String)


class Transport(Base):
    __tablename__ = 'transport'

    number = Column(Integer, primary_key=True)
    model = Column(String)
    date_of_registration = Column(String)
    colour = Column(String)


class Sender(Base):
    __tablename__ = 'senders'

    id = Column(Integer, primary_key=True)
    surname = Column(String)
    name = Column(String)
    second_name = Column(String)
    date_of_birth = Column(String)
    index = Column(Integer)
    city = Column(String)
    street = Column(String)
    house_number = Column(Integer)
    apartment_number = Column(Integer)
    phone_number = Column(String)


class Receiver(Base):
    __tablename__ = 'receivers'

    id = Column(Integer, primary_key=True)
    surname = Column(String)
    name = Column(String)
    second_name = Column(String)
    date_of_birth = Column(String)
    index = Column(Integer)
    city = Column(String)
    street = Column(String)
    house_number = Column(Integer)
    apartment_number = Column(Integer)
    phone_number = Column(String)


class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)

    id_sender = Column(Integer, ForeignKey('senders.id'))
    sender = relationship('Sender')

    id_receiver = Column(Integer, ForeignKey('receivers.id'))
    receiver = relationship('Receiver')

    date_of_order = Column(String)
    date_of_delivery = Column(String)
    price_of_delivery = Column(Float)

    id_courier = Column(Integer, ForeignKey('couriers.id'))
    courier = relationship('Courier')

    transport_number = Column(Integer, ForeignKey('transport.number'))
    transport = relationship('Transport')


# Метаданные
Base.metadata.create_all(engine)

# Сессия
Session = sessionmaker(bind=engine)
session = Session()

# Создание новых записей
sender1 = Sender(id=1, surname='Petrov', name='Petr', second_name='Sergeevich', date_of_birth='10.10.1985',
                 index=117042, city='Kazan', street='Lenina', house_number=25, apartment_number=3,
                 phone_number='+7123456789')
session.add(sender1)

sender2 = Sender(id=2, surname='Taylor', name='Chris', second_name='Michael', date_of_birth='05.06.1993', index=900001,
                 city='San Francisco', street='Market Street', house_number=50, apartment_number=21,
                 phone_number='1234567890')
session.add(sender2)

receiver1 = Receiver(id=1, surname='Voronov', name='Igor', second_name='Nikolaevich', date_of_birth='12.12.1990',
                     index=450123, city='Novosibirsk', street='Sverdlova', house_number=44, apartment_number=101,
                     phone_number='+7987654321')
session.add(receiver1)

receiver2 = Receiver(id=2, surname='Johnson', name='Emily', second_name='Grace', date_of_birth='15.09.1988',
                     index=606303, city='Chicago', street='State Street', house_number=10, apartment_number=405,
                     phone_number='555123456')
session.add(receiver2)

session.commit()

order1 = Order(id=1, id_sender=2, id_receiver=1, date_of_order='25.11.2024', date_of_delivery='30.11.2024',
               price_of_delivery=300.50, id_courier=1, transport_number=74321)
session.add(order1)

order2 = Order(id=2, id_sender=1, id_receiver=2, date_of_order='20.11.2024', date_of_delivery='28.11.2024',
               price_of_delivery=450.75, id_courier=1, transport_number=74321)
session.add(order2)

session.commit()
