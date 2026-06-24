# How To: Extract Dataframe Capture Groups Index

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test extract dataframe capture groups index

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

### Step 3: Assign s = Series(...)

```python
s = Series(data, index=index, dtype=any_string_dtype)
```

### Step 4: Assign result = s.str.extract(...)

```python
result = s.str.extract('(\\d)', expand=True)
```

### Step 5: Assign expected = DataFrame(...)

```python
expected = DataFrame(['1', '2', np.nan], index=index, dtype=any_string_dtype)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 7: Assign result = s.str.extract(...)

```python
result = s.str.extract('(?P<letter>\\D)(?P<number>\\d)?', expand=True)
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
pytest.skip(f'Index needs more than {len(data)} values')
```


## Complete Example

```python
# Setup
# Fixtures: index, any_string_dtype

# Workflow
data = ['A1', 'B2', 'C']
if len(index) < len(data):
    pytest.skip(f'Index needs more than {len(data)} values')
index = index[:len(data)]
s = Series(data, index=index, dtype=any_string_dtype)
result = s.str.extract('(\\d)', expand=True)
expected = DataFrame(['1', '2', np.nan], index=index, dtype=any_string_dtype)
tm.assert_frame_equal(result, expected)
result = s.str.extract('(?P<letter>\\D)(?P<number>\\d)?', expand=True)
expected = DataFrame([['A', '1'], ['B', '2'], ['C', np.nan]], columns=['letter', 'number'], index=index, dtype=any_string_dtype)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_extract.py:361 | Complexity: Advanced | Last updated: 2026-06-02*