# How To: Valid

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test valid

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: datetime_series
```

## Step-by-Step Guide

### Step 1: Assign ts = datetime_series.copy(...)

```python
ts = datetime_series.copy()
```

**Verification:**
```python
assert len(result) == ts.count()
```

### Step 2: Assign ts.index = ts.index._with_freq(...)

```python
ts.index = ts.index._with_freq(None)
```

### Step 3: Assign unknown = value

```python
ts[::2] = np.nan
```

### Step 4: Assign result = ts.dropna(...)

```python
result = ts.dropna()
```

**Verification:**
```python
assert len(result) == ts.count()
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, ts[1::2])
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, ts[pd.notna(ts)])
```


## Complete Example

```python
# Setup
# Fixtures: datetime_series

# Workflow
ts = datetime_series.copy()
ts.index = ts.index._with_freq(None)
ts[::2] = np.nan
result = ts.dropna()
assert len(result) == ts.count()
tm.assert_series_equal(result, ts[1::2])
tm.assert_series_equal(result, ts[pd.notna(ts)])
```

## Next Steps


---

*Source: test_missing.py:84 | Complexity: Intermediate | Last updated: 2026-06-02*