from typing import List
import services.database as db;
import models.cliente as cliente;
import pandas as pd

def Incluir(cliente):
    count = db.cursor.execute(
        "INSERT INTO cliente (nome_cli, endereco_cli, telefone_cli) VALUES (?, ?, ?)",
        (cliente.nome, cliente.endereco, cliente.telefone)
    ).rowcount
    db.conn.commit()
        
def Alterar(cliente):
    count = db.cursor.execute(
        "UPDATE cliente SET nome_cli = ?, telefone_cli = ?, endereco_cli = ?) where id = ?",        
        (cliente.nome, cliente.endereco, cliente.telefone, cliente.cod)
    ).rowcount
    db.conn.commit()

def SelecionarTodos():
    db.cursor.execute("SELECT * FROM cliente")
    costumerList = []

    for row in db.cursor.fetchall():
        costumerList.append(cliente.Cliente(row[0], row[1],row[2], row[3]))

    return costumerList

def SelecionarByCod(cod):
    db.cursor.execute("SELECT * FROM cliente WHERE cod_cli = ?", cod)
    costumerList = []

    for row in db.cursor.fetchall():
        costumerList.append(cliente.Cliente(row[0], row[1],row[2], row[3]))
    return costumerList[0]

def Excluir(id):
    count = db.cursor.execute(
        "DELETE FROM cliente WHERE cod_cli = ?",
        (id)
    ).rowcount
    db.conn.commit()
    
