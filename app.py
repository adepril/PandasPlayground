import streamlit as st
import pandas as pd
import numpy as np

# Fonction pour générer un DataFrame fictif
def generate_dataframe():
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 35, 30, 40],
        'Salary': [90000, 60000, 70000, 80000],
        'Date': pd.date_range(start='1/1/2021', periods=4, freq='M')
    }
    return pd.DataFrame(data)

# Fonctions Pandas à tester
functions = {
    'pd.read_csv(filepath)': 'Lit un fichier CSV et le charge dans un DataFrame.',
    'pd.read_excel(filepath)': 'Lit un fichier Excel et le charge dans un DataFrame.',
    'pd.read_json(filepath)': 'Lit un fichier JSON et le charge dans un DataFrame.',
    'df.to_csv(filepath)': 'Écrit un DataFrame dans un fichier CSV.',
    'df.to_excel(filepath)': 'Écrit un DataFrame dans un fichier Excel.',
    'df.to_json(filepath)': 'Écrit un DataFrame dans un fichier JSON.',
    'pd.DataFrame(data)': 'Crée un DataFrame à partir de diverses structures de données.',
    'pd.Series(data)': 'Crée une série à partir de diverses structures de données.',
    'df.head(n)': 'Affiche les n premières lignes du DataFrame.',
    'df.tail(n)': 'Affiche les n dernières lignes du DataFrame.',
    'df.iloc[row_index, col_index]': 'Sélectionne des lignes et des colonnes par index.',
    'df.loc[row_labels, col_labels]': 'Sélectionne des lignes et des colonnes par étiquettes.',
    'df[df[\'column\'] > value]': 'Filtre les lignes en fonction d\'une condition.',
    'df.drop(labels, axis)': 'Supprime des lignes ou des colonnes spécifiques.',
    'df.rename(columns={\'old_name\': \'new_name\'})': 'Renomme des colonnes.',
    'df.sort_values(by=\'column\')': 'Trie les valeurs d\'une colonne.',
    'df.groupby(\'column\').mean()': 'Groupe les données par une colonne et calcule la moyenne.',
    'df.merge(other_df, on=\'column\')': 'Fusionne deux DataFrames sur une colonne commune.',
    'df.join(other_df, on=\'column\')': 'Joint deux DataFrames sur une colonne commune.',
    'pd.concat([df1, df2])': 'Concatène plusieurs DataFrames.',
    'df.describe()': 'Affiche des statistiques descriptives pour chaque colonne.',
    'df.mean()': 'Calcule la moyenne de chaque colonne.',
    'df.sum()': 'Calcule la somme de chaque colonne.',
    'df.count()': 'Compte le nombre de valeurs non nulles dans chaque colonne.',
    'df.value_counts()': 'Compte le nombre d\'occurrences de chaque valeur unique dans une colonne.',
    'df.dropna()': 'Supprime les lignes ou les colonnes avec des valeurs manquantes.',
    'df.fillna(value)': 'Remplit les valeurs manquantes avec une valeur spécifiée.',
    'df.isna()': 'Vérifie si les valeurs sont manquantes (NaN).',
    'df.apply(func)': 'Applique une fonction à chaque colonne ou ligne.',
    'df.map(func)': 'Applique une fonction à chaque élément d\'une série.'
}

# Interface utilisateur
st.title('Pandas Functions Visualizer')
st.sidebar.title('Select a Function')

# Sélection de la fonction
selected_function = st.sidebar.selectbox('Choose a function', list(functions.keys()))

# Affichage de la description de la fonction
st.sidebar.write(functions[selected_function])

# Génération du DataFrame fictif
df = generate_dataframe()

# Exécution de la fonction sélectionnée
if selected_function == 'pd.read_csv(filepath)':
    st.write('This function reads a CSV file and loads it into a DataFrame.')
    st.write(df)
elif selected_function == 'pd.read_excel(filepath)':
    st.write('This function reads an Excel file and loads it into a DataFrame.')
    st.write(df)
elif selected_function == 'pd.read_json(filepath)':
    st.write('This function reads a JSON file and loads it into a DataFrame.')
    st.write(df)
elif selected_function == 'df.to_csv(filepath)':
    st.write('This function writes a DataFrame to a CSV file.')
    st.write(df)
elif selected_function == 'df.to_excel(filepath)':
    st.write('This function writes a DataFrame to an Excel file.')
    st.write(df)
elif selected_function == 'df.to_json(filepath)':
    st.write('This function writes a DataFrame to a JSON file.')
    st.write(df)
elif selected_function == 'pd.DataFrame(data)':
    st.write('This function creates a DataFrame from various data structures.')
    st.write(df)
elif selected_function == 'pd.Series(data)':
    st.write('This function creates a Series from various data structures.')
    st.write(df['Name'])
elif selected_function == 'df.head(n)':
    n = st.number_input('Enter the number of rows to display', min_value=1, max_value=len(df), value=5)
    st.write(df.head(n))
elif selected_function == 'df.tail(n)':
    n = st.number_input('Enter the number of rows to display', min_value=1, max_value=len(df), value=5)
    st.write(df.tail(n))
elif selected_function == 'df.iloc[row_index, col_index]':
    row_index = st.number_input('Enter the row index', min_value=0, max_value=len(df)-1, value=0)
    col_index = st.number_input('Enter the column index', min_value=0, max_value=len(df.columns)-1, value=0)
    st.write(df.iloc[row_index, col_index])
elif selected_function == 'df.loc[row_labels, col_labels]':
    row_labels = st.text_input('Enter the row labels (comma-separated)', '0,1')
    col_labels = st.text_input('Enter the column labels (comma-separated)', 'Name,Age')
    row_labels = row_labels.split(',')
    col_labels = col_labels.split(',')
    st.write(df.loc[row_labels, col_labels])
elif selected_function == 'df[df[\'column\'] > value]':
    column = st.selectbox('Select a column', df.columns)
    value = st.number_input('Enter the value')
    st.write(df[df[column] > value])
elif selected_function == 'df.drop(labels, axis)':
    labels = st.text_input('Enter the labels to drop (comma-separated)', 'Name')
    axis = st.selectbox('Select the axis', ['columns', 'index'])
    axis = 1 if axis == 'columns' else 0
    labels = labels.split(',')
    st.write(df.drop(labels, axis=axis))
elif selected_function == 'df.rename(columns={\'old_name\': \'new_name\'})':
    old_name = st.text_input('Enter the old column name', 'Name')
    new_name = st.text_input('Enter the new column name', 'FullName')
    st.write(df.rename(columns={old_name: new_name}))
elif selected_function == 'df.sort_values(by=\'column\')':
    column = st.selectbox('Select a column to sort by', df.columns)
    st.write(df.sort_values(by=column))
elif selected_function == 'df.groupby(\'column\').mean()':
    column = st.selectbox('Select a column to group by', df.columns)
    st.write(df.groupby(column).mean())
elif selected_function == 'df.merge(other_df, on=\'column\')':
    other_df = generate_dataframe()
    column = st.selectbox('Select a column to merge on', df.columns)
    st.write(df.merge(other_df, on=column))
elif selected_function == 'df.join(other_df, on=\'column\')':
    other_df = generate_dataframe()
    column = st.selectbox('Select a column to join on', df.columns)
    st.write(df.join(other_df.set_index(column), on=column))
elif selected_function == 'pd.concat([df1, df2])':
    other_df = generate_dataframe()
    st.write(pd.concat([df, other_df]))
elif selected_function == 'df.describe()':
    st.write(df.describe())
elif selected_function == 'df.mean()':
    st.write(df.mean())
elif selected_function == 'df.sum()':
    st.write(df.sum())
elif selected_function == 'df.count()':
    st.write(df.count())
elif selected_function == 'df.value_counts()':
    column = st.selectbox('Select a column', df.columns)
    st.write(df[column].value_counts())
elif selected_function == 'df.dropna()':
    st.write(df.dropna())
elif selected_function == 'df.fillna(value)':
    value = st.text_input('Enter the value to fill NaN', '0')
    st.write(df.fillna(value))
elif selected_function == 'df.isna()':
    st.write(df.isna())
elif selected_function == 'df.apply(func)':
    func = st.text_input('Enter the function to apply', 'lambda x: x * 2')
    st.write(df.apply(eval(func)))
elif selected_function == 'df.map(func)':
    func = st.text_input('Enter the function to apply', 'lambda x: x * 2')
    column = st.selectbox('Select a column', df.columns)
    st.write(df[column].map(eval(func)))

