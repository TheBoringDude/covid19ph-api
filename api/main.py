from .crawler import Crawler
from datetime import datetime
from enum import Enum
from fastapi import FastAPI, Header, Request, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(docs_url=None, redoc_url=None)

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


class DataModel(str, Enum):
    confirmed = "confirmed"
    active = "active"
    suspected = "suspected"
    severe = "severe"
    critical = "critical"
    recovered = "recovered"
    deaths = "deaths"
    fatality_rate = "fatality_rate"
    total = "all"


# function
async def get_data():
    crawler = Crawler()
    return await crawler.get_all()


@app.get("/")
async def root(request: Request):
    data = await get_data()
    return templates.TemplateResponse("index.html", {"request": request, "data": data, "datetime": datetime.now()})


@app.get("/api/cases/{case_name}")
async def read_case(case_name: str):
    if case_name == DataModel.confirmed:
        return {
            "Info": "PH CoVid-19 Data",
            "Confirmed_Cases": {"total": get_data()["confirmed"]},
            "current_time": datetime.now(),
        }

    elif case_name == DataModel.active:
        return {
            "Info": "PH CoVid-19 Data",
            "Active_Cases": {"total": get_data()["active"]},
            "current_time": datetime.now(),
        }

    elif case_name == DataModel.suspected:
        return {
            "Info": "PH CoVid-19 Data",
            "Suspected_Cases": {"total": get_data()["suspected"]},
            "current_time": datetime.now(),
        }

    elif case_name == DataModel.severe:
        return {
            "Info": "PH CoVid-19 Data",
            "Severe_Cases": {"total": get_data()["severe"]},
            "current_time": datetime.now(),
        }

    elif case_name == DataModel.critical:
        return {
            "Info": "PH CoVid-19 Data",
            "Critical_Cases": {"total": get_data()["critical"]},
            "current_time": datetime.now(),
        }

    elif case_name == DataModel.recovered:
        return {
            "Info": "PH CoVid-19 Data",
            "Recovered_Cases": {"total": get_data()["recovered"]},
            "current_time": datetime.now(),
        }

    elif case_name == DataModel.deaths:
        return {
            "Info": "PH CoVid-19 Data",
            "Deaths_Cases": {"total": get_data()["deaths"]},
            "current_time": datetime.now(),
        }

    elif case_name == DataModel.fatality_rate:
        return {
            "Info": "PH CoVid-19 Data",
            "Fatality_Rate": {"total": get_data()["fatality_rate"]},
            "current_time": datetime.now(),
        }

    elif case_name == DataModel.total:
        return {
            "country": "Philippines",
            "country_code": "PH",
            "current_time": datetime.now(),
            "cases": get_data(),
            "api_info": "This is just a simple API on the Summary of Cases of COVID-19 in the Philippines.",
        }

    return {"Info": "No Data Found"}


@app.get("/api")
async def api_info():
    return {
        "api_info": "This is just a simple API on the Summary of Cases of COVID-19 in the Philippines."
    }