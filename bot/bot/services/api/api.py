from .categories import CategoriesAPI
from .products import ProductsAPI
from .files import FilesAPI
from .feedbacks import FeedbacksAPI
from .orders import OrdersAPI

class API(CategoriesAPI, ProductsAPI, FilesAPI, FeedbacksAPI, OrdersAPI):
    BASE_URL = "http://127.0.0.1:8000"