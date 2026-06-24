# How To: Sample Aligns Weights With Frame

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test sample aligns weights with frame

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.core.common`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'col1': [5, 6, 7], 'col2': ['a', 'b', 'c']}, index=[9, 5, 3])
```

### Step 2: Assign ser = Series(...)

```python
ser = Series([1, 0, 0], index=[3, 5, 9])
```

### Step 3: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df.loc[[3]], df.sample(1, weights=ser))
```

### Step 4: Assign ser2 = Series(...)

```python
ser2 = Series([0.001, 0, 10000], index=[3, 5, 10])
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df.loc[[3]], df.sample(1, weights=ser2))
```

### Step 6: Assign ser3 = Series(...)

```python
ser3 = Series([0.01, 0], index=[3, 5])
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df.loc[[3]], df.sample(1, weights=ser3))
```

### Step 8: Assign ser4 = Series(...)

```python
ser4 = Series([1, 0], index=[1, 2])
```

### Step 9: Call df.sample()

```python
df.sample(1, weights=ser4)
```


## Complete Example

```python
# Workflow
df = DataFrame({'col1': [5, 6, 7], 'col2': ['a', 'b', 'c']}, index=[9, 5, 3])
ser = Series([1, 0, 0], index=[3, 5, 9])
tm.assert_frame_equal(df.loc[[3]], df.sample(1, weights=ser))
ser2 = Series([0.001, 0, 10000], index=[3, 5, 10])
tm.assert_frame_equal(df.loc[[3]], df.sample(1, weights=ser2))
ser3 = Series([0.01, 0], index=[3, 5])
tm.assert_frame_equal(df.loc[[3]], df.sample(1, weights=ser3))
ser4 = Series([1, 0], index=[1, 2])
with pytest.raises(ValueError, match='Invalid weights: weights sum to zero'):
    df.sample(1, weights=ser4)
```

## Next Steps


---

*Source: test_sample.py:315 | Complexity: Advanced | Last updated: 2026-06-02*