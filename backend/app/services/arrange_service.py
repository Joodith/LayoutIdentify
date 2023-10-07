from backend.app.config import PRODUCTS, Shapes, RowParams, ColumnParams
import math

MAX_VALUE = math.inf

TRAVERSALS = [(0, -1), (0, 1), (1, 0), (-1, 0)]
LEFT_MOVE = 0
RIGHT_MOVE = 1
BOTTOM_MOVE = 2
TOP_MOVE = 3


class ProductArrangeService:
    def __init__(self, shelf_identification_service, product_repr):
        if product_repr not in PRODUCTS:
            raise Exception("Product not recognised")
        self.product_name = PRODUCTS[product_repr]
        self.product_repr = product_repr
        self.top_left = (0, 0)
        self.top_right = (0, 0)
        self.bottom_left = (0, MAX_VALUE)
        self.bottom_right = (0, 0)
        self.shape = ""
        self.location = ""
        self.shelf_service = shelf_identification_service
        self.left_margins = set()
        self.right_margins = set()
        self.top_margins = set()
        self.bottom_margins = set()

    def is_valid_location(self, row, col):
        if 0 <= row < self.shelf_service.rows and 0 <= col < self.shelf_service.columns:
            return True
        return False

    def is_margin(self, adj_row, adj_col, target_product):
        if self.is_valid_location(adj_row, adj_col):
            if self.shelf_service.layout2D[adj_row][adj_col] == target_product:
                return False
        return True

    def update_bottom_left(self, row, col):
        cur_bt_row, cur_bt_col = self.bottom_left[0], self.bottom_left[1]
        if col < cur_bt_col:
            self.bottom_left = (row, col)
        elif col == cur_bt_col:
            if row > cur_bt_row:
                self.bottom_left = (row, col)

    def update_top_right(self, row, col):
        cur_top_row, cur_top_col = self.top_right[0], self.top_right[1]
        if col > cur_top_col:
            self.top_right = (row, col)
        elif col == cur_top_col:
            if row < cur_top_row:
                self.top_right = (row, col)

    def update_top_left(self, row, col):
        cur_top_row, cur_top_col = self.top_left[0], self.top_left[1]
        if row < cur_top_row:
            self.top_left = (row, col)
        elif row == cur_top_row:
            if col < cur_top_col:
                self.top_left = (row, col)

    def update_bottom_right(self, row, col):
        cur_bt_row, cur_bt_col = self.bottom_right[0], self.bottom_right[1]
        if row > cur_bt_row:
            self.bottom_right = (row, col)
        elif row == cur_bt_row:
            if col > cur_bt_col:
                self.bottom_right = (row, col)

    def trace_layout_for_pattern(self, row, col, target_product):
        self.shelf_service.grouped[row][col] = True
        for index, (row_incr, col_incr) in enumerate(TRAVERSALS):
            adj_row = row + row_incr
            adj_col = col + col_incr

            if self.is_margin(adj_row, adj_col, target_product):
                if index == LEFT_MOVE:
                    self.left_margins.add((row, col))
                    self.update_bottom_left(row, col)
                elif index == RIGHT_MOVE:
                    self.right_margins.add((row, col))
                    self.update_top_right(row, col)
                elif index == TOP_MOVE:
                    self.top_margins.add((row, col))
                    self.update_top_left(row, col)
                else:
                    self.bottom_margins.add((row, col))
                    self.update_bottom_right(row, col)
            else:
                if not self.shelf_service.grouped[adj_row][adj_col]:
                    self.trace_layout_for_pattern(adj_row, adj_col, target_product)

        return

    def find_pattern(self, row, col):
        target_product = self.shelf_service.layout2D[row][col]
        self.top_left = (row, col)
        self.trace_layout_for_pattern(row, col, target_product)
        # print(self.bottom_margins)
        self.assign_shape()
        self.assign_location_description()
        return self

    def has_perfect_margins(self):
        perfect_left = True if len({x[1] for i, x in enumerate(self.left_margins)}) == 1 else False
        perfect_right = True if len({x[1] for i, x in enumerate(self.right_margins)}) == 1 else False
        perfect_top = True if len({x[0] for i, x in enumerate(self.top_margins)}) == 1 else False
        perfect_bottom = True if len({x[0] for i, x in enumerate(self.bottom_margins)}) == 1 else False
        return perfect_left and perfect_top and perfect_right and perfect_bottom

    def is_regular_shape(self):
        return (self.top_left[0] == self.top_right[0]) and (self.bottom_left[0] == self.bottom_right[0]) and (
                self.top_left[1] == self.bottom_left[1]) and (self.top_right[1] == self.bottom_right[1]) and (
            self.has_perfect_margins()
        )

    def assign_shape(self):
        if self.is_regular_shape():
            width = (self.top_right[1] - self.top_left[1]) + 1
            height = (self.bottom_left[0] - self.top_left[0]) + 1
            if width == height:
                self.shape = Shapes.SQUARE
            elif width > height:
                self.shape = Shapes.HORIZONTAL_RECTANGLE
            else:
                self.shape = Shapes.VERTICAL_RECTANGLE

        else:
            self.shape = Shapes.POLYGON

    def assign_location_description(self):
        loc = ""
        row_param, col_param = None, None
        if (self.bottom_right[0] < self.shelf_service.rows // 2) or (
                self.top_left[0] == 0 and self.bottom_right[0] != self.shelf_service.rows - 1):
            row_param = RowParams.TOP
        elif (self.top_left[0] >= self.shelf_service.rows // 2) or (
                self.bottom_right[0] == self.shelf_service.rows - 1 and self.top_left[0] != 0):
            row_param = RowParams.BOTTOM
        else:
            if (self.bottom_right[0] - self.top_left[0]) + 1 != self.shelf_service.rows:
                row_param = RowParams.MIDDLE

        if self.top_right[1] < self.shelf_service.columns // 2:
            col_param = ColumnParams.LEFT
        elif self.bottom_left[1] >= self.shelf_service.columns // 2:
            col_param = ColumnParams.RIGHT
        # else:
        #     if row_param != RowParams.MIDDLE:
        #         col_param = ColumnParams.AROUND_MIDDLE
        if row_param != None:
            loc += row_param.name + " "
        if col_param != None:
            loc += col_param.name
        self.location = loc
