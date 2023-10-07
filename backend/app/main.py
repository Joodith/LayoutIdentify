from fastapi import FastAPI
from pydantic import BaseModel
from collections import defaultdict

from backend.app.services.api_service import ShelfIdentificationService
from backend.app.services.errors import ProductNotRecognisedError
main_app = FastAPI()

class Layout(BaseModel):
    array2D: list[list[str]]


@main_app.post("/shape_of_brand/")
async def shape_of_brand(layout: Layout):
    shelf_obj = ShelfIdentificationService(layout.array2D)
    print(shelf_obj.rows, shelf_obj.columns)
    product_arrangements = shelf_obj.identify_products_arrangements(shelf_obj)
    response = defaultdict(list)
    for arrangement in product_arrangements:
        if isinstance(arrangement, ProductNotRecognisedError):
            response[arrangement.product_repr] = [{
                "error_message": arrangement.error_msg
            }]
        else:
            response[arrangement.product_repr].append({
                "shape": arrangement.shape,
                "location": arrangement.location
            })
    return response
