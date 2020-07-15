from app import app

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)

# import sqlalchemy as db

# # specify database configurations
# config = {
#     'host': 'localhost',
#     'port': 3306,
#     'user': 'new_user',
#     'password': 'newpassword',
#     'database': 'test_db'
# }

# db_user = config.get('user')
# db_pwd = config.get('password')
# db_host = config.get('host')
# db_port = config.get('port')
# db_name = config.get('database')
# # specify connection string
# connection_str = f'mysql+pymysql://{db_user}:{db_pwd}@{db_host}:{db_port}/{db_name}'
# # connect to database
# engine = db.create_engine(connection_str)
# connection = engine.connect()
# # pull metadata of a table
# metadata = db.MetaData()
# test_table = db.Table('test_table', metadata, autoload=True, autoload_with=engine)
# #metadata.reflect(only=['test_table'])

# print(test_table.columns.keys())
