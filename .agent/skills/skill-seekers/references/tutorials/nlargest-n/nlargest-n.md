# How To: Nlargest N

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test nlargest n

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `itertools`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: n
```

## Step-by-Step Guide

### Step 1: Assign ser = Series(...)

```python
ser = Series([1, 4, 3, 2], index=[0, 0, 1, 1])
```

### Step 2: Assign result = ser.nlargest(...)

```python
result = ser.nlargest(n)
```

### Step 3: Assign expected = ser.sort_values.head(...)

```python
expected = ser.sort_values(ascending=False).head(n)
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign result = ser.nsmallest(...)

```python
result = ser.nsmallest(n)
```

### Step 6: Assign expected = ser.sort_values.head(...)

```python
expected = ser.sort_values().head(n)
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: n

# Workflow
ser = Series([1, 4, 3, 2], index=[0, 0, 1, 1])
result = ser.nlargest(n)
expected = ser.sort_values(ascending=False).head(n)
tm.assert_series_equal(result, expected)
result = ser.nsmallest(n)
expected = ser.sort_values().head(n)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_nlargest.py:160 | Complexity: Intermediate | Last updated: 2026-06-02*