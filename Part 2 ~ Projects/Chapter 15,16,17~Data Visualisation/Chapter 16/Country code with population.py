import json
from GettingCountryCodes import GetCountryCode
filename='population_data.json'
with open(filename) as f:
    pop_data=json.load(f)
for pop_dict in pop_data:
    if pop_dict['Year']=='2010':
        country_name=pop_dict['Country Name']
        code=GetCountryCode(country_name)
        if code:
            population=int(float(pop_dict['Value']))
            print(code+": "+str(population))
        else:
            print("ERROR - "+ country_name)
