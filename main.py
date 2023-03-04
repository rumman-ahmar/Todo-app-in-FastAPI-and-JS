import json
from fastapi import FastAPI, Depends, Request, Response
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from database.configurations import init_db, db_session
from database.schema import ItemSchema
from database.models import Item


# configure fastapi
app = FastAPI()
# configure static route
app.mount("/static", StaticFiles(directory="static"), name="static")

# configure template
templates = Jinja2Templates(directory="templates")


@app.on_event("startup")
def on_startup():
    init_db()


@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse(
        "index.html", {"request": request}
        )


##########################
# TODO APIs
##########################

# API get endpoint
@app.get("/api/todo")
def getItems(session: Session = Depends(db_session)):
    items = session.query(Item).all()
    return items


# API post endpoint
@app.post("/api/todo")
def addItem(item: ItemSchema, session: Session = Depends(db_session)):
    todoitem = Item(task=item.task)
    session.add(todoitem)
    session.commit()
    session.refresh(todoitem)
    return todoitem


# API put endpoint
@app.put("/api/todo/{id}")
def updateItem(id: int, item: ItemSchema,
               session: Session = Depends(db_session)):
    todoitem = session.query(Item).get(id)
    if todoitem:
        todoitem.task = item.task
        session.commit()
        session.close()
        response = json.dumps({"msg": "Item has been updated."})
        return Response(
            content=response, media_type='application/json', status_code=200
            )
    else:
        response = json.dumps({"msg": "Item not found"})
        return Response(
            content=response, media_type='application/json', status_code=404
            )


# API delete endpoint
@app.delete("/api/todo/{id}")
def deleteItem(id: int, session: Session = Depends(db_session)):
    todoitem = session.query(Item).get(id)
    if todoitem:
        session.delete(todoitem)
        session.commit()
        session.close()
        response = json.dumps({"msg": "Item has been deleted."})
        return Response(
            content=response, media_type='application/json', status_code=200
            )
    else:
        response = json.dumps({"msg": "Item not found"})
        return Response(
            content=response, media_type='application/json', status_code=404
            )
