Introducing the Fabric Python SDK: Simplifying Fabric API Interactions with Sempy
🚀 A New Way to Interact with Fabric Using Python

As a data engineer working with Microsoft Fabric, you’ve probably spent time navigating APIs, managing authentication, and making repetitive API calls to fetch workspace details, pipelines, lakehouses, and more. Well, good news – those days are over!

We’ve built a Fabric Python SDK powered by the `Sempy` package, enabling seamless interaction with Fabric’s REST APIs. Whether you need to retrieve all workspaces, check pipeline statuses, or manage dataflows, this SDK has you covered.

🔧 Installation: Get Started in Seconds!
Before diving into the capabilities, let’s get it installed:
if you prefer a pre-packaged `.whl` file, simply import it into your Python environment and start using it like a pro!

📌 Key Features & How to Use Them
1️⃣ Workspaces Management
🔍 Get All Workspaces
Fetches a list of all Fabric workspaces along with their Git connection status.

```python

from your_sdk_module import FabricAPIBase
fabric = FabricAPIBase()
all_workspaces = fabric.GetAllWorkspaces( )
print(all_workspaces)

```



🏗️ Get Fabric-Specific Workspaces
Filters out workspaces that contain Fabric-related elements such as Lakehouses, Pipelines, Warehouses, or Notebooks.

```python

fabric_workspaces = fabric.GetFabricWorkspaces( )
print(fabric_workspaces)
```
📊 Get Power BI Workspaces
Retrieves only Power BI workspaces, excluding Fabric-related workspaces.

```python

powerbi_workspaces = fabric.GetPowerBIWorkspaces( )
print(powerbi_workspaces)
```
2️⃣ Lakehouses & Warehouses
🏡 Get All Lakehouses
Fetches all lakehouses available in Fabric.

```python

lakehouses = fabric.GetAllLakehouses( )
print(lakehouses)
```
Need to filter by **ID or Name**?

```python

lakehouse_by_id = fabric.GetLakehouseByID('your-lakehouse-id')
lakehouse_by_name = fabric.GetLakehouseByName('Lakehouse Name')
```

🏢 Get All Warehouses
Fetches all data warehouses in Fabric.

```python

warehouses = fabric.GetAllWarehouses( )
print(warehouses)
```
Need a specific one?

```python

warehouse_by_id = fabric.GetWarehouseByID('your-warehouse-id')
warehouse_by_name = fabric.GetWarehouseByName('Warehouse Name')
```
3️⃣ Data Pipelines & Jobs
🚀 Fetch Data Pipelines
Fetches all data pipelines within a given workspace.

```python

pipelines = fabric.FetchDataPipelines(workspace_id='your-workspace-id')
print(pipelines)
```
🏃 Fetch Pipeline Run Details
Retrieves all run details of a specific pipeline.

```python

pipeline_runs = fabric.FetchPipelineRunDetails('workspace-id', 'pipeline-id')
print(pipeline_runs)
```



🔍 Get Pipeline Details by Name
Fetches pipeline details by searching with the pipeline name.

```python

pipeline_details = fabric.GetPipelineDetailsByName('Pipeline Name')
print(pipeline_details)
```
⏳ Check Pipeline Run Status
Want to fetch all past runs?

```python

pipeline_statuses = fabric.GetPipelineAllRunsStatuses('Workspace Name', 'Pipeline Name')
print(pipeline_statuses)
```
Only need the **latest** Run?

```python

last_run_status = fabric.GetPipelineLastRunStatus('Workspace Name', 'Pipeline Name')
print(last_run_status)
```

4️⃣ Role Assignments & Access Control
🔑 Get Workspace Role Assignments
Retrieves the role assignments for a specific workspace, useful for managing permissions.

```python

roles = fabric.GetWorkspaceRoleAssignments('workspace-id')
print(roles)
```


🎯 Why Use This SDK?
✅ Saves Development Time – No need to manually craft API requests.
✅ Easier Data Exploration – Quickly retrieve and analyze Fabric elements.
✅ Structured API Responses – Everything is returned in a clean DataFrame.
✅ Handles Authentication Automatically – No need to worry about token management.
✅ Scalable & Extendable – You can build on top of it for custom needs.

💡 Final Thoughts
This SDK was built to simplify interaction with Microsoft Fabric and improve developer productivity. Whether you’re a Data Engineer, BI Developer, or ML Engineer, this tool is designed to help you focus on insights rather than API complexities.

🚀 Give it a spin and let us know your thoughts! If you have feedback or feature requests, we’d love to hear them!

🔗 Official Documentation: [Microsoft Sempy Fabric API](https://learn.microsoft.com/en-us/python/api/semantic-link-sempy/sempy.fabric?view=semantic-link-python)
