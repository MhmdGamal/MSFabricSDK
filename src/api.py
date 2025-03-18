from sempy.fabric import list_workspaces, list_items, list_dataflows
from urllib.parse import urljoin
import requests
import json

class FabricAPIBase:
    def __init__(self, base_url=None, token=None):
        self.base_url = base_url or "https://api.fabric.microsoft.com/v1/"
        if token:
            self.token = token
        else:
            try:
                # Import notebookutils only if available
                from notebookutils.credentials import getToken
                self.token = getToken('pbi')
            except ImportError:
                raise ImportError(
                    "notebookutils is not available. Please provide a token manually when initializing FabricAPIBase."
                )

    def make_request(self, method='GET', endpoint=None, params=None, data=None):
        url = urljoin(self.base_url, endpoint)
        headers = {
            'Authorization': f'Bearer {self.token}',
            'Content-Type': 'application/json'
        }
        response = requests.request(
            method,
            url,
            headers=headers,
            params=params,
            data=json.dumps(data) if data else None
        )
        response.raise_for_status()
        return response.json()

    def GetAllWorkspaces(self):
        self.workspaces = list_workspaces()
        self.workspaces['Git_status'] = [
            self.make_request('GET', f'workspaces/{id}/git/connection')['gitConnectionState']
            for id in self.workspaces['Id']
        ]
        return self.workspaces  # DataFrame

    def GetFabricWorkspaces(self):
        self.workspaces = list_workspaces()
        self.workspaces['Git_status'] = [
            self.make_request('GET', f'workspaces/{id}/git/connection')['gitConnectionState']
            for id in self.workspaces['Id']
        ]
        self.fabric_workspaces_IDs = []
        for id in self.workspaces['Id']:
            if (('Lakehouse' in set(list_items(workspace=id)['Type'].values)) or
                ('DataPipeline' in set(list_items(workspace=id)['Type'].values)) or
                ('Warehouse' in set(list_items(workspace=id)['Type'].values)) or
                ('Notebook' in set(list_items(workspace=id)['Type'].values)) or
                (list_dataflows(id).shape[0] > 0)):
                self.fabric_workspaces_IDs.append(id)
        self.fabric_workspaces = self.workspaces[self.workspaces['Id'].isin(self.fabric_workspaces_IDs)]
        return self.fabric_workspaces

    def GetPowerBIWorkspaces(self):
        self.workspaces = list_workspaces()
        self.workspaces['Git_status'] = [
            self.make_request('GET', f'workspaces/{id}/git/connection')['gitConnectionState']
            for id in self.workspaces['Id']
        ]
        self.PowerBI_workspaces_IDs = []
        for id in self.workspaces['Id']:
            if not (('Lakehouse' in set(list_items(workspace=id)['Type'].values)) or
                    ('DataPipeline' in set(list_items(workspace=id)['Type'].values)) or
                    ('Warehouse' in set(list_items(workspace=id)['Type'].values)) or
                    ('Notebook' in set(list_items(workspace=id)['Type'].values)) or
                    (list_dataflows(id).shape[0] > 0)):
                self.PowerBI_workspaces_IDs.append(id)
        self.PowerBI_workspaces = self.workspaces[self.workspaces['Id'].isin(self.PowerBI_workspaces_IDs)]
        return self.PowerBI_workspaces

    def GetAllWarehouses(self):
        return list_items('Warehouse')

    def GetAllLakehouses(self):
        return list_items('Lakehouse')

    def GetWarehouseByID(self, ID):
        self.warehouses = list_items('Warehouse')
        return self.warehouses[self.warehouses['Id'] == ID]

    def GetWarehouseByName(self, Name):
        self.warehouses = list_items('Warehouse')
        return self.warehouses[self.warehouses['Display Name'] == Name]

    def GetLakehouseByID(self, ID):
        self.Lakehouses = list_items('Lakehouse')
        return self.Lakehouses[self.Lakehouses['Id'] == ID]

    def GetLakehouseByName(self, Name):
        self.Lakehouses = list_items('Lakehouse')
        return self.Lakehouses[self.Lakehouses['Display Name'] == Name]
