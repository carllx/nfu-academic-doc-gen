# How To: Max Sas Date

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test max sas date

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `contextlib`
- `datetime`
- `io`
- `os`
- `pathlib`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`
- `pandas.io.sas.sas7bdat`
- `py.path`

**Setup Required:**
```python
# Fixtures: datapath
```

## Step-by-Step Guide

### Step 1: Assign fname = datapath(...)

```python
fname = datapath('io', 'sas', 'data', 'max_sas_date.sas7bdat')
```

### Step 2: Assign df = pd.read_sas(...)

```python
df = pd.read_sas(fname, encoding='iso-8859-1')
```

### Step 3: Assign expected = pd.DataFrame(...)

```python
expected = pd.DataFrame({'text': ['max', 'normal'], 'dt_as_float': [253717747199.999, 1880323199.999], 'dt_as_dt': np.array([datetime(9999, 12, 29, 23, 59, 59, 999000), datetime(2019, 8, 1, 23, 59, 59, 999000)], dtype='M8[ms]'), 'date_as_float': [2936547.0, 21762.0], 'date_as_date': np.array([datetime(9999, 12, 29), datetime(2019, 8, 1)], dtype='M8[s]')}, columns=['text', 'dt_as_float', 'dt_as_dt', 'date_as_float', 'date_as_date'])
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, expected)
```


## Complete Example

```python
# Setup
# Fixtures: datapath

# Workflow
fname = datapath('io', 'sas', 'data', 'max_sas_date.sas7bdat')
df = pd.read_sas(fname, encoding='iso-8859-1')
expected = pd.DataFrame({'text': ['max', 'normal'], 'dt_as_float': [253717747199.999, 1880323199.999], 'dt_as_dt': np.array([datetime(9999, 12, 29, 23, 59, 59, 999000), datetime(2019, 8, 1, 23, 59, 59, 999000)], dtype='M8[ms]'), 'date_as_float': [2936547.0, 21762.0], 'date_as_date': np.array([datetime(9999, 12, 29), datetime(2019, 8, 1)], dtype='M8[s]')}, columns=['text', 'dt_as_float', 'dt_as_dt', 'date_as_float', 'date_as_date'])
if not IS64:
    expected.loc[:, 'dt_as_dt'] -= np.timedelta64(1, 'ms')
tm.assert_frame_equal(df, expected)
```

## Next Steps


---

*Source: test_sas7bdat.py:270 | Complexity: Intermediate | Last updated: 2026-06-02*