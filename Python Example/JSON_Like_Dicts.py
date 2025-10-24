# Work with nested dicts resembling JSON.
data = {"user": {"name": "Sam", "roles": ["admin","user"]}, "active": True}

def has_role(d, role):
    return role in d.get('user', {}).get('roles', [])

if __name__ == '__main__':
    print('Its Admin? ', has_role(data, 'admin'))
    print('is moderator? ', has_role(data, 'modarator'))