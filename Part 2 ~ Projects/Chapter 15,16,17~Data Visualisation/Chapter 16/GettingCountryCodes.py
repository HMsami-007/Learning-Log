# Try importing from the direct plugin package paths
try:
    from pygal_maps_world.maps import COUNTRIES
except ImportError:
    try:
        from pygal_maps_world.i18n import COUNTRIES
    except ImportError:
        from pygal.maps.world import COUNTRIES

def GetCountryCode(country_name):
    # Print out the sorted codes
    for code,name in COUNTRIES.items():
        if name==country_name:
            return code
    return None
    
