import numpy as np

def hill_encrypt(message, key):
    """Criptografa a mensagem usando a Cifra de Hill."""
    key_matrix = np.array(key)
    message = message.replace(" ", "").upper()  # Remove espaços e transforma em maiúsculas
    while len(message) % key_matrix.shape[0] != 0:
        message += 'X'  # Adiciona 'X' se necessário para completar

    encrypted_message = ""
    for i in range(0, len(message), key_matrix.shape[0]):
        block = np.array([ord(char) - 65 for char in message[i:i + key_matrix.shape[0]]])  # Converte para índices
        encrypted_block = np.dot(key_matrix, block) % 26  # Multiplica e aplica módulo 26
        encrypted_message += ''.join(chr(num + 65) for num in encrypted_block)  # Converte de volta para letras

    return encrypted_message

def hill_decrypt(encrypted_message, key):
    """Descriptografa a mensagem usando a Cifra de Hill."""
    key_matrix = np.array(key)
    det = int(np.round(np.linalg.det(key_matrix)))  # Determinante
    inv_det = pow(det, -1, 26)  # Inverso modular do determinante
    key_matrix_inv = (inv_det * np.round(np.linalg.inv(key_matrix)).astype(int)) % 26  # Matriz inversa

    decrypted_message = ""
    for i in range(0, len(encrypted_message), key_matrix.shape[0]):
        block = np.array([ord(char) - 65 for char in encrypted_message[i:i + key_matrix.shape[0]]])
        decrypted_block = np.dot(key_matrix_inv, block) % 26
        decrypted_message += ''.join(chr(num + 65) for num in decrypted_block)

    return decrypted_message

# Exemplo de uso
mensagem = "HELLO"
chave = [[6, 24], [1, 13]]  # Matriz 2x2

# Criptografia
mensagem_criptografada = hill_encrypt(mensagem, chave)
print(f"Mensagem Criptografada: {mensagem_criptografada}")

# Decriptação
mensagem_decriptada = hill_decrypt(mensagem_criptografada, chave)
print(f"Mensagem Decriptada: {mensagem_decriptada}")
