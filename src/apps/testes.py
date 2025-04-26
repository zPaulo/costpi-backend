# cria um arquivo test_env.py só pra testar
from decouple import config

print(config('DB_PASSWORD'))
