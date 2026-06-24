# How To: Float Freq

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test float freq

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas._testing`
- `pandas.tseries.offsets`


## Step-by-Step Guide

### Step 1: Assign result = interval_range(...)

```python
result = interval_range(0, 1, freq=0.1)
```

### Step 2: Assign expected = IntervalIndex.from_breaks(...)

```python
expected = IntervalIndex.from_breaks([0 + 0.1 * n for n in range(11)])
```

### Step 3: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 4: Assign result = interval_range(...)

```python
result = interval_range(0, 1, freq=0.6)
```

### Step 5: Assign expected = IntervalIndex.from_breaks(...)

```python
expected = IntervalIndex.from_breaks([0, 0.6])
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Workflow
result = interval_range(0, 1, freq=0.1)
expected = IntervalIndex.from_breaks([0 + 0.1 * n for n in range(11)])
tm.assert_index_equal(result, expected)
result = interval_range(0, 1, freq=0.6)
expected = IntervalIndex.from_breaks([0, 0.6])
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_interval_range.py:361 | Complexity: Intermediate | Last updated: 2026-06-02*