# How To: Productsales

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test productsales

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
fname = datapath('io', 'sas', 'data', 'productsales.sas7bdat')
```

### Step 2: Assign df = pd.read_sas(...)

```python
df = pd.read_sas(fname, encoding='utf-8')
```

### Step 3: Assign fname = datapath(...)

```python
fname = datapath('io', 'sas', 'data', 'productsales.csv')
```

### Step 4: Assign df0 = pd.read_csv(...)

```python
df0 = pd.read_csv(fname, parse_dates=['MONTH'])
```

### Step 5: Assign vn = value

```python
vn = ['ACTUAL', 'PREDICT', 'QUARTER', 'YEAR']
```

### Step 6: Assign unknown = unknown.astype(...)

```python
df0[vn] = df0[vn].astype(np.float64)
```

### Step 7: Assign unknown = unknown.astype(...)

```python
df0['MONTH'] = df0['MONTH'].astype('M8[s]')
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, df0)
```


## Complete Example

```python
# Setup
# Fixtures: datapath

# Workflow
fname = datapath('io', 'sas', 'data', 'productsales.sas7bdat')
df = pd.read_sas(fname, encoding='utf-8')
fname = datapath('io', 'sas', 'data', 'productsales.csv')
df0 = pd.read_csv(fname, parse_dates=['MONTH'])
vn = ['ACTUAL', 'PREDICT', 'QUARTER', 'YEAR']
df0[vn] = df0[vn].astype(np.float64)
df0['MONTH'] = df0['MONTH'].astype('M8[s]')
tm.assert_frame_equal(df, df0)
```

## Next Steps


---

*Source: test_sas7bdat.py:153 | Complexity: Advanced | Last updated: 2026-06-02*