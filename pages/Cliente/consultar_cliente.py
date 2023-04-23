import streamlit as st
import numpy as np
import pandas as pd
import matplotlib as plt
from datetime import datetime
import controllers.clientecontroller as clientecontroller;
import models.cliente as cliente;
import pages.Cliente.incluir_cliente as PageIncluirCliente;

def Consultar_Cliente():
    paramId = st.experimental_get_query_params()
    if paramId == {}:
        colms = st.columns((1,2,3,4))
        campos = ['Cod', 'Nome', 'Endereco', 'Telefone', 'Excluir', 'Alterar']
        for col, campo_nome in zip(colms,campos):
            col.write(campo_nome)
        
        for item in clientecontroller.SelecionarTodos():
            col1, col2, col3, col4, col5, col6 = st.columns((1,1,1,1,1,1))
            col1.write(item.cod)
            col2.write(item.nome)
            col3.write(f"   {item.telefone}")
            col4.write(f"{item.endereco}")
            button_space_excluir = col5.empty()
            on_click_excluir = button_space_excluir.button('Excluir', 'btnExcluir' + str(item.cod))
            button_space_alterar = col6.empty()
            on_click_alterar = button_space_alterar.button('Alterar', 'btnAlterar' + str(item.cod))

            if on_click_excluir:
                clientecontroller.Excluir(item.cod)
                button_space_excluir.button('Excluido', 'btnExcluir2' + str(item.cod))

            if on_click_alterar:
                st.experimental_set_query_params(
                    id=[item.cod]
                )
                st.experimental_rerun()
    else:
        PageIncluirCliente.Incluir_Cliente()

