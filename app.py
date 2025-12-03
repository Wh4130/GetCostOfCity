from fastapi import FastAPI, BackgroundTasks
import uvicorn
import logging

from scripts import Obj, GetLivingExpenses


logger = logging.getLogger("uvicorn")
app = FastAPI()

# *** ---------------------------------------------------------------------------------------------------------
# --- APIs

@app.post("/source_html")
def get_html(doc: Obj):
    result_json = GetLivingExpenses.scrape(doc)
    return {"result": result_json}

@app.post("/expenses")
def get_living_expenses(doc: Obj):
    result_json = GetLivingExpenses.RUN(doc)
    return result_json

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)