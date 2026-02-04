#\!/usr/bin/env python3
"""PROTOCOL ZERO: Qdrant Memory Initialization"""

import os
import requests
from typing import List, Dict

QDRANT_URL = os.getenv('QDRANT_HOST', 'http://localhost:6333')

def init_collections():
    """Initialize Qdrant collections for the system"""
    
    collections = [
        {
            'name': 'agent_memory',
            'vector_size': 1024,  # mxbai-embed-large
            'distance': 'Cosine'
        },
        {
            'name': 'research_cache',
            'vector_size': 1024,
            'distance': 'Cosine'
        },
        {
            'name': 'code_reviews',
            'vector_size': 1024,
            'distance': 'Cosine'
        }
    ]
    
    for coll in collections:
        name = coll['name']
        
        # Check if exists
        resp = requests.get(f'{QDRANT_URL}/collections/{name}')
        if resp.status_code == 200:
            print(f'Collection {name} already exists')
            continue
        
        # Create collection
        payload = {
            'vectors': {
                'size': coll['vector_size'],
                'distance': coll['distance']
            }
        }
        
        resp = requests.put(f'{QDRANT_URL}/collections/{name}', json=payload)
        if resp.status_code == 200:
            print(f'Created collection: {name}')
        else:
            print(f'Failed to create {name}: {resp.text}')

def list_collections():
    """List all collections"""
    resp = requests.get(f'{QDRANT_URL}/collections')
    if resp.status_code == 200:
        data = resp.json()
        print('Collections:')
        for coll in data.get('result', {}).get('collections', []):
            print(f'  - {coll["name"]}')
    else:
        print('Failed to list collections')

if __name__ == '__main__':
    print('Initializing Qdrant collections...')
    init_collections()
    print()
    list_collections()
