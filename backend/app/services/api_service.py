from backend.app.services.arrange_service import ProductArrangeService
from backend.app.services.errors import ProductNotRecognisedError


class ShelfIdentificationService:
    def __init__(self, layout2D):
        self.rows = len(layout2D)
        self.columns = len(layout2D[0])
        self.layout2D = layout2D
        self.product_arrangements = list()
        self.grouped = [[False for col in range(self.columns)] for row in range(self.rows)]

    def initialise_products(self):
        product_list = self.get_unique_products()
        products_count = len(product_list)
        for i in range(products_count):
            pass

    def get_unique_products(self):
        products_set = set()
        for row in range(self.rows):
            for col in range(self.columns):
                products_set.add(self.layout2D[row][col])
        return list(products_set)

    def identify_products_arrangements(self, shelf_identify_obj):
        for row in range(self.rows):
            for col in range(self.columns):
                if not self.grouped[row][col]:
                    arrangement = self.get_product_arrangement(row, col, shelf_identify_obj)
                    self.add_product_arrangement(arrangement)
        return self.product_arrangements

    def add_product_arrangement(self, arrangement):
        self.product_arrangements.append(arrangement)

    def get_product_arrangement(self, row, col, shelf_identify_obj):
        print("The product : " + self.layout2D[row][col])
        try:
            arrange_service = ProductArrangeService(shelf_identify_obj, self.layout2D[row][col])
        except Exception as e:
            return ProductNotRecognisedError(self.layout2D[row][col],str(e))
        arrangement = arrange_service.find_pattern(row, col)
        return arrangement
