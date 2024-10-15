def encrypt(message, key):
    """Criptografa a mensagem usando a Cifra de César."""
    encrypted_message = ""
    for char in message:
        if char.isalpha():  # Verifica se é uma letra
            shift = 65 if char.isupper() else 97  # Ajusta para maiúsculas/minúsculas
            encrypted_message += chr((ord(char) - shift + key) % 26 + shift)
        else:
            encrypted_message += char  # Mantém espaços e pontuação
    return encrypted_message

def decrypt(encrypted_message, key):
    """Descriptografa a mensagem usando a Cifra de César."""
    return encrypt(encrypted_message, -key)  # Reutiliza a função de criptografia

# Exemplo de uso
mensagem = "Ola Mundo!"
chave = 3

# Criptografia
mensagem_criptografada = encrypt(mensagem, chave)
print(f"Mensagem Criptografada: {mensagem_criptografada}")

# Decriptação
mensagem_decriptada = decrypt(mensagem_criptografada, chave)
print(f"Mensagem Decriptada: {mensagem_decriptada}")
