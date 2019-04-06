from django.contrib.auth.models import User

user = User.objects.create_user("alice", "alice@gmail.com", "alicepass12345")

user.first_name = "Alice"
user.is_active = False

user.save()
