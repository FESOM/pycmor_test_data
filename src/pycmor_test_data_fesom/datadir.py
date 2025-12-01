"""Data directory fixtures for FESOM models.

This module provides fixtures for accessing FESOM model run data,
using the BaseModelRun pattern for consistency.
"""

import pytest


@pytest.fixture(scope="session")
def fesom_2p6_datadir(fesom_2p6_model_run):
    """Data directory for FESOM 2.6.

    Returns stub data by default, or real data if:
    1. The PYCMOR_USE_REAL_TEST_DATA environment variable is set
    2. The real_data pytest marker is present

    Returns
    -------
    Path
        Path to the data directory
    """
    return fesom_2p6_model_run.datadir


@pytest.fixture(scope="session")
def fesom_dev_datadir(fesom_dev_model_run):
    """Data directory for FESOM dev.

    Returns stub data by default, or real data if:
    1. The PYCMOR_USE_REAL_TEST_DATA environment variable is set
    2. The real_data pytest marker is present

    Returns
    -------
    Path
        Path to the data directory
    """
    return fesom_dev_model_run.datadir
