import pandas as pd
import numpy as np
import pytest

from shape import shape_shifter

k = pd.DataFrame([1, 2, 3])

print(shape_shifter(k))

def test_shape_shifter_numpy():
    # test con un array NumPy
    x = np.array([1, 2, 3])
    assert (shape_shifter(x) == [1, 2, 3]).all()
    

def test_shape_shifter_list():
    # test con una lista
    x = [1, 2, 3]
    assert (shape_shifter(x) == [1, 2, 3]).all()
    

def test_shape_shifter_series():
    # test con una serie di Pandas
    x = pd.Series([1, 2, 3])
    assert (shape_shifter(x) == [1, 2, 3]).all()
    

def test_shape_shifter_dataframe():
    # test con un dataframe di Pandas
    x = pd.DataFrame([1, 2, 3])
    assert (shape_shifter(x) == [1, 2, 3]).all()
    

def test_shape_shifter_invalid_tipologia():
    # test con un valore non valido per tipologia
    x = [1, 2, 3]
    with pytest.raises(NotImplementedError):
        shape_shifter(x, tipologia='non valido')

def test_shape_shifter_invalid_dimensions():
    # test con un dataframe di Pandas con più di una colonna
    x = pd.DataFrame([[1, 2], [3, 4], [5, 6]])
    with pytest.raises(ValueError):
        shape_shifter(x)
