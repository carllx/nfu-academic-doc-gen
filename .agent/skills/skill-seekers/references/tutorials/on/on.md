# How To: On

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test on

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`
- `pandas.tseries`

**Setup Required:**
```python
# Fixtures: regular
```

## Step-by-Step Guide

### Step 1: Assign df = regular

```python
df = regular
```

### Step 2: Assign msg = 'invalid on specified as foobar, must be a column \\(of DataFrame\\), an Index or None'

```python
msg = 'invalid on specified as foobar, must be a column \\(of DataFrame\\), an Index or None'
```

### Step 3: Assign df = df.copy(...)

```python
df = df.copy()
```

### Step 4: Assign unknown = date_range(...)

```python
df['C'] = date_range('20130101', periods=len(df))
```

### Step 5: Call df.rolling.sum()

```python
df.rolling(window='2d', on='C').sum()
```

### Step 6: Assign msg = 'window must be an integer'

```python
msg = 'window must be an integer'
```

### Step 7: Call df.rolling.B.sum()

```python
df.rolling(window='2d', on='C').B.sum()
```

### Step 8: Call df.rolling()

```python
df.rolling(window='2s', on='foobar')
```

### Step 9: Call df.rolling()

```python
df.rolling(window='2d', on='B')
```


## Complete Example

```python
# Setup
# Fixtures: regular

# Workflow
df = regular
msg = 'invalid on specified as foobar, must be a column \\(of DataFrame\\), an Index or None'
with pytest.raises(ValueError, match=msg):
    df.rolling(window='2s', on='foobar')
df = df.copy()
df['C'] = date_range('20130101', periods=len(df))
df.rolling(window='2d', on='C').sum()
msg = 'window must be an integer'
with pytest.raises(ValueError, match=msg):
    df.rolling(window='2d', on='B')
df.rolling(window='2d', on='C').B.sum()
```

## Next Steps


---

*Source: test_timeseries_window.py:90 | Complexity: Advanced | Last updated: 2026-06-02*