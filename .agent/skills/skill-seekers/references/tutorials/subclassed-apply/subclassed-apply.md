# How To: Subclassed Apply

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test subclassed apply

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = tm.SubclassedDataFrame(...)

```python
df = tm.SubclassedDataFrame([['John', 'Doe', 'height', 5.5], ['Mary', 'Bo', 'height', 6.0], ['John', 'Doe', 'weight', 130], ['Mary', 'Bo', 'weight', 150]], columns=['first', 'last', 'variable', 'value'])
```

**Verification:**
```python
assert isinstance(row, tm.SubclassedSeries)
```

### Step 2: Call df.apply()

```python
df.apply(lambda x: check_row_subclass(x))
```

**Verification:**
```python
assert isinstance(result, tm.SubclassedDataFrame)
```

### Step 3: Call df.apply()

```python
df.apply(lambda x: check_row_subclass(x), axis=1)
```

**Verification:**
```python
assert isinstance(result, tm.SubclassedDataFrame)
```

### Step 4: Assign expected = tm.SubclassedDataFrame(...)

```python
expected = tm.SubclassedDataFrame([['John', 'Doe', 'height', 6.0], ['Mary', 'Bo', 'height', 6.5], ['John', 'Doe', 'weight', 130], ['Mary', 'Bo', 'weight', 150]], columns=['first', 'last', 'variable', 'value'])
```

**Verification:**
```python
assert isinstance(result, tm.SubclassedDataFrame)
```

### Step 5: Assign result = df.apply(...)

```python
result = df.apply(lambda x: stretch(x), axis=1)
```

**Verification:**
```python
assert not isinstance(result, tm.SubclassedDataFrame)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 7: Assign expected = tm.SubclassedDataFrame(...)

```python
expected = tm.SubclassedDataFrame([[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]])
```

### Step 8: Assign result = df.apply(...)

```python
result = df.apply(lambda x: tm.SubclassedSeries([1, 2, 3]), axis=1)
```

**Verification:**
```python
assert isinstance(result, tm.SubclassedDataFrame)
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 10: Assign result = df.apply(...)

```python
result = df.apply(lambda x: [1, 2, 3], axis=1, result_type='expand')
```

**Verification:**
```python
assert isinstance(result, tm.SubclassedDataFrame)
```

### Step 11: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 12: Assign expected = tm.SubclassedSeries(...)

```python
expected = tm.SubclassedSeries([[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]])
```

### Step 13: Assign result = df.apply(...)

```python
result = df.apply(lambda x: [1, 2, 3], axis=1)
```

**Verification:**
```python
assert not isinstance(result, tm.SubclassedDataFrame)
```

### Step 14: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

**Verification:**
```python
assert isinstance(row, tm.SubclassedSeries)
```


## Complete Example

```python
# Workflow
def check_row_subclass(row):
    assert isinstance(row, tm.SubclassedSeries)

def stretch(row):
    if row['variable'] == 'height':
        row['value'] += 0.5
    return row
df = tm.SubclassedDataFrame([['John', 'Doe', 'height', 5.5], ['Mary', 'Bo', 'height', 6.0], ['John', 'Doe', 'weight', 130], ['Mary', 'Bo', 'weight', 150]], columns=['first', 'last', 'variable', 'value'])
df.apply(lambda x: check_row_subclass(x))
df.apply(lambda x: check_row_subclass(x), axis=1)
expected = tm.SubclassedDataFrame([['John', 'Doe', 'height', 6.0], ['Mary', 'Bo', 'height', 6.5], ['John', 'Doe', 'weight', 130], ['Mary', 'Bo', 'weight', 150]], columns=['first', 'last', 'variable', 'value'])
result = df.apply(lambda x: stretch(x), axis=1)
assert isinstance(result, tm.SubclassedDataFrame)
tm.assert_frame_equal(result, expected)
expected = tm.SubclassedDataFrame([[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]])
result = df.apply(lambda x: tm.SubclassedSeries([1, 2, 3]), axis=1)
assert isinstance(result, tm.SubclassedDataFrame)
tm.assert_frame_equal(result, expected)
result = df.apply(lambda x: [1, 2, 3], axis=1, result_type='expand')
assert isinstance(result, tm.SubclassedDataFrame)
tm.assert_frame_equal(result, expected)
expected = tm.SubclassedSeries([[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]])
result = df.apply(lambda x: [1, 2, 3], axis=1)
assert not isinstance(result, tm.SubclassedDataFrame)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_subclass.py:538 | Complexity: Advanced | Last updated: 2026-06-02*