# How To: Concat Datetimeindex Freq

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test concat datetimeindex freq

## Prerequisites

**Required Modules:**
- `datetime`
- `datetime`
- `dateutil`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign dr = date_range(...)

```python
dr = date_range('01-Jan-2013', periods=100, freq='50ms', tz='UTC')
```

### Step 2: Assign data = list(...)

```python
data = list(range(100))
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame(data, index=dr)
```

### Step 4: Assign result = concat(...)

```python
result = concat([expected[:50], expected[50:]])
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 6: Assign result = concat(...)

```python
result = concat([expected[50:], expected[:50]])
```

### Step 7: Assign expected = DataFrame(...)

```python
expected = DataFrame(data[50:] + data[:50], index=dr[50:].append(dr[:50]))
```

### Step 8: Assign expected.index._data.freq = None

```python
expected.index._data.freq = None
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
dr = date_range('01-Jan-2013', periods=100, freq='50ms', tz='UTC')
data = list(range(100))
expected = DataFrame(data, index=dr)
result = concat([expected[:50], expected[50:]])
tm.assert_frame_equal(result, expected)
result = concat([expected[50:], expected[:50]])
expected = DataFrame(data[50:] + data[:50], index=dr[50:].append(dr[:50]))
expected.index._data.freq = None
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_datetimes.py:108 | Complexity: Advanced | Last updated: 2026-06-02*