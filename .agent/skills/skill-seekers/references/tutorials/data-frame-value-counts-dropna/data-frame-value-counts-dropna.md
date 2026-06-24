# How To: Data Frame Value Counts Dropna

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test data frame value counts dropna

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
# Fixtures: names_with_nulls_df, dropna, normalize, name, expected_data, expected_index
```

## Step-by-Step Guide

### Step 1: Assign result_frame = names_with_nulls_df.value_counts(...)

```python
result_frame = names_with_nulls_df.value_counts(dropna=dropna, normalize=normalize)
```

### Step 2: Assign expected = Series(...)

```python
expected = Series(data=expected_data, index=expected_index, name=name)
```

### Step 3: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result_frame, expected)
```

### Step 4: Assign result_frame_groupby = names_with_nulls_df.groupby.value_counts(...)

```python
result_frame_groupby = names_with_nulls_df.groupby('key').value_counts(dropna=dropna, normalize=normalize)
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result_frame_groupby, expected)
```


## Complete Example

```python
# Setup
# Fixtures: names_with_nulls_df, dropna, normalize, name, expected_data, expected_index

# Workflow
result_frame = names_with_nulls_df.value_counts(dropna=dropna, normalize=normalize)
expected = Series(data=expected_data, index=expected_index, name=name)
if normalize:
    expected /= float(len(expected_data))
tm.assert_series_equal(result_frame, expected)
result_frame_groupby = names_with_nulls_df.groupby('key').value_counts(dropna=dropna, normalize=normalize)
tm.assert_series_equal(result_frame_groupby, expected)
```

## Next Steps


---

*Source: test_value_counts.py:577 | Complexity: Intermediate | Last updated: 2026-06-02*