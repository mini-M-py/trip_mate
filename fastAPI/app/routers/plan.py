from fastapi import HTTPException, APIRouter, Depends, Query, status, Form
from sqlalchemy.orm import Session
from typing import Annotated, List
from .. import schemas, model
from ..database import get_db

router = APIRouter(
    tags=["Plan"],
    prefix="/plan"
    )


@router.post('/create/{id}', status_code=status.HTTP_201_CREATED)
def create_plan(plan: Annotated[schemas.create_plan, Form()], id: int ): 
       new_plan = model.Plan(guide_id = id, title = plan.title, discription = plan.discription, 
                             tour_type = plan.tour_type, transportation = plan.transportation,
                             price = plan.price) 

       return new_plan
