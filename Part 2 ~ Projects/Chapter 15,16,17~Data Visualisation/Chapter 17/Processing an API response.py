import requests
url='https://api.github.com/search/repositories?q=language:python&sort=stars'
r=requests.get(url)
print("Status code:",r.status_code)
response_dict=r.json()
print(response_dict.keys())
##Status code of 200 means request response is successful
