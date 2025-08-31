class ContactManagementAPIResponse:
    def __init__(self, contact_id: str, success:bool=True, data: dict={}, message: str=""):
        self.contact_id = contact_id
        self.success = success
        self.data = data
        self.message = message
    
    def response(self):
        return {
            "contact_id": self.contact_id,
            "success": self.success,
            "data": self.data,
            "message": self.message
        }