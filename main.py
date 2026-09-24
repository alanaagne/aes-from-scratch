# main.py
from aes import aes_encrypt_block, aes_decrypt_block

def main():
    print("=" * 60)
    print(" DEMONSTRAÇÃO PRÁTICA DO ALGORITMO AES-128 (SEM LIBS) ")
    print("=" * 60)

    # Texto e chave exatamente com 16 caracteres (16 bytes = 128 bits)
    texto_claro = "SegurancaRedes26"  # 16 bytes
    chave = "ChaveSecreta128b"         # 16 bytes

    bytes_texto = texto_claro.encode('utf-8')
    bytes_chave = chave.encode('utf-8')

    print(f"\n[+] Texto Original : {texto_claro}")
    print(f"[+] Chave Usada     : {chave}")
    print(f"[+] Bytes do Texto  : {bytes_texto.hex()}")

    # Cifragem
    bloco_cifrado = aes_encrypt_block(bytes_texto, bytes_chave)
    print(f"\n[✓] Bloco Cifrado (HEX): {bloco_cifrado.hex().upper()}")

    # Decifragem
    bloco_decifrado = aes_decrypt_block(bloco_cifrado, bytes_chave)
    texto_recuperado = bloco_decifrado.decode('utf-8')

    print(f"\n[✓] Bloco Decifrado (Texto): {texto_recuperado}")

    # Validação do teste
    if texto_claro == texto_recuperado:
        print("\n--> SUCESSO: O texto decifrado é idêntico ao original!")
    else:
        print("\n--> ERRO: Falha no processo de decifragem.")

if __name__ == "__main__":
    main()