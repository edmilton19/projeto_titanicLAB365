     Documentação do Projeto: Análise Titanic LAB365
     
Descrição do Projeto:
Este projeto foi desenvolvido para a atividade prática extra do curso de Introdução ao Data Science do SENAI LAB365. O foco foi realizar uma Análise Exploratória de Dados (AED) no famoso dataset do Titanic para entender quais fatores foram determinantes para a sobrevivência dos passageiros.


1. Tratamento de Dados (Data Cleaning):
Ao abrir o arquivo titanic_dataset.csv, identifiquei de cara alguns problemas que poderiam sujar a análise. A coluna 'Age' (Idade) tinha muitos campos vazios; para não perder essas linhas e nem criar uma média mentirosa com valores extremos, decidi preencher os nulos com a mediana das idades. Já a coluna 'Cabin' estava com quase 80% de dados faltantes, então a melhor decisão técnica foi removê-la (drop), pois ela não traria uma base estatística confiável. Também fiz um ajuste na coluna 'Embarked', preenchendo os poucos nulos com a moda (o porto onde mais gente embarcou).


2. Análise e Insights (GroupBy):
Para tirar informações úteis, usei o groupby do Pandas para segmentar os sobreviventes. Os números confirmaram a hipótese de prioridade:

Gênero: As mulheres tiveram uma taxa de sobrevivência muito superior à dos homens (mais de 74% contra menos de 20%).


Classe Social: Passageiros da 1ª classe tiveram uma vantagem nítida de salvamento em comparação à 3ª classe, mostrando o impacto do fator socioeconômico no desastre.

3. Visualização dos Dados:
Criei um gráfico de barras cruzando as classes sociais com o gênero e a sobrevivência. Ele está salvo como survival_plot.png e ajuda a visualizar como ser mulher na primeira classe era quase um passaporte para a sobrevivência, enquanto ser homem na terceira classe era o cenário de maior risco.


