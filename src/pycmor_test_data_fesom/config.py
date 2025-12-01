"""Configuration fixtures for FESOM models."""

import pytest


@pytest.fixture
def fesom_2p6_model_run(tmp_path_factory, request):
    """FESOM 2.6 model run instance.

    Returns
    -------
    Fesom2p6ModelRun
        Model run instance with data and config access
    """
    from pycmor_test_data_fesom.fesom_2p6 import Fesom2p6ModelRun

    use_real = Fesom2p6ModelRun.should_use_real_data(request)
    return Fesom2p6ModelRun.from_module(__file__, use_real=use_real, tmp_path_factory=tmp_path_factory)


@pytest.fixture
def fesom_dev_model_run(tmp_path_factory, request):
    """FESOM dev model run instance.

    Returns
    -------
    FesomDevModelRun
        Model run instance with data and config access
    """
    from pycmor_test_data_fesom.fesom_dev import FesomDevModelRun

    use_real = FesomDevModelRun.should_use_real_data(request)
    return FesomDevModelRun.from_module(__file__, use_real=use_real, tmp_path_factory=tmp_path_factory)
