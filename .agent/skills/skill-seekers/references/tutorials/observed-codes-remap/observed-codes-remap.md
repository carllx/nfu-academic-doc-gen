# How To: Observed Codes Remap

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test observed codes remap

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.api.typing`
- `pandas.tests.groupby`

**Setup Required:**
```python
# Fixtures: observed
```

## Step-by-Step Guide

### Step 1: Assign d = value

```python
d = {'C1': [3, 3, 4, 5], 'C2': [1, 2, 3, 4], 'C3': [10, 100, 200, 34]}
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame(d)
```

### Step 3: Assign values = pd.cut(...)

```python
values = pd.cut(df['C1'], [1, 2, 3, 6])
```

### Step 4: Assign values.name = 'cat'

```python
values.name = 'cat'
```

### Step 5: Assign groups_double_key = df.groupby(...)

```python
groups_double_key = df.groupby([values, 'C2'], observed=observed)
```

### Step 6: Assign idx = MultiIndex.from_arrays(...)

```python
idx = MultiIndex.from_arrays([values, [1, 2, 3, 4]], names=['cat', 'C2'])
```

### Step 7: Assign expected = DataFrame(...)

```python
expected = DataFrame({'C1': [3.0, 3.0, 4.0, 5.0], 'C3': [10.0, 100.0, 200.0, 34.0]}, index=idx)
```

### Step 8: Assign result = groups_double_key.agg(...)

```python
result = groups_double_key.agg('mean')
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 10: Assign expected = cartesian_product_for_groupers(...)

```python
expected = cartesian_product_for_groupers(expected, [values.values, [1, 2, 3, 4]], ['cat', 'C2'])
```


## Complete Example

```python
# Setup
# Fixtures: observed

# Workflow
d = {'C1': [3, 3, 4, 5], 'C2': [1, 2, 3, 4], 'C3': [10, 100, 200, 34]}
df = DataFrame(d)
values = pd.cut(df['C1'], [1, 2, 3, 6])
values.name = 'cat'
groups_double_key = df.groupby([values, 'C2'], observed=observed)
idx = MultiIndex.from_arrays([values, [1, 2, 3, 4]], names=['cat', 'C2'])
expected = DataFrame({'C1': [3.0, 3.0, 4.0, 5.0], 'C3': [10.0, 100.0, 200.0, 34.0]}, index=idx)
if not observed:
    expected = cartesian_product_for_groupers(expected, [values.values, [1, 2, 3, 4]], ['cat', 'C2'])
result = groups_double_key.agg('mean')
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_categorical.py:468 | Complexity: Advanced | Last updated: 2026-06-02*