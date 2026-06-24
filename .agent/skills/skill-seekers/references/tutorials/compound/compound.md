# How To: Compound

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test compound

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.util.version`

**Setup Required:**
```python
# Fixtures: education_df, normalize, sort, ascending, expected_rows, expected_count, expected_group_size, any_string_dtype, using_infer_string
```

## Step-by-Step Guide

### Step 1: Assign dtype = any_string_dtype

```python
dtype = any_string_dtype
```

### Step 2: Assign education_df = education_df.astype(...)

```python
education_df = education_df.astype(dtype)
```

### Step 3: Assign education_df.columns = education_df.columns.astype(...)

```python
education_df.columns = education_df.columns.astype(dtype)
```

### Step 4: Assign gp = education_df.groupby(...)

```python
gp = education_df.groupby(['country', 'gender'], as_index=False, sort=False)
```

### Step 5: Assign result = unknown.value_counts(...)

```python
result = gp['education'].value_counts(normalize=normalize, sort=sort, ascending=ascending)
```

### Step 6: Assign expected = DataFrame(...)

```python
expected = DataFrame()
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 8: Assign unknown = value

```python
expected[column] = [education_df[column][row] for row in expected_rows]
```

### Step 9: Assign expected = expected.astype(...)

```python
expected = expected.astype(dtype)
```

### Step 10: Assign expected.columns = expected.columns.astype(...)

```python
expected.columns = expected.columns.astype(dtype)
```

### Step 11: Assign unknown = expected_count

```python
expected['proportion'] = expected_count
```

### Step 12: Assign unknown = expected_count

```python
expected['count'] = expected_count
```

### Step 13: Assign expected = expected.astype(...)

```python
expected = expected.astype({'country': 'str', 'gender': 'str', 'education': 'str'})
```

### Step 14: Assign unknown = unknown.convert_dtypes(...)

```python
expected['proportion'] = expected['proportion'].convert_dtypes()
```

### Step 15: Assign unknown = unknown.convert_dtypes(...)

```python
expected['count'] = expected['count'].convert_dtypes()
```


## Complete Example

```python
# Setup
# Fixtures: education_df, normalize, sort, ascending, expected_rows, expected_count, expected_group_size, any_string_dtype, using_infer_string

# Workflow
dtype = any_string_dtype
education_df = education_df.astype(dtype)
education_df.columns = education_df.columns.astype(dtype)
gp = education_df.groupby(['country', 'gender'], as_index=False, sort=False)
result = gp['education'].value_counts(normalize=normalize, sort=sort, ascending=ascending)
expected = DataFrame()
for column in ['country', 'gender', 'education']:
    expected[column] = [education_df[column][row] for row in expected_rows]
    expected = expected.astype(dtype)
    expected.columns = expected.columns.astype(dtype)
if normalize:
    expected['proportion'] = expected_count
    expected['proportion'] /= expected_group_size
    if dtype == 'string[pyarrow]':
        expected['proportion'] = expected['proportion'].convert_dtypes()
else:
    expected['count'] = expected_count
    if dtype == 'string[pyarrow]':
        expected['count'] = expected['count'].convert_dtypes()
if using_infer_string and dtype == object:
    expected = expected.astype({'country': 'str', 'gender': 'str', 'education': 'str'})
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_value_counts.py:399 | Complexity: Advanced | Last updated: 2026-06-02*