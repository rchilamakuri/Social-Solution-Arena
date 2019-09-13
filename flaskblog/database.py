from flaskblog import db
from flaskblog.Models import User
user = User.query.first()



print(user)

