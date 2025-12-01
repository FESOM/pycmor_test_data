"""Dataset fixtures for FESOM models.

This module provides xarray dataset fixtures that load FESOM data
using the BaseModelRun pattern.
"""

import pytest


@pytest.fixture(scope="session")
def fesom_2p6_ds(fesom_2p6_model_run):
    """Open FESOM 2.6 dataset with xarray.

    Returns
    -------
    xr.Dataset
        Opened dataset from the model run
    """
    return fesom_2p6_model_run.ds


@pytest.fixture(scope="session")
def fesom_dev_ds(fesom_dev_model_run):
    """Open FESOM dev dataset with xarray.

    Returns
    -------
    xr.Dataset
        Opened dataset from the model run
    """
    return fesom_dev_model_run.ds
