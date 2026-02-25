import pandas as pd
import matplotlib.pyplot as plt
import sns  # Seaborn

# 1. Carregamento dos dados
df = pd.read_csv('titanic_dataset.csv')

# 2. Tratamento de Dados (Requisito: Verificação e tratamento de nulos)

df['Age'] = df['Age'].fillna(df['Age'].median())

# Preenchemos o local de embarque com a moda (valor mais frequente)
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

# Removemos a coluna Cabin devido ao excesso de valores ausentes (75%+)
df.drop(columns=['Cabin'], inplace=True)

# 3. Análise Exploratória (Requisito: Uso de GroupBy)
print("--- Taxa de Sobrevivência por Sexo ---")
print(df.groupby('Sex')['Survived'].mean())

print("\n--- Taxa de Sobrevivência por Classe ---")
print(df.groupby('Pclass')['Survived'].mean())

# 4. Construção da Visualização Gráfica
plt.figure(figsize=(10, 6))
sns.barplot(x='Pclass', y='Survived', hue='Sex', data=df, palette='viridis')
plt.title('Taxa de Sobrevivência por Classe e Gênero')
plt.ylabel('Proporção de Sobreviventes')
plt.xlabel('Classe (1ª, 2ª e 3ª)')
plt.savefig('survival_plot.png')
print("\nAnálise concluída. O gráfico foi salvo como 'survival_plot.png'.")