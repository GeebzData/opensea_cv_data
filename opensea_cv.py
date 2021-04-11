import requests
import pandas as pd


url = 'https://api.opensea.io/api/v1/assets?asset_contract_address=0x79986af15539de2db9a5086382daeda917a9cf0c'

# update query string for desired results
querystring = {
   "order_direction":"desc",
   "offset":"0",
   "limit":"5000"}

# add headers/SSL if necessary
response = requests.request("GET", url, params=querystring)
j = response.json()

# create dataframe with one columns of json strings
df = pd.DataFrame.from_dict(j)

# split out json assets to columns
assets_normalized = pd.json_normalize(df.assets)
#assets_normalized.to_csv('assets.csv', index=False)
#print(assets_normalized)


#condense down to only needed data
final_data = assets_normalized[[
'id',
'name',
'description',
'traits',
'asset_contract.address',
'asset_contract.asset_contract_type',
'asset_contract.created_date',
'asset_contract.name',
'asset_contract.description',
'collection.description',
'collection.name',
'last_sale.total_price',
'last_sale.payment_token.symbol',
'last_sale.event_timestamp',
'last_sale.transaction.timestamp',
'last_sale.transaction.to_account.user.username'
]]

final_data.to_csv('assets.csv', index=False) 