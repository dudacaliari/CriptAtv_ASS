def matrix_multiply(matrix, vector, mod=26):
    """Multiplica uma matriz por um vetor e aplica módulo."""
    result = []
    for row in matrix:
        # Soma dos produtos correspondentes da linha da matriz e do vetor
        value = sum(row[i] * vector[i] for i in range(len(vector))) % mod
        result.append(value)
    return result

def mod_inverse(a, mod):
    """Calcula o inverso modular de 'a' no módulo dado."""
    for i in range(mod):
        if (a * i) % mod == 1:
            return i
    raise ValueError(f"Inverso modular não encontrado para {a} no módulo {mod}")

def matrix_inverse_2x2(matrix, mod=26):
    """Calcula a inversa de uma matriz 2x2 no módulo dado."""
    det = (matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]) % mod
    inv_det = mod_inverse(det, mod)

    # Matriz adjunta e multiplicação pelo inverso do determinante
    return [
        [(matrix[1][1] * inv_det) % mod, (-matrix[0][1] * inv_det) % mod],
        [(-matrix[1][0] * inv_det) % mod, (matrix[0][0] * inv_det) % mod]
    ]

def hill_encrypt(message, key):
    """Criptografa a mensagem usando a Cifra de Hill."""
    n = len(key)  # Tamanho da matriz chave
    # Preenche a mensagem com 'x' se necessário
    while len(message) % n != 0:
        message += 'x'

    encrypted_message = ""
    for i in range(0, len(message), n):
        block = [ord(char) - 97 for char in message[i:i + n]]  # Converte para índices
        encrypted_block = matrix_multiply(key, block)  # Multiplica pela chave
        encrypted_message += ''.join(chr(num + 97) for num in encrypted_block)  # Converte de volta para letras

    return encrypted_message

def hill_decrypt(encrypted_message, key):
    """Descriptografa a mensagem usando a Cifra de Hill."""
    n = len(key)  # Tamanho da matriz chave
    key_inv = matrix_inverse_2x2(key)  # Inversa da chave

    decrypted_message = ""
    for i in range(0, len(encrypted_message), n):
        block = [ord(char) - 97 for char in encrypted_message[i:i + n]]  # Converte para índices
        decrypted_block = matrix_multiply(key_inv, block)  # Multiplica pela matriz inversa
        decrypted_message += ''.join(chr(num + 97) for num in decrypted_block)  # Converte de volta para letras

    return decrypted_message

# Exemplo de uso
mensagem = "kirby"
chave = [[3, 3], [2, 5]]  # Matriz 2x2

# Criptografia
mensagem_criptografada = hill_encrypt(mensagem, chave)
print(f"Mensagem Criptografada: {mensagem_criptografada}")

# Decriptação
mensagem_decriptada = hill_decrypt(mensagem_criptografada, chave)
print(f"Mensagem Decriptada: {mensagem_decriptada}")
