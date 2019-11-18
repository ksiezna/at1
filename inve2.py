#!/usr/bin/env python
import json


d = {
    'descpacio': {
        'hosts': ['srespacito', 'nietakszybko'],
        'vars': {
            'polski': 'hahahahha',
            'espanol': 'jajajaja'
            }
        }
    }

print(json.dumps(d))
