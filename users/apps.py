from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    # we have to import our signals iside of ready function of app.py file
    def ready(self):
        import users.signals
