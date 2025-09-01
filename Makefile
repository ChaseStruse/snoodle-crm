run-contact:
	PYTHONPATH=contact_management/src fastapi dev contact_management/src/api/contact_management_api.py

run-company:
	PYTHONPATH=company_management/src fastapi dev company_management/src/api/company_management_api.py

run-activity-task:
	PYTHONPATH=activity_task_management/src fastapi dev activity_task_management/src/api/activity_task_management_api.py

run-sales:
	PYTHONPATH=sales_management/src fastapi dev sales_management/src/api/sales_management_api.py

run-ui: 
	PYTHONPATH=crm_interface/src python3 crm_interface/src/views/contact_view.py
