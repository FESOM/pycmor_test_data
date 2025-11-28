# pycmor-test-data-fesom

FESOM test datasets for pycmor tutorial and testing.

## Installation

```bash
pip install pycmor-test-data-fesom
```

## Usage

Once installed, the datasets are automatically available via `pycmor.tutorial`:

```python
import pycmor.tutorial as tutorial

# List available datasets
tutorial.available_datasets()  # includes 'fesom_2p6' and 'fesom_dev'

# Open a dataset
ds = tutorial.open_dataset("fesom_2p6")
```

## Datasets

- **fesom_2p6**: FESOM 2.6 on PI mesh configuration
- **fesom_dev**: FESOM development version with UXarray support
