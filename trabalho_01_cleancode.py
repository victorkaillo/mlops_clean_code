# %%
"""
Alunos: Júlia Guardiani e Victor Kaillo
Dsiciplimna: PROJETO DE SISTEMAS BASEADOS EM APRENDIZADO DE MÁQUINA - T01
Professor: Ivanovitch Medeiros Dantas da Silva
"""
# %%
import io
import pandas as pd
import requests

# %%
#Lendo o arquivo csv através da URL do data society.
URL = "https://query.data.world/s/neunletzdxzilhvaz5zq7kmgdsserz"
s = requests.get(URL).content
autos = pd.read_csv(io.StringIO(s.decode('Latin-1')))
autos.info()
autos.head() # pylint: disable=E1101

# %%
#Visualizando as colunas para poder padronizar depois.
columns_autos = autos.columns # pylint: disable=E1101
print(columns_autos)

# %%
#Padronizando os nomes das colunas para facilitar o trabalho com os dados.
autos_rename = autos.rename(columns={'yearOfRegistration' : 'registration_year',  # pylint: disable=E1101
                      'monthOfRegistration':'registration_month',
                      'notRepairedDamage':'unrepaired_damage',
                      'dateCreated':'ad_created'}, inplace=True)
autos_rename.head() # pylint: disable=E1101

# %%
#Explorando os dados para analisar onde é possível limpar os dados.
autos_describe = autos.describe() # pylint: disable=E1101
print(autos_describe)

# %%
#Padronizando o nome da coluna Kilometer para odometer_km.
autos.rename({"kilometer": "odometer_km"}, axis=1, inplace=True) # pylint: disable=E1101

# %%
#Como sugestão da atividade manteremos os itens de  $1 e acima de $350.000,
#já que os preços aumentam continuamente nesse valor e depois saltam para números improváveis.
autos = autos[autos["price"].between(1,351000)] #pylint: disable=E1101

# %%
#Padronizando todas as colunas.
autos.columns = ['date_crawled', 'name', 'seller', 'offer_type', 'price', 'ab_test',
       'vehicle_type', 'registration_year', 'gearbox', 'power_ps', 'model',
       'odometer_km', 'registration_month', 'fuel_type', 'brand',
       'unrepaired_damage', 'ad_created', 'num_photos', 'postal_code',
       'last_seen']
autos.head() # pylint: disable=E1101

# %%
#Explorando colunas de datas de nao registros que são armazenadas como strings.
print(autos[['date_crawled','ad_created','last_seen']][0:5])

# %%
#Utilizando o sort_index() em date_crawled.
(autos["date_crawled"].str[:10].value_counts(normalize=True, dropna=False).sort_index())

# %%
#Utilizando o sort_values() em date_crawled.
(autos["date_crawled"].str[:10].value_counts(normalize=True, dropna=False).sort_values())

# %%
#Utilizando o sort_index em ad_created.
(autos["ad_created"].str[:10].value_counts(normalize=True, dropna=False).sort_index())

# %%
#Utilando o sort_index em last_seen.
(autos["last_seen"].str[:10].value_counts(normalize=True, dropna=False).sort_index())

# %%
autos["registration_year"].describe()

# %%
autos = autos[autos["registration_year"].between(1930,2016)]

# %%
autos["registration_year"].value_counts(normalize=True).head()

# %%
counts_brand = autos["brand"].value_counts(normalize=True)
print(counts_brand)

# %%
#Análise às marcas que representam mais de 5% do total de listagens. (e.g. > 5%)
pop_brands = counts_brand[counts_brand > .05].index


# %%
#Diferença de preço nas principais marcas
mean_prices = {}

for brand in pop_brands:
    brand_key = autos[autos["brand"] == brand]
    mean_price = brand_key["price"].mean()
    mean_prices[brand] = int(mean_price)
print(mean_prices)

# %%
bmp_series = pd.Series(mean_prices)
print(bmp_series)

# %%
df = pd.DataFrame(bmp_series, columns=["mean_price"])
print(df)

# %%
#Explorando a milhagem.
mean_mileage_list = {}

for brand in pop_brands:
    brand_key = autos[autos["brand"] == brand]
    mean_mileage = brand_key["odometer_km"].mean()
    mean_mileage_list[brand] = int(mean_mileage)

mean_mileage = pd.Series(mean_mileage_list).sort_values(ascending=False)
mean_prices_sec = pd.Series(mean_prices).sort_values(ascending=False)

# %%
brand_info = pd.DataFrame(mean_mileage,columns=['mean_mileage'])
print(brand_info)

# %%
brand_info["mean_price"] = mean_prices_sec
