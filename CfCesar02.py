def encrypt(message, key):
    """Criptografa a mensagem usando a Cifra de César."""
    encrypted_message = ""
    for char in message:
        encrypted_message += chr((ord(char) + key))  # Lógica simplificada
    return encrypted_message

def decrypt(encrypted_message, key):
    """Descriptografa a mensagem usando a Cifra de César."""
    decrypted_message = ""
    for char in encrypted_message:
        decrypted_message += chr((ord(char) - key))  # Deslocamento inverso
    return decrypted_message

# Exemplo de uso
mensagem = "hamster"
chave = 2

# Criptografia
mensagem_criptografada = encrypt(mensagem, chave)
print(f"Mensagem Criptografada: {mensagem_criptografada}")

# Decriptação
mensagem_decriptada = decrypt(mensagem_criptografada, chave)
print(f"Mensagem Decriptada: {mensagem_decriptada}")
