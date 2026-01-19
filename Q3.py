# Question 3

# By default do Django signals run in the same database transaction 
# as the caller?

# Answer:
# Yes, by default Django signals run inside the same database 
# transaction as the caller.

# Explanation:
# Signals are triggered before the database transaction is 
# committed. If the transaction is rolled back, the database 
# changes made during the signal execution are also rolled back.

# Proof (transaction rollback):

# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def transaction_signal(sender, instance, **kwargs):
    print(
        "User exists inside signal:",
        User.objects.filter(id=instance.id).exists()
    )

# caller code
from django.db import transaction
from django.contrib.auth.models import User

try:
    with transaction.atomic():
        User.objects.create(username="rollback_test")
        raise Exception("Force rollback")
except Exception:
    pass

print(
    "User exists after rollback:",
    User.objects.filter(username="rollback_test").exists()
)


# Observation:
# Inside the signal, the user exists. After the transaction
# rollback, the user no longer exists in the database. 
# This confirms that the signal was executed within the 
# same transaction.