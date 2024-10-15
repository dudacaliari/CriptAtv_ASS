def vigenere_encrypt(message, key):
    """Criptografa a mensagem usando a Cifra de Vigenère."""
    encrypted_message = ""
    # Repete a chave até o comprimento da mensagem
    key_repeated = (key * (len(message) // len(key) + 1))[:len(message)]

    for m, k in zip(message, key_repeated):
        if m.isalpha():  # Verifica se é uma letra
            shift = 65 if m.isupper() else 97  # Determina o offset para letras maiúsculas/minúsculas
            encrypted_message += chr((ord(m) - shift + ord(k.lower()) - 97) % 26 + shift)
        else:
            encrypted_message += m  # Mantém espaços e pontuação
    return encrypted_message

def vigenere_decrypt(encrypted_message, key):
    """Descriptografa a mensagem usando a Cifra de Vigenère."""
    decrypted_message = ""
    key_repeated = (key * (len(encrypted_message) // len(key) + 1))[:len(encrypted_message)]

    for e, k in zip(encrypted_message, key_repeated):
        if e.isalpha():  # Verifica se é uma letra
            shift = 65 if e.isupper() else 97
            decrypted_message += chr((ord(e) - shift - (ord(k.lower()) - 97)) % 26 + shift)
        else:
            decrypted_message += e  # Mantém espaços e pontuação
    return decrypted_message

# Exemplo de uso
mensagem = "A Cifra Vigenere é interessante"
chave = "chave"

# Criptografia
mensagem_criptografada = vigenere_encrypt(mensagem, chave)
print(f"Mensagem Criptografada: {mensagem_criptografada}")

# Decriptação
mensagem_decriptada = vigenere_decrypt(mensagem_criptografada, chave)
print(f"Mensagem Decriptada: {mensagem_decriptada}")
