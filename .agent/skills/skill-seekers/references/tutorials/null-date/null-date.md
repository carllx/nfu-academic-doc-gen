# How To: Null Date

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test null date

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
fname = datapath('io', 'sas', 'data', 'dates_null.sas7bdat')
```

### Step 2: Assign df = pd.read_sas(...)

```python
df = pd.read_sas(fname, encoding='utf-8')
```

### Step 3: Assign expected = pd.DataFrame(...)

```python
expected = pd.DataFrame({'datecol': np.array([datetime(9999, 12, 29), np.datetime64('NaT')], dtype='M8[s]'), 'datetimecol': np.array([datetime(9999, 12, 29, 23, 59, 59, 999000), np.datetime64('NaT')], dtype='M8[ms]')})
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
fname = datapath('io', 'sas', 'data', 'dates_null.sas7bdat')
df = pd.read_sas(fname, encoding='utf-8')
expected = pd.DataFrame({'datecol': np.array([datetime(9999, 12, 29), np.datetime64('NaT')], dtype='M8[s]'), 'datetimecol': np.array([datetime(9999, 12, 29, 23, 59, 59, 999000), np.datetime64('NaT')], dtype='M8[ms]')})
if not IS64:
    expected.loc[0, 'datetimecol'] -= np.timedelta64(1, 'ms')
tm.assert_frame_equal(df, expected)
```

## Next Steps


---

*Source: test_sas7bdat.py:354 | Complexity: Intermediate | Last updated: 2026-06-02*