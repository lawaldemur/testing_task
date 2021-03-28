from fastapi import FastAPI
from db_connect import Database


# init app and db connection
app = FastAPI()
db = Database()


# get list of all products
# output format: [id, sku, name, category, remains, reserved]
@app.post("/get")
async def get(col='id'):
	rows = db.get_rows(col)
	rows = [', '.join([str(i) for i in row]) for row in rows]
	return rows


# add a new product
@app.put("/add")
async def add(sku, name, category, remains):
    return db.add_row(sku, name, category, remains)


# delete one row by sku
@app.delete("/delete")
async def delete(sku):
    return db.delete_row(sku)


# update remains number
@app.put("/update_remains")
async def update_remains(sku, value):
    return db.update_remains(sku, value)


# reserve a product
@app.put("/reserve")
async def reserve(sku):
    return db.reserve(sku)


# unreserve a product
@app.put("/unreserve")
async def unreserve(sku):
    return db.reserve(sku, 0)
