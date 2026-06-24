# How To: Rolling Apply Out Of Bounds

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test rolling apply out of bounds

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.tseries`

**Setup Required:**
```python
# Fixtures: engine_and_raw
```

## Step-by-Step Guide

### Step 1: Assign unknown = engine_and_raw

```python
engine, raw = engine_and_raw
```

**Verification:**
```python
assert result.isna().all()
```

### Step 2: Assign vals = Series(...)

```python
vals = Series([1, 2, 3, 4])
```

### Step 3: Assign result = vals.rolling.apply(...)

```python
result = vals.rolling(10).apply(np.sum, engine=engine, raw=raw)
```

**Verification:**
```python
assert result.isna().all()
```

### Step 4: Assign result = vals.rolling.apply(...)

```python
result = vals.rolling(10, min_periods=1).apply(np.sum, engine=engine, raw=raw)
```

### Step 5: Assign expected = Series(...)

```python
expected = Series([1, 3, 6, 10], dtype=float)
```

### Step 6: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: engine_and_raw

# Workflow
engine, raw = engine_and_raw
vals = Series([1, 2, 3, 4])
result = vals.rolling(10).apply(np.sum, engine=engine, raw=raw)
assert result.isna().all()
result = vals.rolling(10, min_periods=1).apply(np.sum, engine=engine, raw=raw)
expected = Series([1, 3, 6, 10], dtype=float)
tm.assert_almost_equal(result, expected)
```

## Next Steps


---

*Source: test_apply.py:36 | Complexity: Intermediate | Last updated: 2026-06-02*