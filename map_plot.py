import streamlit as st
import pandas as pd
import numpy as np
import pyodbc 

st.title("Map Plot Rough")



connector = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='
        + st.secrets["server"]
        + ";DATABASE="
        + st.secrets["database"]
        + ";UID="
        + st.secrets["username"]
        + ";PWD="
        + st.secrets["password"])
csr = connector.cursor()

st.header("All products")
table = pd.read_sql("SELECT * FROM DISPATCH_TABLE", connector)

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(table)

st.subheader('Map of all pickups')
st.map(table)

st.header("Plate Dispatch")
table_plate = pd.read_sql("SELECT * FROM DISPATCH_TABLE WHERE PRODUCT = 'PLATE'", connector)

if st.checkbox('Show plate raw data'):
    st.subheader('Raw data')
    st.write(table_plate)

st.subheader('Map of Plate dispatch')
st.map(table_plate)

st.header("Billet Dispatch")
table_billet = pd.read_sql("SELECT * FROM DISPATCH_TABLE WHERE PRODUCT = 'BILLET'", connector)

if st.checkbox('Show billet raw data'):
    st.subheader('Raw data')
    st.write(table_billet)

st.subheader('Map of Billet dispatch')
st.map(table_billet)

st.header("Rebar Dispatch")
table_rebar = pd.read_sql("SELECT * FROM DISPATCH_TABLE WHERE PRODUCT = 'REBAR'", connector)

if st.checkbox('Show rebar raw data'):
    st.subheader('Raw data')
    st.write(table_rebar)

st.subheader('Map of Rebar dispatch')
st.map(table_rebar)

st.header("Coil Dispatch")
table_coil = pd.read_sql("SELECT * FROM DISPATCH_TABLE WHERE PRODUCT = 'COIL'", connector)

if st.checkbox('Show coil raw data'):
    st.subheader('Raw data')
    st.write(table_coil)

st.subheader('Map of Coil dispatch')
st.map(table_coil)

st.header("Slab 200 Dispatch")
table_slab = pd.read_sql("SELECT * FROM DISPATCH_TABLE WHERE PRODUCT = 'SLAB_200'", connector)

if st.checkbox('Show slab raw data'):
    st.subheader('Raw data')
    st.write(table_slab)

st.subheader('Map of Slab 200 dispatch')
st.map(table_slab)