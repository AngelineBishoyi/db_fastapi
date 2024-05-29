from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from db_conn import connect_to_database
import uvicorn
app = FastAPI()


class Item(BaseModel):
    
    name: str
    address: str

conn = connect_to_database()


# Route to create an item
@app.post("/items/", response_model=Item)
def create_item(item: Item):
    cursor = conn.cursor()
    query = "INSERT INTO std_details (name, address) VALUES (%s, %s)"
    cursor.execute(query, (item.name, item.address))
    conn.commit()
    cursor.close()
    return item



@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: Item):
    cursor = conn.cursor()
    query = "UPDATE items SET name=%s, description=%s WHERE id=%s"
    cursor.execute(query, (item.name, item.description, item_id))
    conn.commit()
    cursor.close()

    return item

@app.get("/items/", response_model=list[Item])
def read_items():
    cursor = conn.cursor()
    query = "SELECT name, address FROM std_details"
    cursor.execute(query)
    items = cursor.fetchall()
    cursor.close()
    
    result = []
    for item in items:
        result.append({
            "name": item[0],
            "address": item[1]
        })
    
    return result




if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=4000)