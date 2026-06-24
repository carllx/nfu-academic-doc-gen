# How To: Cummin Cummax Period

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test cummin cummax period

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: func, exp
```

## Step-by-Step Guide

### Step 1: Assign ser = pd.Series(...)

```python
ser = pd.Series([pd.Period('2012-1-1', freq='D'), pd.NaT, pd.Period('2012-1-2', freq='D')])
```

### Step 2: Assign result = getattr(...)

```python
result = getattr(ser, func)(skipna=False)
```

### Step 3: Assign expected = pd.Series(...)

```python
expected = pd.Series([pd.Period('2012-1-1', freq='D'), pd.NaT, pd.NaT])
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign result = getattr(...)

```python
result = getattr(ser, func)(skipna=True)
```

### Step 6: Assign expected = pd.Series(...)

```python
expected = pd.Series([pd.Period('2012-1-1', freq='D'), pd.NaT, exp])
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: func, exp

# Workflow
ser = pd.Series([pd.Period('2012-1-1', freq='D'), pd.NaT, pd.Period('2012-1-2', freq='D')])
result = getattr(ser, func)(skipna=False)
expected = pd.Series([pd.Period('2012-1-1', freq='D'), pd.NaT, pd.NaT])
tm.assert_series_equal(result, expected)
result = getattr(ser, func)(skipna=True)
expected = pd.Series([pd.Period('2012-1-1', freq='D'), pd.NaT, exp])
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_cumulative.py:103 | Complexity: Intermediate | Last updated: 2026-06-02*