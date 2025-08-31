from fastapi import FastAPI

app = FastAPI()


@app.get("/activity/{activity_id}")
def get_activity_by_id(activity_id: int):
    return {
        "body": {
            "activity_id": activity_id
        }
    }


@app.get("/task/{task_id}")
def get_task_by_id(task_id: int):
    return {
        "body": {
            "task_id": task_id
        }
    }