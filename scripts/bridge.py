#!/usr/bin/env python3
"""PROTOCOL ZERO: n8n API Bridge v2"""

import os
import json
import time
import argparse
from typing import Optional, Dict, Any, List

try:
    import requests
except ImportError:
    print('Installing requests...')
    os.system('pip3 install requests')
    import requests

class N8nBridge:
    def __init__(self, api_url: str = None, api_key: str = None, verbose: bool = False):
        self.api_url = api_url or os.getenv('N8N_API_URL', 'http://localhost:5678/api')
        self.api_key = api_key or os.getenv('N8N_API_KEY', '')
        self.verbose = verbose
        self.session = requests.Session()
        if self.api_key:
            self.session.headers.update({'X-N8N-API-KEY': self.api_key})
        self.session.headers.update({'Content-Type': 'application/json'})

    def log(self, msg: str):
        if self.verbose:
            print(f'[DEBUG] {msg}')

    def _retry_request(self, func, *args, max_retries: int = 3, **kwargs):
        for attempt in range(max_retries):
            try:
                return func(*args, **kwargs)
            except requests.exceptions.RequestException as e:
                self.log(f'Attempt {attempt + 1} failed: {e}')
                if attempt == max_retries - 1:
                    raise
                time.sleep(2 ** attempt)
        return None

    def health_check(self) -> bool:
        try:
            url = self.api_url.replace('/api', '') + '/healthz'
            response = self.session.get(url, timeout=5)
            return response.status_code == 200
        except:
            return False

    def list_workflows(self) -> List[Dict]:
        try:
            response = self._retry_request(self.session.get, f'{self.api_url}/workflows')
            response.raise_for_status()
            return response.json().get('data', {}).get('workflows', [])
        except Exception as e:
            print(f'Failed to list workflows: {e}')
            return []

    def import_workflow(self, workflow_json: Any) -> Optional[Dict]:
        if isinstance(workflow_json, str):
            workflow_json = json.loads(workflow_json)
        try:
            response = self._retry_request(self.session.post, f'{self.api_url}/workflows/import', json=workflow_json)
            response.raise_for_status()
            result = response.json().get('data')
            name = result.get('name', 'Unknown') if result else 'Unknown'
            print(f'Imported workflow: {name}')
            return result
        except Exception as e:
            print(f'Failed to import workflow: {e}')
            return None

    def import_workflow_from_file(self, file_path: str) -> Optional[Dict]:
        try:
            with open(file_path, 'r') as f:
                return self.import_workflow(json.load(f))
        except FileNotFoundError:
            print(f'File not found: {file_path}')
            return None

    def activate_workflow(self, workflow_id: str) -> bool:
        try:
            response = self._retry_request(self.session.patch, f'{self.api_url}/workflows/{workflow_id}', json={'active': True})
            response.raise_for_status()
            print(f'Activated workflow: {workflow_id}')
            return True
        except Exception as e:
            print(f'Failed to activate: {e}')
            return False

def main():
    import argparse
    parser = argparse.ArgumentParser(description='n8n API Bridge v2')
    parser.add_argument('action', choices=['health', 'list', 'import', 'activate'])
    parser.add_argument('--file', '-f')
    parser.add_argument('--id')
    parser.add_argument('--url', default='http://localhost:5678/api')
    parser.add_argument('--verbose', '-v', action='store_true')
    args = parser.parse_args()
    bridge = N8nBridge(api_url=args.url, verbose=args.verbose)
    if args.action == 'health':
        print('OK' if bridge.health_check() else 'FAILED')
    elif args.action == 'list':
        for wf in bridge.list_workflows():
            status = '[ACTIVE]' if wf.get('active') else '[INACTIVE]'
            print(f'  {status} {wf.get("id", "N/A"):40} {wf.get("name", "Unknown")}')

if __name__ == '__main__':
    main()
