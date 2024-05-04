import streamlit as st
import pandas as pd

st. header("Simulador CESDE")

df = pd.read_csv('datasets/cesde.csv')


#------------------------------------------------------------------------------
def notas_estudiante():
    gruposU = sorted(df['GRUPO'].unique()) 
    momentoU = sorted(df['MOMENTO'].unique()) 
    col1, col2 = st.columns(2)
    with col1:
        grupo_seleccionado= st.selectbox("Grupos",gruposU)
    with col2:
        momento_selecionado = st.selectbox("Momentos",momentoU)
    estudiantes = df[(df['GRUPO']==grupo_seleccionado)&(df['MOMENTO']==momento_selecionado)]
    
    estudiante_selecionado = st.selectbox("Estudiante",estudiantes['NOMBRE'])

    notas_estudiante = estudiantes[df['NOMBRE']==estudiante_selecionado]
    # estudiante = sorted(estudiantes['NOMBRE'].unique())
    # print(type(estudiantes))
    st.table(notas_estudiante[['CONOCIMIENTO','DESEMPEÑO','PRODUCTO']])

    data = {
    'Tipo': ['CONOCIMIENTO', 'DESEMPEÑO', 'PRODUCTO'],
    'Cantidad': [5, 2,4]
    }

    df_grafico = pd.DataFrame(data)
   
    # Graficar el DataFrame con un gráfico de barras
    st.bar_chart(df_grafico.set_index('Tipo'))

#------------------------------------------------------------------------------
def notas_grupo():
    gruposU = sorted(df['GRUPO'].unique()) 
    opcion = st.selectbox("Grupos",gruposU)
    estudiantes = df[df['GRUPO']==opcion]
    st.table(estudiantes)

#------------------------------------------------------------------------------
def estudiantes_becado():
    pass


#------------------------------------------------------------------------------
filtros = [
    'Notas por estudiante',
    'Notas por grupo',
    'Estudiantes becados'
]

seleccion_filtro = st.selectbox("Filtro", filtros)

if seleccion_filtro:
    index = filtros.index(seleccion_filtro)
    if index == 0:
        notas_estudiante()
    elif index == 1:
        notas_grupo()
    elif index == 2:
        estudiantes_becado()
    


