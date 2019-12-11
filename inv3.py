import json

d = {"grupa1": {"hosts": ['server30.example.com', 'server.example.com'],"vars": {"trabant": "jest"}},"_meta": {"hostvars": {"server30.example.com": {"trabant": "nie ma","auto": " o to to"}}}}

print(json.dumps(d))
