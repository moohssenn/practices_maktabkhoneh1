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

@app.get("/")
def root():
    content={"message": "Hello World"}
    return JSONResponse(content=content,status_code=status.HTTP_202_ACCEPTED)

@app.get("/names",status_code=status.HTTP_201_CREATED)
def retrieve_names_list(q : str | None=None):
    if q:
        return [item for item in names_list if item["name"] == q]
    return names_list

@app.post("/names")
def create_name(name:str):
    name_obj={"id":random.randint(6,100),"name":name}
    names_list.append(name_obj)
    return name_obj



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

@app.get("/")
def root():
    return {"message": "Hello World"} 

@app.delete("/names/{name_id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_name(name_id:int):
    for item in names_list:
        if item["id"] == name_id:
            names_list.remove(item)
            return JSONResponse(content={"detail":"Object removed successfully"},status_code=status.HTTP_200_OK)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Object Not found")    
