import requests
res = requests.get('https://zipcloud.ibsnet.co.jp/api/search', params={'zipcode':'1008111'})
res_json = res.json()
results = res_json['results'][0]
address = results['address2'] + results['address3']
print(address)