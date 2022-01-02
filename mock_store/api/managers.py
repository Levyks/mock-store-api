from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """
    Manager for user profiles
    """

    def create_user(self, email, first_name, last_name, password=None):
        """
        Create a new user profile
        """
        if not email:
            raise ValueError('User must have an email address')

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, first_name, last_name, password):
        """
        Create and save a new superuser with given details
        """
        user = self.create_user(email, first_name, last_name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user
