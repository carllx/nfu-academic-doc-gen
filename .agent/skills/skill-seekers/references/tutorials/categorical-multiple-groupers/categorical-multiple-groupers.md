# How To: Categorical Multiple Groupers

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test categorical multiple groupers

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
# Fixtures: education_df, as_index, observed, expected_index, normalize, name, expected_data
```

## Step-by-Step Guide

### Step 1: Assign education_df = education_df.copy(...)

```python
education_df = education_df.copy()
```

### Step 2: Assign unknown = unknown.astype(...)

```python
education_df['country'] = education_df['country'].astype('category')
```

### Step 3: Assign unknown = unknown.astype(...)

```python
education_df['education'] = education_df['education'].astype('category')
```

### Step 4: Assign gp = education_df.groupby(...)

```python
gp = education_df.groupby(['country', 'education'], as_index=as_index, observed=observed)
```

### Step 5: Assign result = gp.value_counts(...)

```python
result = gp.value_counts(normalize=normalize)
```

### Step 6: Assign expected_series = Series(...)

```python
expected_series = Series(data=expected_data[expected_data > 0.0] if observed else expected_data, index=MultiIndex.from_tuples(expected_index, names=['country', 'education', 'gender']), name=name)
```

### Step 7: Assign expected_series.index = expected_series.index.set_levels(...)

```python
expected_series.index = expected_series.index.set_levels(CategoricalIndex(expected_series.index.levels[i]), level=i)
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected_series)
```

### Step 9: Assign expected = expected_series.reset_index(...)

```python
expected = expected_series.reset_index(name='proportion' if normalize else 'count')
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: education_df, as_index, observed, expected_index, normalize, name, expected_data

# Workflow
education_df = education_df.copy()
education_df['country'] = education_df['country'].astype('category')
education_df['education'] = education_df['education'].astype('category')
gp = education_df.groupby(['country', 'education'], as_index=as_index, observed=observed)
result = gp.value_counts(normalize=normalize)
expected_series = Series(data=expected_data[expected_data > 0.0] if observed else expected_data, index=MultiIndex.from_tuples(expected_index, names=['country', 'education', 'gender']), name=name)
for i in range(2):
    expected_series.index = expected_series.index.set_levels(CategoricalIndex(expected_series.index.levels[i]), level=i)
if as_index:
    tm.assert_series_equal(result, expected_series)
else:
    expected = expected_series.reset_index(name='proportion' if normalize else 'count')
    tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_value_counts.py:905 | Complexity: Advanced | Last updated: 2026-06-02*