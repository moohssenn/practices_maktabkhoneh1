from fastapi import FastAPI,status,HTTPException,Path
from fastapi.responses import JSONResponse
from schemas import CostsCreateSchema,CostsResponseSchema,CostsUpdateSchema
from typing import List
from contextlib import asynccontextmanager
from database import Base,engine



@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Application statup")
    Base.metadata.create_all(engine)
    yield
    print("Application shutdown")



app = FastAPI(lifespan=lifespan)

costs_list = [
    {"id":1,"description":"Housing","price":14.56},
    {"id":2,"description":"Food","price":19.55},
    {"id":3,"description":"Health","price":16.33},
    {"id":4,"description":"Kids","price":17.44},
    {"id":5,"description":"Pets","price":22.52},
    {"id":6,"description":"personalDevelopment","price":12.66},
    {"id":7,"description":"Technology","price":11.33},
    {"id":8,"description":"Giving","price":99.00},
]


#    لیست همه هزینه ها 
@app.get("/costs",response_model=List[CostsResponseSchema],status_code=status.HTTP_200_OK)
def retrieve_cost_list(q : int | None=None):
    if q:
        return [item for item in costs_list if item["id"] == q]
    return costs_list


# اضافه کردن به لیست هزینه ها
@app.post("/costs",status_code=status.HTTP_201_CREATED,response_model=CostsResponseSchema)
def create_new_cost(costs : CostsCreateSchema):
    max_id = max(costs_list, key=lambda d: d['id'])
    max_id=max_id['id']+1
    cost_obj={"id":max_id,"description":costs.description,"price":costs.price}
    costs_list.append(cost_obj)
    #raise HTTPException(status_code=status.HTTP_201_CREATED,detail="New Cost Added")    
    return cost_obj
    

# جستجوی هزینه بر اساس شناسه
@app.get("/costs/{cost_id}",response_model=CostsResponseSchema)
def retrieve_cost_list_detail(cost_id:int = Path(title="object id")):
    for item in costs_list:
        if item["id"] == cost_id:
            return item
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Cost id Not found")    
    
# برای بروز رسانی هزینه بر اساس شناسه
@app.put("/cost/{cost_id}",response_model=CostsResponseSchema)
def Update_cost_detail(costs:CostsUpdateSchema, cost_id:int,status_code=status.HTTP_200_OK ):
    for item in costs_list:
        if item["id"] == cost_id:
            item["description"]=costs.description
            item["price"]=costs.price
            return item
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Object Not found")    

#برای حذف آیتم بر اساس شناسه 
@app.delete("/cost/{cost_id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_cost(cost_id:int):
    for item in costs_list:
        if item["id"] == cost_id:
            costs_list.remove(item)
            return JSONResponse(content={"detail":"Object removed successfully"},status_code=status.HTTP_200_OK)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Object Not found")    
