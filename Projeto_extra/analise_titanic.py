from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# 1. Carregamento dos dados
BASE_DIR = Path(__file__).resolve().parent
df = pd.read_csv(BASE_DIR / 'titanic_dataset.csv')

# 2. Tratamento de dados (verificacao e tratamento de nulos)
df['Age'] = df['Age'].fillna(df['Age'].median())

# Preenchemos o local de embarque com a moda (valor mais frequente)
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

# Removemos a coluna Cabin devido ao excesso de valores ausentes (75%+)
df.drop(columns=['Cabin'], inplace=True)

# 3. Analise exploratoria (uso de groupby)
print('--- Taxa de Sobrevivencia por Sexo ---')
print(df.groupby('Sex')['Survived'].mean())

print('\n--- Taxa de Sobrevivencia por Classe ---')
print(df.groupby('Pclass')['Survived'].mean())

# 4. Construcao da visualizacao grafica
plt.figure(figsize=(10, 6))
sns.barplot(x='Pclass', y='Survived', hue='Sex', data=df, palette='viridis')
plt.title('Taxa de Sobrevivencia por Classe e Genero')
plt.ylabel('Proporcao de Sobreviventes')
plt.xlabel('Classe (1a, 2a e 3a)')
plt.savefig(BASE_DIR / 'survival_plot.png')
print("\nAnalise concluida. O grafico foi salvo como 'survival_plot.png'.")
