
import os
from neo4j import GraphDatabase

URI = "neo4j+s://3bfd8ebc.databases.neo4j.io"
AUTH = ("neo4j", "bGUw5BwMn0kJ2OsqHtxMufcE60_7qRoOoytCvr2yyd4")

with GraphDatabase.driver(URI, auth=AUTH) as driver:
    driver.verify_connectivity()

