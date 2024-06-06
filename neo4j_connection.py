
import os
from neo4j import GraphDatabase
def read_config(file_path):
    config = {}
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line and not line.startswith('#'):
                key, value = line.split('=', 1)
                config[key] = value
    return config

config = read_config('Neo4j-3bfd8ebc-Created-2024-06-04.txt')

URI = config['NEO4J_URI']
AUTH = (config['NEO4J_USERNAME'], config['NEO4J_PASSWORD'])

with GraphDatabase.driver(URI, auth=AUTH) as driver:
    driver.verify_connectivity()

