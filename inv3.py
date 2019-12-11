#!/usr/bin/env python
import json

d = {"grupa1": {"hosts": ['server30.example.com', 'amaster1.example.com'],"vars": {"trabant": "jest"}},"_meta": {"hostvars": {"amaster1.example.com": {"trabant": "nie ma","auto": " o to to","ansible_port":22,"ansible_user":"root","ansible_password":"1","become_method":"sudo"}}}}

print(json.dumps(d))
