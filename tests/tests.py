"""
KMeans tests.
"""
from src.k_means import KMeans


def test_instantiate():
    """
    Test instantiation.
    """
    assert isinstance(KMeans(3), KMeans)
