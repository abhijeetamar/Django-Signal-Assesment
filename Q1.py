# Question 1

# By default are Django signals executed synchronously or asynchronously?

# Answer:
# By default, Django signals are executed synchronously.

# Explanation:
# When a signal is triggered, Django directly calls the connected
# signal handler like a normal Python function. There is no 
# background worker, async task, or separate execution 
# flow involved by default. Because of this, the caller 
# waits until the signal handler finishes executing.

# Proof (logic-based code):

# signals.py
import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def slow_signal(sender, instance, **kwargs):
    print("Signal started")
    time.sleep(5)
    print("Signal finished")

# caller code
import time
from django.contrib.auth.models import User

start = time.time()
User.objects.create(username="sync_test")
print("Time taken:", time.time() - start)


# Observation:
# The create() call takes around 5 seconds to return. 
# This shows the caller is blocked until the signal finishes, 
# proving that signals are synchronous by default.