# How To: Slice Year

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test slice year

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign dti = date_range(...)

```python
dti = date_range(freq='B', start=datetime(2005, 1, 1), periods=500)
```

### Step 2: Assign s = Series(...)

```python
s = Series(np.arange(len(dti)), index=dti)
```

### Step 3: Assign result = value

```python
result = s['2005']
```

### Step 4: Assign expected = value

```python
expected = s[s.index.year == 2005]
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 6: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).random((len(dti), 5)), index=dti)
```

### Step 7: Assign result = value

```python
result = df.loc['2005']
```

### Step 8: Assign expected = value

```python
expected = df[df.index.year == 2005]
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
dti = date_range(freq='B', start=datetime(2005, 1, 1), periods=500)
s = Series(np.arange(len(dti)), index=dti)
result = s['2005']
expected = s[s.index.year == 2005]
tm.assert_series_equal(result, expected)
df = DataFrame(np.random.default_rng(2).random((len(dti), 5)), index=dti)
result = df.loc['2005']
expected = df[df.index.year == 2005]
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_partial_slicing.py:123 | Complexity: Advanced | Last updated: 2026-06-02*