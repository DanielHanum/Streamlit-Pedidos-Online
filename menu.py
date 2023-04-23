#bibliotecas importadas

import streamlit as st
import numpy as np
import pandas as pd
import matplotlib as plt
from datetime import datetime
import controllers.clientecontroller as clientecontroller;
import models.cliente as cliente;
import pages.Cliente.incluir_cliente as page_incluir_cliente;
import pages.Cliente.consultar_cliente as page_consultar_cliente;
import pages.pedidos.novopedido as novo_pedido;
#variaveis globais

data_atual = datetime.now()
data_em_texto = data_atual.strftime("dia "'%d/%m %H:%M')
paginaselecionada = st.sidebar.selectbox("Selecione uma opção",['Cadastro','Novo Pedido','ConsultarCliente'])

#menu de cadastro de clientes 
if paginaselecionada=='Cadastro':
    page_incluir_cliente.Incluir_Cliente()

#menu pedido 
elif paginaselecionada=='Novo Pedido':
    novo_pedido.novo_pedido()

#menu Consultar cliente
elif paginaselecionada=='ConsultarCliente':
    page_consultar_cliente.Consultar_Cliente()

