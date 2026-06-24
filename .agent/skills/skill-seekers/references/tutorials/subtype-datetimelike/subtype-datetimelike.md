# How To: Subtype Datetimelike

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test subtype datetimelike

## Prerequisites

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign dtype = IntervalDtype(...)

```python
dtype = IntervalDtype('timedelta64[ns]', 'right')
```

### Step 2: Assign msg = 'Cannot convert .* to .*; subtypes are incompatible'

```python
msg = 'Cannot convert .* to .*; subtypes are incompatible'
```

### Step 3: Assign index = interval_range(...)

```python
index = interval_range(Timestamp('2018-01-01'), periods=10)
```

### Step 4: Assign index = interval_range(...)

```python
index = interval_range(Timestamp('2018-01-01', tz='CET'), periods=10)
```

### Step 5: Assign dtype = IntervalDtype(...)

```python
dtype = IntervalDtype('datetime64[ns]', 'right')
```

### Step 6: Assign index = interval_range(...)

```python
index = interval_range(Timedelta('0 days'), periods=10)
```

### Step 7: Call index.astype()

```python
index.astype(dtype)
```

### Step 8: Call index.astype()

```python
index.astype(dtype)
```

### Step 9: Call index.astype()

```python
index.astype(dtype)
```


## Complete Example

```python
# Workflow
dtype = IntervalDtype('timedelta64[ns]', 'right')
msg = 'Cannot convert .* to .*; subtypes are incompatible'
index = interval_range(Timestamp('2018-01-01'), periods=10)
with pytest.raises(TypeError, match=msg):
    index.astype(dtype)
index = interval_range(Timestamp('2018-01-01', tz='CET'), periods=10)
with pytest.raises(TypeError, match=msg):
    index.astype(dtype)
dtype = IntervalDtype('datetime64[ns]', 'right')
index = interval_range(Timedelta('0 days'), periods=10)
with pytest.raises(TypeError, match=msg):
    index.astype(dtype)
```

## Next Steps


---

*Source: test_astype.py:237 | Complexity: Advanced | Last updated: 2026-06-02*