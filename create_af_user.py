from airflow import models, settings
from airflow.contrib.auth.backends.password_auth import PasswordUser
user = PasswordUser(models.User())
user.username = 'test_user'
user.email = 'sheldonpeachesjohnson@gmail.com'
user.password = 'TestPassword24'
session = settings.Session()
session.add(user)
session.commit()
session.close()
exit()
