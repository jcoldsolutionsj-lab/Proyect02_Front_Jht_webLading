import requests
from django.conf import settings

class APIClientError(Exception):
    pass

class BaseAPIClient:
    """
    Cliente base para conectar con la API FastAPI de Operaciones de JHT.
    Maneja la autenticación básica y los requests.
    """
    def __init__(self):
        self.base_url = getattr(settings, 'OPERATIONS_API_URL', 'http://localhost:8001/api/v1')
        self.api_key = getattr(settings, 'OPERATIONS_API_KEY', '')

    def _get_headers(self):
        return {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

    def _request(self, method, endpoint, **kwargs):
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        headers = self._get_headers()
        
        # Merge custom headers if provided
        if 'headers' in kwargs:
            headers.update(kwargs.pop('headers'))
            
        try:
            response = requests.request(method, url, headers=headers, **kwargs)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            # Aquí se puede agregar logging
            raise APIClientError(f"Error calling {url}: {str(e)}")
