import platform
import random
import requests
import yaml
from github import Github

# Favorite standard lib features
# https://twitter.com/driscollis/status/1511322675725189127

# Platform
print(platform.python_version())

# Random
for _ in range(10):
  print(random.randrange(0,9))

# Open a YAML file
with open('repos.yml', 'r') as file:
    data = yaml.safe_load(file)

from replit import db

for entry in data:
  print(data['repos'])
  db['repos'] = data['repos']

value = db["repos"]
  
#split
#datetime
#re
#itertools


