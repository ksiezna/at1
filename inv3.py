#!/usr/bin/env python
import json

d = {"grupa1": {"hosts": ['server30.example.com', 'server.example.com'],"vars": {"trabant": "jest"}},"_meta": {"hostvars": {"server30.example.com": {"trabant": "nie ma","auto": " o to to","ansible_port":22,"ansible_user":"mat","become_method":"sudo"}}}}

print(json.dumps(d))
