# How To: Linspace Dst Transition

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test linspace dst transition

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas._testing`
- `pandas.tseries.offsets`

**Setup Required:**
```python
# Fixtures: start, mid, end
```

## Step-by-Step Guide

### Step 1: Assign start = start.as_unit(...)

```python
start = start.as_unit('ns')
```

### Step 2: Assign mid = mid.as_unit(...)

```python
mid = mid.as_unit('ns')
```

### Step 3: Assign end = end.as_unit(...)

```python
end = end.as_unit('ns')
```

### Step 4: Assign result = interval_range(...)

```python
result = interval_range(start=start, end=end, periods=2)
```

### Step 5: Assign expected = IntervalIndex.from_breaks(...)

```python
expected = IntervalIndex.from_breaks([start, mid, end])
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: start, mid, end

# Workflow
start = start.as_unit('ns')
mid = mid.as_unit('ns')
end = end.as_unit('ns')
result = interval_range(start=start, end=end, periods=2)
expected = IntervalIndex.from_breaks([start, mid, end])
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_interval_range.py:182 | Complexity: Intermediate | Last updated: 2026-06-02*