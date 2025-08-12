from fastapi import FastAPI,status,HTTPException,Path
from fastapi.responses import JSONResponse
import random

app = FastAPI()

list_costs = [
    {"id":1,"description":"Housing","price":14.56},
    {"id":2,"description":"Food","price":19.55},
    {"id":3,"description":"Health","price":16.33},
    {"id":4,"description":"Kids","price":17.44},
    {"id":5,"description":"Pets","price":22.52},
    {"id":6,"description":"Personal Development","price":12.66},
    {"id":7,"description":"Technology","price":11.33},
    {"id":8,"description":"Giving","price":99.00},
]


#    اگر صفحه اصلی را باز کرده بود
@app.get("/")
def root():
    content={"message": "This is a first project"}
    return JSONResponse(content=content,status_code=status.HTTP_202_ACCEPTED)

#    لیست همه هزینه ها 
@app.get("/costs",status_code=status.HTTP_201_CREATED)
def retrieve_cost_list():
    return list_costs


# اضافه کردن به لیست هزینه ها
@app.post("/costs")
def create_new_cost(description:str,Price:float):
    max_id = max(list_costs, key=lambda d: d['id'])
    max_id=max_id['id']+1
    cost_obj={"id":max_id,"description":description,"price":Price}
    list_costs.append(cost_obj)
    raise HTTPException(status_code=status.HTTP_201_CREATED,detail="New Cost Added")    
    

# جستجوی هزینه بر اساس شناسه
@app.get("/costs/{cost_id}")
def retrieve_cost_list_detail(cost_id:int):
    for xx in list_costs:
        if xx["id"] == cost_id:
            return xx["description"],xx["price"]
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Cost id Not found")    
    
# برای بروز رسانی هزینه بر اساس شناسه
@app.put("/cost/{cost_id}")
def Update_cost_detail(cost_id:int,description:str,price:float,status_code=status.HTTP_200_OK ):
    for item in list_costs:
        if item["id"] == cost_id:
            item["description"]=description
            item["price"]=price
            return item
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Object Not found")    

#برای حذف آیتم بر اساس شناسه 
@app.delete("/cost/{cost_id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_cost(cost_id:int):
    for item in list_costs:
        if item["id"] == cost_id:
            list_costs.remove(item)
            return JSONResponse(content={"detail":"Object removed successfully"},status_code=status.HTTP_200_OK)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Object Not found")    
