# How To: Transpose Td64 Intervals

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test transpose td64 intervals

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign tdi = timedelta_range(...)

```python
tdi = timedelta_range('0 Days', '3 Days')
```

### Step 2: Assign ii = IntervalIndex.from_breaks(...)

```python
ii = IntervalIndex.from_breaks(tdi)
```

### Step 3: Assign ii = ii.insert(...)

```python
ii = ii.insert(-1, np.nan)
```

### Step 4: Assign df = DataFrame(...)

```python
df = DataFrame(ii)
```

### Step 5: Assign result = value

```python
result = df.T
```

### Step 6: Assign expected = DataFrame(...)

```python
expected = DataFrame({i: ii[i:i + 1] for i in range(len(ii))})
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
tdi = timedelta_range('0 Days', '3 Days')
ii = IntervalIndex.from_breaks(tdi)
ii = ii.insert(-1, np.nan)
df = DataFrame(ii)
result = df.T
expected = DataFrame({i: ii[i:i + 1] for i in range(len(ii))})
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_transpose.py:22 | Complexity: Intermediate | Last updated: 2026-06-02*