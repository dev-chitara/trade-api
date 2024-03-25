from uuid import UUID
from typing import List

from fastapi import HTTPException, status, APIRouter, Depends
from sqlalchemy.orm import Session

from models.trades import Trade
from schemas.trades import CreateTradeSchema, UpdateTradeSchema, GetTradeSchema
from db_setup import get_db


router = APIRouter(tags=["Trade API"])


@router.get("/trades", status_code=status.HTTP_200_OK, response_model=List[GetTradeSchema])
async def fetch_trades(db: Session=Depends(get_db)):
    trade_objects = db.query(Trade).all()
    return trade_objects


@router.post("/trades", status_code=status.HTTP_201_CREATED, response_model=GetTradeSchema)
async def create_trade(trade_data: CreateTradeSchema, db: Session=Depends(get_db)):
    trade_object = Trade(**trade_data.model_dump())
    db.add(trade_object)
    db.commit()
    db.refresh(trade_object)
    return trade_object

@router.get("/trades/{trade_id}", status_code=status.HTTP_200_OK, response_model=GetTradeSchema)
async def get_trade(trade_id: UUID, db: Session=Depends(get_db)):
    trade_object = db.query(Trade).filter(Trade.id == trade_id).first()

    if trade_object is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"message": "Trade does not found!"}
        )
    
    return trade_object

@router.patch("/trades/{trade_id}", status_code=status.HTTP_200_OK, response_model=GetTradeSchema)
async def update_trade(trade_id: UUID, trade_data: UpdateTradeSchema, db: Session=Depends(get_db)):
    update_trade_data = trade_data.model_dump(exclude_none=True)

    trade_query = db.query(Trade).filter(Trade.id == trade_id)
    trade_object = trade_query.first()

    if trade_object is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"message": "Trade does not found!"}
        )
    
    trade_query.update(update_trade_data)
    db.commit()
    db.refresh(trade_object)
    return trade_object


@router.delete("/trades/{trade_id}", status_code=status.HTTP_200_OK)
async def delete_trade(trade_id: UUID, db: Session=Depends(get_db)):
    trade_object = db.query(Trade).filter(Trade.id == trade_id).first()

    if trade_object is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"message": "Trade does not found!"}
        )
    
    db.delete(trade_object)
    db.commit()
    return {"Deleted": True}