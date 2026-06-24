# How To: Getitem Numeric Categorical Listlike Matches Scalar

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test getitem numeric categorical listlike matches scalar

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.indexing`
- `pandas.tseries.offsets`


## Step-by-Step Guide

### Step 1: Assign ser = Series(...)

```python
ser = Series(['a', 'b', 'c'], index=pd.CategoricalIndex([2, 1, 0]))
```

**Verification:**
```python
assert ser[0] == 'c'
```

### Step 2: Assign res = value

```python
res = ser[[0]]
```

### Step 3: Assign expected = value

```python
expected = ser.iloc[-1:]
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(res, expected)
```

### Step 5: Assign res2 = value

```python
res2 = ser[[0, 1, 2]]
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(res2, ser.iloc[::-1])
```


## Complete Example

```python
# Workflow
ser = Series(['a', 'b', 'c'], index=pd.CategoricalIndex([2, 1, 0]))
assert ser[0] == 'c'
res = ser[[0]]
expected = ser.iloc[-1:]
tm.assert_series_equal(res, expected)
res2 = ser[[0, 1, 2]]
tm.assert_series_equal(res2, ser.iloc[::-1])
```

## Next Steps


---

*Source: test_getitem.py:179 | Complexity: Intermediate | Last updated: 2026-06-02*