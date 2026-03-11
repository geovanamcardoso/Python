import pandas as pd
import numpy as np
 
#Criando um dataframe ficticio
np.random.seed(23) #garante a reprodução do experimento
n = 10000 # quantidade de clientes que queremos gerar dados ficticios
 
df = pd.DataFrame({
    "ID": range(1, n+1),
    "Idade": np.random.randint(18,65, n),
    "Renda" : np.random.uniform(2000.0,30000.0, n).round(2),
    "Regiao": np.random.choice(["Norte", "Sul", "Leste", "Oeste"], n)
})
print(df.head())
 
df.sample(15) #pega dados/linhas aleatórias da tabela
 
#Amostragem aleatória simples
#Cria uma tabela nova a partir da anterior (10000 linhas), agora pega 1000 linhas de forma aleatória (33 vezes)
amostra_simples = df.sample(n=1000, random_state=33) #Random state tem o mesmo papel do seed
print(amostra_simples.head())
 
#Amostragem aleatória sistemática
#Constrói intervalos/recortes de 50 linhas nas 10000 linhas
intervalo = np.random.randint(1,50) #Gera intervalo com base na quantidade de registros
amostra_sistematica = df.iloc[::intervalo, :] #nova tabela a partir dos recortes, escolhe dados de cada recorte :: -> qualquer uma, : -> retorne uma
print(amostra_sistematica.head())
 
#Amostragem estratificada
#parte dataset pela metade = 0.5 (50%) (máx: 1), a partir da metade da coluna regiao
#separa em quatro tabelas (4 regioes) e parte metade de cada uma e gera uma unica
from sklearn.model_selection import train_test_split
 
amostra_estratificada, _ = train_test_split(df, test_size=0.5, stratify=df["Regiao"])
print(amostra_estratificada.head())
 
