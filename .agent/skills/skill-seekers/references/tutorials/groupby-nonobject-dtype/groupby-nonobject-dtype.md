# How To: Groupby Nonobject Dtype

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test groupby nonobject dtype

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `decimal`
- `decimal`
- `re`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`
- `pandas.core.common`

**Setup Required:**
```python
# Fixtures: multiindex_dataframe_random_data
```

## Step-by-Step Guide

### Step 1: Assign key = value

```python
key = multiindex_dataframe_random_data.index.codes[0]
```

**Verification:**
```python
assert result.index.dtype == np.int8
```

### Step 2: Assign grouped = multiindex_dataframe_random_data.groupby(...)

```python
grouped = multiindex_dataframe_random_data.groupby(key)
```

**Verification:**
```python
assert expected.index.dtype == np.int64
```

### Step 3: Assign result = grouped.sum(...)

```python
result = grouped.sum()
```

### Step 4: Assign expected = multiindex_dataframe_random_data.groupby.sum(...)

```python
expected = multiindex_dataframe_random_data.groupby(key.astype('O')).sum()
```

**Verification:**
```python
assert result.index.dtype == np.int8
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected, check_index_type=False)
```


## Complete Example

```python
# Setup
# Fixtures: multiindex_dataframe_random_data

# Workflow
key = multiindex_dataframe_random_data.index.codes[0]
grouped = multiindex_dataframe_random_data.groupby(key)
result = grouped.sum()
expected = multiindex_dataframe_random_data.groupby(key.astype('O')).sum()
assert result.index.dtype == np.int8
assert expected.index.dtype == np.int64
tm.assert_frame_equal(result, expected, check_index_type=False)
```

## Next Steps


---

*Source: test_groupby.py:137 | Complexity: Intermediate | Last updated: 2026-06-02*