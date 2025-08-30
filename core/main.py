from fastapi import FastAPI,status,HTTPException,Path,Depends,Query
from fastapi.responses import JSONResponse
from schemas import CostsCreateSchema,CostsResponseSchema,CostsUpdateSchema
from typing import List
from contextlib import asynccontextmanager
from database import Base,engine,get_db,Costs
from sqlalchemy import func
from sqlalchemy.orm import Session



@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Application statup")
    Base.metadata.create_all(engine)
    yield
    print("Application shutdown")

app = FastAPI(lifespan=lifespan)  

#    لیست همه هزینه ها 
@app.get("/costs",response_model=List[CostsResponseSchema],status_code=status.HTTP_200_OK)
def retrieve_cost_list(q : int | None= Query(alias="search",default=None),db:Session=Depends(get_db)):
    query = db.query(Costs)
    if q:
        query = query.filter_by(id=q)
    resualt = query.all()
    return resualt


# اضافه کردن به لیست هزینه ها
@app.post("/costs",status_code=status.HTTP_201_CREATED,response_model=CostsResponseSchema)
def create_new_cost(request : CostsCreateSchema,db:Session=Depends(get_db)):
    max_id = db.query(func.max(Costs.id)).scalar()
    if not max_id: max_id=0
    max_id = max_id+1

    new_cost=Costs(id=max_id,description=request.description,price=request.price)
    db.add(new_cost)
    db.commit()
    return new_cost
    

# جستجوی هزینه بر اساس شناسه
@app.get("/costs/{cost_id}",response_model=CostsResponseSchema)
def retrieve_cost_list_detail(cost_id:int = Path(title="object id") , db:Session=Depends(get_db)):
    cost = db.query(Costs).filter_by(id = cost_id).one_or_none()
    if cost:
        return cost
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Cost id Not found")    
    
# برای بروز رسانی هزینه بر اساس شناسه
@app.put("/cost/{cost_id}",response_model=CostsResponseSchema)
def Update_cost_detail(request:CostsUpdateSchema, cost_id:int,status_code=status.HTTP_200_OK , db:Session=Depends(get_db) ):
    cost = db.query(Costs).filter_by(id = cost_id).one_or_none()
    if cost:
        cost.description = request.description
        cost.price = request.price
        db.commit()
        db.refresh(cost)
        return cost
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Object Not found")    

#برای حذف آیتم بر اساس شناسه 
@app.delete("/cost/{cost_id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_cost(cost_id:int, db:Session=Depends(get_db)):
    cost = db.query(Costs).filter_by(id = cost_id).one_or_none()
    if cost:
        db.delete(cost)
        db.commit()
        return JSONResponse(content={"detail":"Object removed successfully"},status_code=status.HTTP_200_OK)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Object Not found")    
