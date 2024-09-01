import pandas as pd

# Listes des fonctions et leurs descriptions
fonctions_panda = {
    'Function 1': 'Loading data from a CSV file into a DataFrame.',
    'Function 2': 'Creating a DataFrame from a dictionary of lists.',
    'Function 3': 'Creating a DataFrame from two separate arrays.',
    'Function 4': 'Adding two DataFrames together.',
    'Function 5': 'Merging two DataFrames based on a common column.'
}

def charger_donnees():
    """Charge des données fictives dans un DataFrame"""
    data = {
        'Nom': ['Alice', 'Bob', 'Carol'],
        'Age': [25, 30, 35],
        'Ville': ['New York', 'Paris', 'Londres']
    }

    return pd.DataFrame(data)

def charger_donnees_csv():
    """Charge des données fictives à partir d'un fichier CSV"""
    data = {
        'Nom': ['Alice', 'Bob', 'Carol'],
        'Age': [25, 30, 35],
        'Ville': ['New York', 'Paris', 'Londres']
    }

    df_csv = pd.DataFrame(data)

    ##return pd.read_csv('donnees.csv')
    return df_csv

def creer_df_dictionnaire():
    """Crée un DataFrame à partir d'un dictionnaire"""
    data = {
        'Nom': ['Alice', 'Bob', 'Carol'],
        'Age': [25, 30, 35],
        'Ville': ['New York', 'Paris', 'Londres']
    }

    return pd.DataFrame(data)

def main():
    for fonction in fonctions_panda.keys():
        print(f"{fonction}\n{fonctions_panda[fonction]}\n")

        if fonction == "Function 1":
            df = charger_donnees_csv()
            print(df)
            print("\n")
        elif fonction == "Function 2":
            data = {
                'Nom': ['Alice', 'Bob', 'Carol'],
                'Age': [25, 30, 35],
                'Ville': ['New York', 'Paris', 'Londres']
            }

            df = pd.DataFrame(data)
            print(df)
            print("\n")
        elif fonction == "Function 3":
            # Creating DataFrame from two separate arrays
            nom = ['Alice', 'Bob', 'Carol']
            age = [25, 30, 35]

            data = {
                'Nom': nom,
                'Age': age
            }

            df = pd.DataFrame(data)
            print(df)
            print("\n")
        elif fonction == "Function 4":
            # Adding two DataFrames together
            df1 = charger_donnees_csv()
            df2 = creer_df_dictionnaire()

            df_add = pd.concat([df1, df2], ignore_index=True)

            print(df_add)
            print("\n")
        elif fonction == "Function 5":
            # Merging two DataFrames based on a common column
            df1 = charger_donnees_csv()
            df2 = creer_df_dictionnaire()

            merge_df = pd.merge(df1, df2, how='outer', indicator=True)

            print(merge_df)
            print("\n")
        else:
            print("Cette fonction n'est pas supportée.")
        print("-----------")

if __name__ == "__main__":
    main()