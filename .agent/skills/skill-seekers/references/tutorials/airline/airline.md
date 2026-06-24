# How To: Airline

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test airline

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
fname = datapath('io', 'sas', 'data', 'airline.sas7bdat')
```

### Step 2: Assign df = pd.read_sas(...)

```python
df = pd.read_sas(fname)
```

### Step 3: Assign fname = datapath(...)

```python
fname = datapath('io', 'sas', 'data', 'airline.csv')
```

### Step 4: Assign df0 = pd.read_csv(...)

```python
df0 = pd.read_csv(fname)
```

### Step 5: Assign df0 = df0.astype(...)

```python
df0 = df0.astype(np.float64)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, df0)
```


## Complete Example

```python
# Setup
# Fixtures: datapath

# Workflow
fname = datapath('io', 'sas', 'data', 'airline.sas7bdat')
df = pd.read_sas(fname)
fname = datapath('io', 'sas', 'data', 'airline.csv')
df0 = pd.read_csv(fname)
df0 = df0.astype(np.float64)
tm.assert_frame_equal(df, df0)
```

## Next Steps


---

*Source: test_sas7bdat.py:174 | Complexity: Intermediate | Last updated: 2026-06-02*