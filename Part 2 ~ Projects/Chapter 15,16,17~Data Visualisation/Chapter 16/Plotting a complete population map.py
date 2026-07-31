import json
import pygal
from GettingCountryCodes import GetCountryCode
from pygal_maps_world.maps import World
filename='population_data.json'
with open(filename) as f:
    pop_data=json.load(f)
cc_populations={}
for pop_dict in pop_data:
    if pop_dict['Year']=='2010':
        country_name=pop_dict['Country Name']
        code=GetCountryCode(country_name)
        population=int(float(pop_dict['Value']))
        if code:
            cc_populations[code]=population
wm=World()
wm.title="World Population in 2010,by country"
wm.add('2010',cc_populations)
wm.render_to_file('world_population.svg')