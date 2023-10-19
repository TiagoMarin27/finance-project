"""main module of finance Application."""
from typing import List
from fastapi import FastAPI, HTTPException

from finance_project.models.stocks import Stock

from finance_project.schemas.stock_schemas import StockSchema

from finance_project.database.database import SessionLocal


app = FastAPI()

def get_db():
    db= SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/stocks/get-stock/{stock_name}")
def get_stock_by_name(stock_name: str):
    for stock in stocks:
        if stock.name == stock_name:
            return stock
    # Si el stock no se encuentra, devuelve una respuesta de error
    raise HTTPException(status_code=404, detail="Stock no encontrado")

@app.get("/stocks")
def get_stocks():
    print(str(stocks))
    return stocks



@app.post("/stocks/create-stock")
def create_stocks(stock_body: StockSchema):
    stock = Stock(**stock_body.model_dump()) 
    stocks.append(stock)
