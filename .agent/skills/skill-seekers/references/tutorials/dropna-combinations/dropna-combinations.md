# How To: Dropna Combinations

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test dropna combinations

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
# Fixtures: nulls_df, group_dropna, count_dropna, expected_rows, expected_values, request
```

## Step-by-Step Guide

### Step 1: Assign gp = nulls_df.groupby(...)

```python
gp = nulls_df.groupby(['A', 'B'], dropna=group_dropna)
```

### Step 2: Assign result = gp.value_counts(...)

```python
result = gp.value_counts(normalize=True, sort=True, dropna=count_dropna)
```

### Step 3: Assign columns = DataFrame(...)

```python
columns = DataFrame()
```

### Step 4: Assign index = MultiIndex.from_frame(...)

```python
index = MultiIndex.from_frame(columns)
```

### Step 5: Assign expected = Series(...)

```python
expected = Series(data=expected_values, index=index, name='proportion')
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 7: Call request.applymarker()

```python
request.applymarker(pytest.mark.xfail(reason='pandas default unstable sorting of duplicatesissue with numpy>=1.25 with AVX instructions', strict=False))
```

### Step 8: Assign unknown = value

```python
columns[column] = [nulls_df[column][row] for row in expected_rows]
```


## Complete Example

```python
# Setup
# Fixtures: nulls_df, group_dropna, count_dropna, expected_rows, expected_values, request

# Workflow
if Version(np.__version__) >= Version('1.25') and (not group_dropna):
    request.applymarker(pytest.mark.xfail(reason='pandas default unstable sorting of duplicatesissue with numpy>=1.25 with AVX instructions', strict=False))
gp = nulls_df.groupby(['A', 'B'], dropna=group_dropna)
result = gp.value_counts(normalize=True, sort=True, dropna=count_dropna)
columns = DataFrame()
for column in nulls_df.columns:
    columns[column] = [nulls_df[column][row] for row in expected_rows]
index = MultiIndex.from_frame(columns)
expected = Series(data=expected_values, index=index, name='proportion')
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_value_counts.py:516 | Complexity: Advanced | Last updated: 2026-06-02*