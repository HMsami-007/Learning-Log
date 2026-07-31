import requests
url='https://api.github.com/search/repositories?q=language:python&sort=stars'
r=requests.get(url)
print("Status code:",r.status_code)
response_dict=r.json()
print("Total repositories:",response_dict['total_count'])
repo_dicts=response_dict['items']
print("Repositories returned:",len(repo_dicts))
print("\nSelected information about first repository:")
for repo_dict in repo_dicts:
    print('\nName:',repo_dict['name'])           #The name public-apis appears instead of a personal username because this specific repository belongs to a GitHub Organization, not an individual person.
    print('Owner',repo_dict['owner']['login'])
    print('Stars:',repo_dict['stargazers_count'])
    print('Repository:',repo_dict['html_url'])
    print('Description:',repo_dict['description'])
