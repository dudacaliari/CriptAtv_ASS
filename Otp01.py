def encrypt(message, key):
    """Criptografa a mensagem usando XOR."""
    return message ^ key  # XOR entre mensagem e chave

def decrypt(encrypted_message, key):
    """Descriptografa a mensagem usando XOR."""
    return encrypted_message ^ key  # XOR entre mensagem criptografada e chave

def to_binary(value):
    """Converte um número decimal para uma string binária."""
    return bin(value)[2:].zfill(8)  # [2:] Remove '0b' e .zfill(8) completa com zeros à esquerda até a string ter 8 bits

# Exemplo de uso
mensagem = 56  # Mensagem clara 
chave = 78     # Chave

# Criptografia
mensagem_criptografada = encrypt(mensagem, chave)

# Exibindo valores em decimal e binário
print(f"Mensagem: {mensagem} | Binário: {to_binary(mensagem)}")
print(f"Chave: {chave} | Binário: {to_binary(chave)}")
print(f"Mensagem Criptografada: {mensagem_criptografada} | Binário: {to_binary(mensagem_criptografada)}")

# Decriptação
mensagem_decriptada = decrypt(mensagem_criptografada, chave)
print(f"Mensagem Decriptada: {mensagem_decriptada} | Binário: {to_binary(mensagem_decriptada)}")
