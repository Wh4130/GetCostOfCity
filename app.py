from fastapi import FastAPI, BackgroundTasks
import uvicorn
import logging

from scripts import GetLivingExpenses


logger = logging.getLogger("uvicorn")
app = FastAPI()

# *** --------------------------------------------------------------------------------------------------------
# --- APIs

@app.get("/source_html")
def get_html(city: str):
    result_json = GetLivingExpenses.scrape(city)
    return {"result": result_json}

@app.get("/expenses")
def get_living_expenses(city: str):
    result_json = GetLivingExpenses.RUN(city)
    return result_json

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)