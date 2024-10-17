def vigenere_encrypt(message, key):
    """Criptografa a mensagem usando a Cifra de Vigenère (simplificada)."""
    encrypted_message = ""
    key_repeated = (key * (len(message) // len(key) + 1))[:len(message)] #Repetição da chave

    for m, k in zip(message, key_repeated):
        encrypted_message += chr(((ord(m) - 97 + ord(k) - 97) % 26) + 97)
    
    return encrypted_message

def vigenere_decrypt(encrypted_message, key):
    """Descriptografa a mensagem usando a Cifra de Vigenère (simplificada)."""
    decrypted_message = ""
    key_repeated = (key * (len(encrypted_message) // len(key) + 1))[:len(encrypted_message)]

    for e, k in zip(encrypted_message, key_repeated):
        decrypted_message += chr(((ord(e) - 97 - (ord(k) - 97)) % 26) + 97)
    
    return decrypted_message

# Exemplo de uso
mensagem = "likethelastnight"
chave = "dream"

# Criptografia
mensagem_criptografada = vigenere_encrypt(mensagem, chave)
print(f"Mensagem Criptografada: {mensagem_criptografada}")

# Decriptação
mensagem_decriptada = vigenere_decrypt(mensagem_criptografada, chave)
print(f"Mensagem Decriptada: {mensagem_decriptada}")
