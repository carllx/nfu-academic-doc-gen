# How To: Categorical Single Grouper With Only Observed Categories

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test categorical single grouper with only observed categories

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
# Fixtures: education_df, as_index, observed, normalize, name, expected_data, request
```

## Step-by-Step Guide

### Step 1: Assign gp = education_df.astype.groupby(...)

```python
gp = education_df.astype('category').groupby('country', as_index=as_index, observed=observed)
```

### Step 2: Assign result = gp.value_counts(...)

```python
result = gp.value_counts(normalize=normalize)
```

### Step 3: Assign expected_index = MultiIndex.from_tuples(...)

```python
expected_index = MultiIndex.from_tuples([('FR', 'male', 'low'), ('FR', 'female', 'high'), ('FR', 'male', 'medium'), ('FR', 'female', 'low'), ('FR', 'female', 'medium'), ('FR', 'male', 'high'), ('US', 'female', 'high'), ('US', 'male', 'low'), ('US', 'female', 'low'), ('US', 'female', 'medium'), ('US', 'male', 'high'), ('US', 'male', 'medium')], names=['country', 'gender', 'education'])
```

### Step 4: Assign expected_series = Series(...)

```python
expected_series = Series(data=expected_data, index=expected_index, name=name)
```

### Step 5: Call request.applymarker()

```python
request.applymarker(pytest.mark.xfail(reason='pandas default unstable sorting of duplicatesissue with numpy>=1.25 with AVX instructions', strict=False))
```

### Step 6: Assign expected_series.index = expected_series.index.set_levels(...)

```python
expected_series.index = expected_series.index.set_levels(CategoricalIndex(expected_series.index.levels[i]), level=i)
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected_series)
```

### Step 8: Assign expected = expected_series.reset_index(...)

```python
expected = expected_series.reset_index(name='proportion' if normalize else 'count')
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: education_df, as_index, observed, normalize, name, expected_data, request

# Workflow
if Version(np.__version__) >= Version('1.25'):
    request.applymarker(pytest.mark.xfail(reason='pandas default unstable sorting of duplicatesissue with numpy>=1.25 with AVX instructions', strict=False))
gp = education_df.astype('category').groupby('country', as_index=as_index, observed=observed)
result = gp.value_counts(normalize=normalize)
expected_index = MultiIndex.from_tuples([('FR', 'male', 'low'), ('FR', 'female', 'high'), ('FR', 'male', 'medium'), ('FR', 'female', 'low'), ('FR', 'female', 'medium'), ('FR', 'male', 'high'), ('US', 'female', 'high'), ('US', 'male', 'low'), ('US', 'female', 'low'), ('US', 'female', 'medium'), ('US', 'male', 'high'), ('US', 'male', 'medium')], names=['country', 'gender', 'education'])
expected_series = Series(data=expected_data, index=expected_index, name=name)
for i in range(3):
    expected_series.index = expected_series.index.set_levels(CategoricalIndex(expected_series.index.levels[i]), level=i)
if as_index:
    tm.assert_series_equal(result, expected_series)
else:
    expected = expected_series.reset_index(name='proportion' if normalize else 'count')
    tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_value_counts.py:618 | Complexity: Advanced | Last updated: 2026-06-02*