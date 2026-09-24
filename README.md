# 🔒 AES-128 do Zero em Python (sem bibliotecas externas)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square&logo=python)
![Licença](https://img.shields.io/badge/Licen%C3%A7a-MIT-green?style=flat-square)
![Status](https://img.shields.io/badge/Status-Conclu%C3%ADdo-brightgreen?style=flat-square)

Este repositório contém uma implementação do algoritmo de criptografia **AES-128 (Advanced Encryption Standard)** desenvolvida do zero na linguagem Python, sem a utilização de quaisquer bibliotecas criptográficas de terceiros (como `cryptography` ou `pycryptodome`). 

O projeto foi desenvolvido para fins académicos no âmbito da disciplina de **Segurança de Redes de Computadores** do **Instituto Federal de Educação, Ciência e Tecnologia da Bahia (IFBA)**.

---

## 📌 Conteúdos do Projeto

- [Sobre o AES-128](#-sobre-o-aes-128)
- [Funcionalidades Implementadas](#-funcionalidades-implementadas)
- [Estrutura do Repositório](#-estrutura-do-repositório)
- [Como Executar](#-como-executar)
- [Exemplo de Saída](#-exemplo-de-saída)
- [Integrantes do Projeto](#-integrantes-do-projeto)

---

## 🔐 Sobre o AES-128

O **AES (Advanced Encryption Standard)** é um algoritmo de criptografia simétrica por blocos adotado como padrão global. A versão **AES-128** opera sobre blocos de dados de 128 bits (16 bytes) e utiliza uma chave de 128 bits, realizando **10 rodadas (rounds)** de transformação sobre uma matriz de estado $4 \times 4$ (*State*).

### Etapas da Cifragem:
1. **KeyExpansion**: Geração das 11 subchaves de rodada a partir da chave principal.
2. **AddRoundKey**: Operação XOR entre a matriz de estado e a subchave da rodada.
3. **SubBytes / InvSubBytes**: Substituição não linear de bytes via S-Box.
4. **ShiftRows / InvShiftRows**: Permutação de linhas na matriz de estado.
5. **MixColumns / InvMixColumns**: Mistura linear das colunas operando sobre o Campo de Galois $GF(2^8)$.

---

## 🚀 Funcionalidades Implementadas

- [x] Tabela **S-Box** e **Inv S-Box** para substituição de bytes.
- [x] Multiplicação no Campo de Galois $GF(2^8)$ com polinómio redutor $0x11B$.
- [x] Rotinas de expansão de chave (**KeyExpansion** com **Rcon**).
- [x] Processo completo de cifragem (**`aes_encrypt_block`**).
- [x] Processo completo de decifragem (**`aes_decrypt_block`**).
- [x] Script interativo de demonstração (`main.py`).

---

## 📂 Estrutura do Repositório

```text
aes-from-scratch/
├── .gitignore          # Ficheiros ignorados pelo Git
├── README.md            # Documentação e instruções de utilização
├── aes.py               # Implementação pura do AES-128 (funções e tabelas)
└── main.py              # Script principal para execução e testes
```
---

## 💻 Como Executar

*  **Pré-requisitos**
Apenas o Python 3.8 ou superior instalado no seu sistema. Não é necessária a instalação de pacotes adicionais via pip.

* **Passos**
Clone o repositório:


```Bash
git clone [https://github.com/alanaagne/aes-from-scratch.git](https://github.com/alanaagne/aes-from-scratch.git)
Entre na pasta do projeto:

```

```Bash
cd aes-from-scratch

```
* Execute o script principal:

```Bash
python main.py

```
---

## 📊 Exemplo de Saída

```Plaintext
============================================================
 DEMONSTRAÇÃO PRÁTICA DO ALGORITMO AES-128 (SEM LIBS) 
============================================================

[+] Texto Original : SegurancaRedes26
[+] Chave Usada     : ChaveSecreta128b
[+] Bytes do Texto  : 5365677572616e636152656465733236

[✓] Bloco Cifrado (HEX): C78E9A82B02A1C3F9A27F11E...

[✓] Bloco Decifrado (Texto): SegurancaRedes26

--> SUCESSO: O texto decifrado é idêntico ao original!

```
---