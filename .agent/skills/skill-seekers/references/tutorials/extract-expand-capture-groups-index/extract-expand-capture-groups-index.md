# How To: Extract Expand Capture Groups Index

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test extract expand capture groups index

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `re`
- `numpy`
- `pytest`
- `pandas.core.dtypes.dtypes`
- `pandas`

**Setup Required:**
```python
# Fixtures: index, any_string_dtype
```

## Step-by-Step Guide

### Step 1: Assign data = value

```python
data = ['A1', 'B2', 'C']
```

### Step 2: Assign index = value

```python
index = index[:len(data)]
```

### Step 3: Assign ser = Series(...)

```python
ser = Series(data, index=index, dtype=any_string_dtype)
```

### Step 4: Assign result = ser.str.extract(...)

```python
result = ser.str.extract('(\\d)', expand=False)
```

### Step 5: Assign expected = Series(...)

```python
expected = Series(['1', '2', np.nan], index=index, dtype=any_string_dtype)
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 7: Assign result = ser.str.extract(...)

```python
result = ser.str.extract('(?P<letter>\\D)(?P<number>\\d)?', expand=False)
```

### Step 8: Assign expected = DataFrame(...)

```python
expected = DataFrame([['A', '1'], ['B', '2'], ['C', np.nan]], columns=['letter', 'number'], index=index, dtype=any_string_dtype)
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 10: Call pytest.skip()

```python
pytest.skip('Test requires len(index) > 0')
```

### Step 11: Assign index = index.repeat(...)

```python
index = index.repeat(2)
```


## Complete Example

```python
# Setup
# Fixtures: index, any_string_dtype

# Workflow
data = ['A1', 'B2', 'C']
if len(index) == 0:
    pytest.skip('Test requires len(index) > 0')
while len(index) < len(data):
    index = index.repeat(2)
index = index[:len(data)]
ser = Series(data, index=index, dtype=any_string_dtype)
result = ser.str.extract('(\\d)', expand=False)
expected = Series(['1', '2', np.nan], index=index, dtype=any_string_dtype)
tm.assert_series_equal(result, expected)
result = ser.str.extract('(?P<letter>\\D)(?P<number>\\d)?', expand=False)
expected = DataFrame([['A', '1'], ['B', '2'], ['C', np.nan]], columns=['letter', 'number'], index=index, dtype=any_string_dtype)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_extract.py:182 | Complexity: Advanced | Last updated: 2026-06-02*