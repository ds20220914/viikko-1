from entities.user import User
from database_connection import get_database_connection
from database_connection import get_course_connection



class UserRepository:
	def __init__(self, connection1,connection2):

		self._connection1=connection1
		self._connection2=connection2

	def create(self, User):
		 
		db=self._connection1.cursor()
		db.execute("INSERT INTO User (User_name,password,role_number) values (?,?,?)",(User.username,User.password,User.role_number))
		self._connection1.commit()
		return User
	def find_all(self):
		db=self._connection1.cursor()
		lista=db.execute("SELECT * FROM User ").fetchall()
		return list(lista)
		
	
		
user_repository=UserRepository(get_database_connection(),get_course_connection())

