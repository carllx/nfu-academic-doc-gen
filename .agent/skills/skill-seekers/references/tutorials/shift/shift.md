# How To: Shift

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test shift

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`


## Step-by-Step Guide

### Step 1: Assign a = IntervalArray.from_breaks(...)

```python
a = IntervalArray.from_breaks([1, 2, 3])
```

### Step 2: Assign result = a.shift(...)

```python
result = a.shift()
```

### Step 3: Assign expected = IntervalArray.from_tuples(...)

```python
expected = IntervalArray.from_tuples([(np.nan, np.nan), (1.0, 2.0)])
```

### Step 4: Call tm.assert_interval_array_equal()

```python
tm.assert_interval_array_equal(result, expected)
```

### Step 5: Assign msg = 'can only insert Interval objects and NA into an IntervalArray'

```python
msg = 'can only insert Interval objects and NA into an IntervalArray'
```

### Step 6: Call a.shift()

```python
a.shift(1, fill_value=pd.NaT)
```


## Complete Example

```python
# Workflow
a = IntervalArray.from_breaks([1, 2, 3])
result = a.shift()
expected = IntervalArray.from_tuples([(np.nan, np.nan), (1.0, 2.0)])
tm.assert_interval_array_equal(result, expected)
msg = 'can only insert Interval objects and NA into an IntervalArray'
with pytest.raises(TypeError, match=msg):
    a.shift(1, fill_value=pd.NaT)
```

## Next Steps


---

*Source: test_interval.py:88 | Complexity: Intermediate | Last updated: 2026-06-02*