# How To: Partial Slicing With Multiindex Series

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test partial slicing with multiindex series

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign ser = Series(...)

```python
ser = Series(range(250), index=MultiIndex.from_product([date_range('2000-1-1', periods=50), range(5)]))
```

### Step 2: Assign s2 = unknown.copy(...)

```python
s2 = ser[:-1].copy()
```

### Step 3: Assign expected = value

```python
expected = s2['2000-1-4']
```

### Step 4: Assign result = value

```python
result = s2[Timestamp('2000-1-4')]
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 6: Assign result = value

```python
result = ser[Timestamp('2000-1-4')]
```

### Step 7: Assign expected = value

```python
expected = ser['2000-1-4']
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 9: Assign df2 = DataFrame(...)

```python
df2 = DataFrame(ser)
```

### Step 10: Assign expected = df2.xs(...)

```python
expected = df2.xs('2000-1-4')
```

### Step 11: Assign result = value

```python
result = df2.loc[Timestamp('2000-1-4')]
```

### Step 12: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
ser = Series(range(250), index=MultiIndex.from_product([date_range('2000-1-1', periods=50), range(5)]))
s2 = ser[:-1].copy()
expected = s2['2000-1-4']
result = s2[Timestamp('2000-1-4')]
tm.assert_series_equal(result, expected)
result = ser[Timestamp('2000-1-4')]
expected = ser['2000-1-4']
tm.assert_series_equal(result, expected)
df2 = DataFrame(ser)
expected = df2.xs('2000-1-4')
result = df2.loc[Timestamp('2000-1-4')]
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_partial_slicing.py:361 | Complexity: Advanced | Last updated: 2026-06-02*