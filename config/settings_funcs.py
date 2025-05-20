import environ
import os
from django.conf import settings

def getEnv(BASE_DIR):
    env = environ.Env(
    DEBUG=(bool, False)
    )
    environ.Env.read_env(os.path.join(BASE_DIR, '.env'))
    return env

def debug_message(debug_status):
    if debug_status:
        print(f"Debugging is ON ({debug_status}) for this server.")
    else:
        print(f"Debugging is OFF ({debug_status}) for this server.")
    return debug_status