# How To: Sort Index Ascending List

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test sort index ascending list

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign arrays = value

```python
arrays = [['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'], ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two'], [4, 3, 2, 1, 4, 3, 2, 1]]
```

### Step 2: Assign tuples = zip(...)

```python
tuples = zip(*arrays)
```

### Step 3: Assign mi = MultiIndex.from_tuples(...)

```python
mi = MultiIndex.from_tuples(tuples, names=['first', 'second', 'third'])
```

### Step 4: Assign ser = Series(...)

```python
ser = Series(range(8), index=mi)
```

### Step 5: Assign result = ser.sort_index(...)

```python
result = ser.sort_index(level=['third', 'first'], ascending=False)
```

### Step 6: Assign expected = value

```python
expected = ser.iloc[[4, 0, 5, 1, 6, 2, 7, 3]]
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 8: Assign result = ser.sort_index(...)

```python
result = ser.sort_index(level=['third', 'first'], ascending=[False, True])
```

### Step 9: Assign expected = value

```python
expected = ser.iloc[[0, 4, 1, 5, 2, 6, 3, 7]]
```

### Step 10: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
arrays = [['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'], ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two'], [4, 3, 2, 1, 4, 3, 2, 1]]
tuples = zip(*arrays)
mi = MultiIndex.from_tuples(tuples, names=['first', 'second', 'third'])
ser = Series(range(8), index=mi)
result = ser.sort_index(level=['third', 'first'], ascending=False)
expected = ser.iloc[[4, 0, 5, 1, 6, 2, 7, 3]]
tm.assert_series_equal(result, expected)
result = ser.sort_index(level=['third', 'first'], ascending=[False, True])
expected = ser.iloc[[0, 4, 1, 5, 2, 6, 3, 7]]
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_sort_index.py:180 | Complexity: Advanced | Last updated: 2026-06-02*