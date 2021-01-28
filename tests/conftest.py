import pytest

@pytest.fixture(params=[3])
def x(request):
    return request.param