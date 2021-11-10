# %%
"""
Testando descrevendo o codigo
"""
import io
import pandas as pd
import requests


# %%
URL = "https://query.data.world/s/neunletzdxzilhvaz5zq7kmgdsserz"
s = requests.get(URL).content
autos = pd.read_csv(io.StringIO(s.decode('Latin-1')))

# %%
autos.info()
autos.head(20) # pylint: disable=E1101
# %%
autos.rename(columns={'yearOfRegistration' : 'registration_year', # pylint: disable=E1101
                      'monthOfRegistration':'registration_month',
                      'notRepairedDamage':'unrepaired_damage',
                      'dateCreated':'ad_created'}, inplace=True)
autos.head() # pylint: disable=E1101


# %%
describe_autos = autos.describe() # pylint: disable=E1101
print(describe_autos)
# %%
#autos["price"] = (autos["price"].str.replace("$","").
# str.replace(",","").astype(int))
#autos["price"].head()

# %%
#Código comentado pois a atividade pedia tal funcionalidade,
#mas o csv do Query já vinha com sem esse problema.

#autos["odometer"] = (autos["odometer"].str.replace("km","")
# .str.replace(",","").astype(int))

# %%
rename_odometer = autos.rename({"kilometer": "odometer_km"}, axis=1, inplace=True) # pylint: disable=E1101
#head_odometer = autos["odometer_km"].head()
#print(head_odometer)

# %%
autos = autos[autos["price"].between(1,351000)]
autos["price"].describe()

# %%
#padronizando todas as colunas
autos.columns = ['date_crawled', 'name', 'seller', 'offer_type', 'price', 'ab_test',
       'vehicle_type', 'registration_year', 'gearbox', 'power_ps', 'model',
       'odometer_km', 'registration_month', 'fuel_type', 'brand',
       'unrepaired_damage', 'ad_created', 'num_photos', 'postal_code',
       'last_seen']
autos.head()

# %%
print(autos[['date_crawled','ad_created','last_seen']][0:5])

# %%
#sort_index()
(autos["date_crawled"].str[:10].value_counts(normalize=True, dropna=False).sort_index())

# %%
#sort_values()
(autos["date_crawled"].str[:10].value_counts(normalize=True, dropna=False).sort_values())

# %%
(autos["ad_created"].str[:10].value_counts(normalize=True, dropna=False).sort_index())

# %%
(autos["last_seen"].str[:10].value_counts(normalize=True, dropna=False).sort_index())

# %%
autos["registration_year"].describe()

# %%
#primeiro modelo de automóvel fabricado pela companhia alemã Volkswagen, sendo produzido entre 1938
registration_auto = (~autos["registration_year"].between(1930,2016)).sum() / autos.shape[0]

# %%
autos = autos[autos["registration_year"].between(1930,2016)]

# %%
autos["registration_year"].value_counts(normalize=True).head()

# %%
counts_brand = autos["brand"].value_counts(normalize=True)
print(counts_brand)

# %%
# (e.g. > 5%)
pop_brands = counts_brand[counts_brand > .05].index
print(pop_brands)
#achar top20

# %%
mean_prices = {}

for brand in pop_brands:
    brand_key = autos[autos["brand"] == brand]
    mean_price = brand_key["price"].mean()
    mean_prices[brand] = int(mean_price)

# %%
print(mean_prices)

# %%
bmp_series = pd.Series(mean_prices)
print(bmp_series)

# %%
df = pd.DataFrame(bmp_series, columns=["mean_price"])
print(df)

# %%
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
print(brand_info)

# %%
