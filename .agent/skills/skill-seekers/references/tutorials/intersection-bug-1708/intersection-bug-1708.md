# How To: Intersection Bug 1708

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test intersection bug 1708

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tseries.offsets`


## Step-by-Step Guide

### Step 1: Assign index_1 = timedelta_range(...)

```python
index_1 = timedelta_range('1 day', periods=4, freq='h')
```

**Verification:**
```python
assert len(result) == 0
```

### Step 2: Assign index_2 = value

```python
index_2 = index_1 + pd.offsets.Hour(5)
```

**Verification:**
```python
assert result.freq == expected.freq
```

### Step 3: Assign result = index_1.intersection(...)

```python
result = index_1.intersection(index_2)
```

**Verification:**
```python
assert len(result) == 0
```

### Step 4: Assign index_1 = timedelta_range(...)

```python
index_1 = timedelta_range('1 day', periods=4, freq='h')
```

### Step 5: Assign index_2 = value

```python
index_2 = index_1 + pd.offsets.Hour(1)
```

### Step 6: Assign result = index_1.intersection(...)

```python
result = index_1.intersection(index_2)
```

### Step 7: Assign expected = timedelta_range(...)

```python
expected = timedelta_range('1 day 01:00:00', periods=3, freq='h')
```

### Step 8: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

**Verification:**
```python
assert result.freq == expected.freq
```


## Complete Example

```python
# Workflow
index_1 = timedelta_range('1 day', periods=4, freq='h')
index_2 = index_1 + pd.offsets.Hour(5)
result = index_1.intersection(index_2)
assert len(result) == 0
index_1 = timedelta_range('1 day', periods=4, freq='h')
index_2 = index_1 + pd.offsets.Hour(1)
result = index_1.intersection(index_2)
expected = timedelta_range('1 day 01:00:00', periods=3, freq='h')
tm.assert_index_equal(result, expected)
assert result.freq == expected.freq
```

## Next Steps


---

*Source: test_setops.py:95 | Complexity: Advanced | Last updated: 2026-06-02*