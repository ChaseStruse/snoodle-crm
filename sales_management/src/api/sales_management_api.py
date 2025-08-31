from fastapi import FastAPI

app = FastAPI()


@app.get("/sales/{deal_id}")
def get_deal_by_id(deal_id: int):
    return {
        "body": {
            "deal_id": deal_id
        }
    }