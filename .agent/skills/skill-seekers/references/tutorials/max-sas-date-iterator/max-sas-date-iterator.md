# How To: Max Sas Date Iterator

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test max sas date iterator

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

### Step 1: Assign col_order = value

```python
col_order = ['text', 'dt_as_float', 'dt_as_dt', 'date_as_float', 'date_as_date']
```

### Step 2: Assign fname = datapath(...)

```python
fname = datapath('io', 'sas', 'data', 'max_sas_date.sas7bdat')
```

### Step 3: Assign results = value

```python
results = []
```

### Step 4: Assign expected = value

```python
expected = [pd.DataFrame({'text': ['max'], 'dt_as_float': [253717747199.999], 'dt_as_dt': np.array([datetime(9999, 12, 29, 23, 59, 59, 999000)], dtype='M8[ms]'), 'date_as_float': [2936547.0], 'date_as_date': np.array([datetime(9999, 12, 29)], dtype='M8[s]')}, columns=col_order), pd.DataFrame({'text': ['normal'], 'dt_as_float': [1880323199.999], 'dt_as_dt': np.array(['2019-08-01 23:59:59.999'], dtype='M8[ms]'), 'date_as_float': [21762.0], 'date_as_date': np.array(['2019-08-01'], dtype='M8[s]')}, columns=col_order)]
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(results[0], expected[0])
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(results[1], expected[1])
```

### Step 7: Call df.reset_index()

```python
df.reset_index(inplace=True, drop=True)
```

### Step 8: Call results.append()

```python
results.append(df)
```


## Complete Example

```python
# Setup
# Fixtures: datapath

# Workflow
col_order = ['text', 'dt_as_float', 'dt_as_dt', 'date_as_float', 'date_as_date']
fname = datapath('io', 'sas', 'data', 'max_sas_date.sas7bdat')
results = []
for df in pd.read_sas(fname, encoding='iso-8859-1', chunksize=1):
    df.reset_index(inplace=True, drop=True)
    results.append(df)
expected = [pd.DataFrame({'text': ['max'], 'dt_as_float': [253717747199.999], 'dt_as_dt': np.array([datetime(9999, 12, 29, 23, 59, 59, 999000)], dtype='M8[ms]'), 'date_as_float': [2936547.0], 'date_as_date': np.array([datetime(9999, 12, 29)], dtype='M8[s]')}, columns=col_order), pd.DataFrame({'text': ['normal'], 'dt_as_float': [1880323199.999], 'dt_as_dt': np.array(['2019-08-01 23:59:59.999'], dtype='M8[ms]'), 'date_as_float': [21762.0], 'date_as_date': np.array(['2019-08-01'], dtype='M8[s]')}, columns=col_order)]
if not IS64:
    expected[0].loc[0, 'dt_as_dt'] -= np.timedelta64(1, 'ms')
    expected[1].loc[0, 'dt_as_dt'] -= np.timedelta64(1, 'ms')
tm.assert_frame_equal(results[0], expected[0])
tm.assert_frame_equal(results[1], expected[1])
```

## Next Steps


---

*Source: test_sas7bdat.py:309 | Complexity: Advanced | Last updated: 2026-06-02*