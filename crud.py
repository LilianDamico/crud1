import sqlite3

conn = sqlite3.connect('clientes.db')
cursor = conn.cursor()

def cria_cliente(nome, email, telefone):
    cursor.execute("""
    INSERT INTO clientes (nome, email, telefone)
    VALUES (?, ?, ?)
    """, (nome, email, telefone))
    conn.commit()
    print('Cliente criado com sucesso.')

cria_cliente('João da Silva', 'joao.silva@gmail.com', '(11) 99999-9999')


