from fastapi import FastAPI

app = FastAPI()


@app.get("/company/{company_id}")
def get_company_by_id(company_id: int):
    return {
        "body": {
            "company_id": company_id
        }
    }

