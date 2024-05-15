import json
import os
import secrets

def generate_secret_key():
    """Gera uma secret key aleatória."""
    return secrets.token_hex(16)  # Gera uma chave hexadecimal de 16 bytes

def save_secret_key_to_json(secret_key, filename='secret_key.json'):
    """Salva a secret key em um arquivo JSON."""
    with open(filename, 'w') as f:
        json.dump({'secret_key': secret_key}, f)

def load_secret_key_from_json(filename='secret_key.json'):
    """Carrega a secret key de um arquivo JSON."""
    with open(filename, 'r') as f:
        data = json.load(f)
        return data.get('secret_key', '')

# Gera uma nova secret key
new_secret_key = generate_secret_key()

# Salva a secret key em um arquivo JSON
save_secret_key_to_json(new_secret_key)

# Carrega a secret key do arquivo JSON
loaded_secret_key = load_secret_key_from_json()

print("Secret key gerada e armazenada com sucesso:", loaded_secret_key)