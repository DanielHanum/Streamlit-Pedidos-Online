import streamlit as st
import numpy as np
import pandas as pd
import matplotlib as plt
from datetime import datetime
import controllers.clientecontroller as clientecontroller;
import models.cliente as cliente;


def Incluir_Cliente():
    idAlteracao = st.experimental_get_query_params()
    st.experimental_set_query_params()
    clienterecuperado = None
    if idAlteracao.get("id") != None:
        idAlteracao = idAlteracao.get("id")[0]
        st.write(idAlteracao)
        st.title("Alterar Cliente")
        clienterecuperado = clientecontroller.SelecionarByCod(idAlteracao)


    else:
        data_atual = datetime.now()
        data_em_texto = data_atual.strftime("dia "'%d/%m %H:%M')
        st.title("Cadastro Cliente")

    with st.form(key="incluir_cliente"):
        if clienterecuperado == None:
            input_name = st.text_input(label="Nome Cliente")
            input_telefone = st.text_input('Telefone', value='', max_chars=14, key='telefone')
            input_endereco = st.text_input(label="endereço")
        else:
            input_name = st.text_input(label="Nome Cliente",value=clienterecuperado.nome)
            input_telefone = st.text_input('Telefone', max_chars=14, key='telefone', value=clienterecuperado.telefone)
            input_endereco = st.text_input(label="endereço", value=clienterecuperado.endereco)
        input_button_submit = st.form_submit_button("cadastrar")
            
    if input_button_submit:
        st.write(f'Nome:{input_name}')
        st.write(f'telefone cliente:{input_telefone}')
        st.write(f'endereço:{input_endereco}')
        st.write(f'Cliente cadastrado {data_em_texto}')
        cliente.nome = input_name
        cliente.telefone = input_telefone
        cliente.endereco = input_endereco
        clientecontroller.Incluir(cliente.Cliente(0,cliente.nome, cliente.telefone, cliente.endereco))
        st.success('Cliente cadastrado com sucesso')