import streamlit as st
import numpy as np
import pandas as pd
import matplotlib as plt
from datetime import datetime
import controllers.clientecontroller as clientecontroller;
import models.cliente as cliente;

def novo_pedido():
    st.title("Digite o pedido")    
    qtd_itens = st.selectbox("Quantidade Itens Pedido:", [1,2,3,4,5,6,7,8,9,10])
    st.write("você selecionou", qtd_itens, "items")
    st.write("Selecione o cliente abaixo")