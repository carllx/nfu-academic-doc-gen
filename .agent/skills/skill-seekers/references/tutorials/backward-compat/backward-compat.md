# How To: Backward Compat

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test backward compat

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `bz2`
- `datetime`
- `datetime`
- `gzip`
- `io`
- `os`
- `struct`
- `tarfile`
- `zipfile`
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.frame`
- `pandas.io.parsers`
- `pandas.io.stata`

**Setup Required:**
```python
# Fixtures: version, datapath
```

## Step-by-Step Guide

### Step 1: Assign data_base = datapath(...)

```python
data_base = datapath('io', 'data', 'stata')
```

### Step 2: Assign ref = os.path.join(...)

```python
ref = os.path.join(data_base, 'stata-compat-118.dta')
```

### Step 3: Assign old = os.path.join(...)

```python
old = os.path.join(data_base, f'stata-compat-{version}.dta')
```

### Step 4: Assign expected = read_stata(...)

```python
expected = read_stata(ref)
```

### Step 5: Assign old_dta = read_stata(...)

```python
old_dta = read_stata(old)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(old_dta, expected, check_dtype=False)
```


## Complete Example

```python
# Setup
# Fixtures: version, datapath

# Workflow
data_base = datapath('io', 'data', 'stata')
ref = os.path.join(data_base, 'stata-compat-118.dta')
old = os.path.join(data_base, f'stata-compat-{version}.dta')
expected = read_stata(ref)
old_dta = read_stata(old)
tm.assert_frame_equal(old_dta, expected, check_dtype=False)
```

## Next Steps


---

*Source: test_stata.py:1980 | Complexity: Intermediate | Last updated: 2026-06-02*