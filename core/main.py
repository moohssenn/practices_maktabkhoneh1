from fastapi import FastAPI,status,HTTPException,Path
from fastapi.responses import JSONResponse
import random

app = FastAPI()

names_list = [
    {"id":1,"name":"ali"},
    {"id":2,"name":"maryam"},
    {"id":3,"name":"mohsen"},
    {"id":4,"name":"aref"},
    {"id":5,"name":"reza"},
    {"id":6,"name":"reza"},
    {"id":7,"name":"reza"},
    {"id":8,"name":"reza"},
]


list_costs = [
    {"id":1,"description":"Housing","price":14.56},
    {"id":2,"description":"Food","price":19.55},
    {"id":3,"description":"Health","price":16.33},
    {"id":4,"description":"Kids","price":17.44},
    {"id":5,"description":"Pets","price":22.52},
    {"id":6,"description":"Personal Development","price":12.66},
    {"id":7,"description":"Technology","price":11.33},
    {"id":8,"description":"Giving","price":9.00},
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
    max_id= max_id+1
    

    #name_obj={"id":random.randint(6,100),"name":name}
    #names_list.append(name_obj)
    return max_id



@app.get("/names/{name_id}")
def retrieve_names_list_detail(name_id:int):
    for name in names_list:
        if name["id"] == name_id:
            return name["name"]
            
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Object Not found")    
    



@app.put("/names/{name_id}")
def Update_name_detail(name_id:int,name:str,status_code=status.HTTP_200_OK ):
    for item in names_list:
        if item["id"] == name_id:
            item["name"]=name
            return item
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Object Not found")    



@app.delete("/names/{name_id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_name(name_id:int):
    for item in names_list:
        if item["id"] == name_id:
            names_list.remove(item)
            return JSONResponse(content={"detail":"Object removed successfully"},status_code=status.HTTP_200_OK)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Object Not found")    
