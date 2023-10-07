from fastapi.testclient import TestClient
from .sample_input_for_test import TEST_LAYOUTS, LAYOUT_WITH_UNRECOG_PROD, ARRANGE_WITH_UNRECOG_PRODUCT

from .main import main_app

client = TestClient(main_app)


def test_shape_of_brand():
    for test_layout in TEST_LAYOUTS:
        response = client.post(
            "/shape_of_brand/",
            json={"array2D": TEST_LAYOUTS[test_layout]["layout"]},
        )
        assert response.status_code == 200
        assert response.json() == TEST_LAYOUTS[test_layout]["response"]


def test_with_unrecognised_product():
    response = client.post(
        "/shape_of_brand/",
        json={"array2D": LAYOUT_WITH_UNRECOG_PROD},
    )
    assert response.status_code == 200
    assert response.json() == ARRANGE_WITH_UNRECOG_PRODUCT
