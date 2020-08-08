import yaml
with open('user.yml.txt','r') as file:
    data = yaml.safe_load(file)
    user = data['user']
    print(user['name'])
    for role in user['roles']:
        print(role)