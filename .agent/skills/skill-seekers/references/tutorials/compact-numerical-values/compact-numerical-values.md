# How To: Compact Numerical Values

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test compact numerical values

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
# Fixtures: datapath, column
```

## Step-by-Step Guide

### Step 1: Assign fname = datapath(...)

```python
fname = datapath('io', 'sas', 'data', 'cars.sas7bdat')
```

### Step 2: Assign df = pd.read_sas(...)

```python
df = pd.read_sas(fname, encoding='latin-1')
```

### Step 3: Assign result = value

```python
result = df[column]
```

### Step 4: Assign expected = unknown.round(...)

```python
expected = df[column].round()
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected, check_exact=True)
```


## Complete Example

```python
# Setup
# Fixtures: datapath, column

# Workflow
fname = datapath('io', 'sas', 'data', 'cars.sas7bdat')
df = pd.read_sas(fname, encoding='latin-1')
result = df[column]
expected = df[column].round()
tm.assert_series_equal(result, expected, check_exact=True)
```

## Next Steps


---

*Source: test_sas7bdat.py:213 | Complexity: Intermediate | Last updated: 2026-06-02*