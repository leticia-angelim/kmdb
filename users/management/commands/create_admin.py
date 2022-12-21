from django.core.management.base import BaseCommand, CommandError
from users.models import User


class Command(BaseCommand):
    help = "Create admin user"

    def add_arguments(self, parser):
        parser.add_argument(
            "--username",
            type=str,
            help="Define a username prefix",
        )

        parser.add_argument(
            "--email",
            type=str,
            help="Define a email prefix",
        )

        parser.add_argument(
            "--password",
            type=str,
            help="Define a password prefix",
        )

    def handle(self, *args, **kwargs):
        username_prefix = kwargs["username"]
        email_prefix = kwargs["email"]
        password_prefix = kwargs["password"]

        username = username_prefix if username_prefix else "admin"
        email = email_prefix if email_prefix else f"{username}@example.com"
        password = password_prefix if password_prefix else "admin1234"

        username_exists = User.objects.filter(username=username)
        email_exists = User.objects.filter(email=email)

        if username_exists:
            raise CommandError(f"Username `{username}` already taken.")

        if email_exists:
            raise CommandError(f"Email `{email}` already taken.")

        User.objects.create_superuser(username=username, email=email, password=password)

        self.stdout.write(self.style.SUCCESS(f"Admin `{username}` successfully created!"))
