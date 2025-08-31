run-contact:
	PYTHONPATH=contact_management/src fastapi dev contact_management/src/api/contact_management_api.py

run-company:
	fastapi dev company_management/src/api/company_management_api.py

run-activity-task:
	fastapi dev activity_task_management/src/api/activity_task_management_api.py

run-sales:
	fastapi dev sales_management/src/api/sales_management_api.py
