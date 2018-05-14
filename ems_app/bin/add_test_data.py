import ems_app
from ems_app.data.dbsession import DbSessionFactory


def main():
    ems_app.init_db(None)
    add_test_data()


def add_test_data():
    pass


if __name__ == '__main__':
    main()