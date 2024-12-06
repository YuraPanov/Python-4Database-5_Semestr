import sqlite3 as sq


def main():

    conn = sq.connect("delivery.db")

    cur = conn.cursor()

    cur.execute("""
                CREATE TABLE IF NOT EXISTS couriers(
                id INT PRIMARY KEY,
                surname TEXT,
                name TEXT,
                second_name TEXT,
                passport_number TEXT,
                date_of_birth TEXT,
                date_of_employment TEXT,
                clock_in_time TEXT,
                clock_out_time TEXT,
                city TEXT,
                street TEXT,
                house_number INT,
                apartment_number INT,
                phone_number TEXT
                );
                """)

    conn.commit()

    cur.execute("""
                CREATE TABLE IF NOT EXISTS transport(
                number INT PRIMARY KEY,
                model TEXT,
                date_of_registration TEXT,
                colour TEXT
                );
                """)

    conn.commit()

    cur.execute("""
                INSERT INTO couriers(id, surname, name, second_name, passport_number, date_of_birth, date_of_employment, clock_in_time, clock_out_time, city, street, house_number, apartment_number, phone_number)
                VALUES('2', 'Smith', 'Ivan', 'Alexander', '123456', '15.03.1990', '10.01.2020', '08:00', '16:00', 'New York', '5th Avenue', '102', '12', '+123456789');
                """)

    conn.commit()

    cur.execute("""
                INSERT INTO transport(number, model, date_of_registration, colour)
                VALUES('74321', 'Cyclone', '15.07.2022', 'blue');
                """)

    conn.commit()


    cur.execute("""
                UPDATE transport SET colour = 'green' WHERE number = 74321; 
                """)

    conn.commit()

    conn.close()


if __name__ == "__main__":
    main()
