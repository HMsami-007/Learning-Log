users={
    'aeinstein':{
        'first':'albert',
        'last':'einstein',
        'location':'princeton'
        },
    'mcurie':{
        'first':'marie',
        'last':'curie',
        'location':'paris'
        }
    }

for username,user_info in users.items():
    print(username)
    print(user_info['first'])
    print(user_info['last'])
    print("")

