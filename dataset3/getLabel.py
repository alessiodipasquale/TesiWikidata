import json
import requests
import os
import time


query = """
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
PREFIX wd: <http://www.wikidata.org/entity/> 
SELECT  *
WHERE {
        wd:%s rdfs:label ?label .
        FILTER (langMatches( lang(?label), "EN" ) )
      } 
LIMIT 1
""" % s