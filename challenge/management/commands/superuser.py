from django.contrib.auth import get_user_model

User = get_user_model();
user = User.objects.create_superuser('admin', 'admin@domain.com', 'password')

