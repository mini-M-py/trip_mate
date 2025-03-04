from fastapi import HTTPException, APIRouter, Depends, Query, status, Form
from sqlalchemy.orm import Session
from typing import Annotated, List
from .. import schemas, model
from ..database import get_db

router = APIRouter(
    tags=["Plan"],
    prefix="/plan"
    )


@router.post('/create/{id}', status_code=status.HTTP_201_CREATED, response_model= schemas.plan_out)
def create_plan(plan: Annotated[schemas.create_plan, Form()], id: int, db:Session = Depends(get_db)): 
       new_plan = model.Plan(guide_id = id, title = plan.title, discription = plan.discription, 
                             tour_type = plan.tour_type, transportation = plan.transportation,
                             price = plan.price) 
        
       db.add(new_plan)
       db.commit()

       return new_plan
