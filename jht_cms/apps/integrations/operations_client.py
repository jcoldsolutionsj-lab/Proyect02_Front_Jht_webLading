from .base_client import BaseAPIClient, APIClientError

class OperationsClient(BaseAPIClient):
    """
    Cliente específico para las operaciones logísticas.
    Usa el backend FastAPI para consultar tracking y gestionar órdenes.
    """

    def get_tracking_info(self, tracking_number: str):
        """
        Consulta el estado de una orden por su número de tracking.
        """
        try:
            return self._request('GET', f'/tracking/{tracking_number}')
        except APIClientError:
            # Retorna un error genérico o estructura vacía en caso de fallo
            return {"error": "No se pudo obtener la información de tracking."}

    def list_recent_orders(self, limit: int = 10):
        """
        Obtiene las órdenes recientes para mostrar en el panel de control.
        """
        try:
            return self._request('GET', '/orders', params={'limit': limit})
        except APIClientError:
            return []

    def update_order_status(self, order_id: str, new_status: str, notes: str = ""):
        """
        Actualiza el estado de una orden.
        """
        payload = {
            "status": new_status,
            "notes": notes
        }
        try:
            return self._request('POST', f'/orders/{order_id}/status', json=payload)
        except APIClientError as e:
            return {"error": str(e)}
