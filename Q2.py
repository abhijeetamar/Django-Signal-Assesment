# Question 2

# Do Django signals run in the same thread as the caller?

# Answer:
# Yes, Django signals run in the same thread as the caller by default.

# Explanation:
# Django does not create a new thread while dispatching signals. 
# The signal handler runs in the same execution context as the 
# code that triggered it.

# Proof (thread identity check):

# signals.py
import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def signal_thread_check(sender, instance, **kwargs):
    print("Signal thread ID:", threading.get_ident())

# caller code
import threading
from django.contrib.auth.models import User

print("Caller thread ID:", threading.get_ident())
User.objects.create(username="thread_test")


# Observation:
# Both the caller and the signal print the same thread ID, 
# which confirms that the signal runs in the same thread as the caller.