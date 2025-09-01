class CompanyManagementAPIResponse:
    def __init__(self, company_id: str, success:bool=True, data: dict={}, message: str=""):
        self.company_id = company_id
        self.success = success
        self.data = data
        self.message = message
    
    def response(self):
        return {
            "company_id": self.company_id,
            "success": self.success,
            "data": self.data,
            "message": self.message
        }