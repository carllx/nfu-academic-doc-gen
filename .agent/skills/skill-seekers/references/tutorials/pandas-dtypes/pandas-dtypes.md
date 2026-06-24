# How To: Pandas Dtypes

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test pandas dtypes

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: col
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'klass': range(5), 'col': col, 'attr1': [1, 0, 0, 0, 0], 'attr2': col})
```

### Step 2: Assign expected_value = pd.concat(...)

```python
expected_value = pd.concat([pd.Series([1, 0, 0, 0, 0]), col], ignore_index=True)
```

### Step 3: Assign result = melt(...)

```python
result = melt(df, id_vars=['klass', 'col'], var_name='attribute', value_name='value')
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame({0: list(range(5)) * 2, 1: pd.concat([col] * 2, ignore_index=True), 2: ['attr1'] * 5 + ['attr2'] * 5, 3: expected_value})
```

### Step 5: Assign expected.columns = value

```python
expected.columns = ['klass', 'col', 'attribute', 'value']
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: col

# Workflow
df = DataFrame({'klass': range(5), 'col': col, 'attr1': [1, 0, 0, 0, 0], 'attr2': col})
expected_value = pd.concat([pd.Series([1, 0, 0, 0, 0]), col], ignore_index=True)
result = melt(df, id_vars=['klass', 'col'], var_name='attribute', value_name='value')
expected = DataFrame({0: list(range(5)) * 2, 1: pd.concat([col] * 2, ignore_index=True), 2: ['attr1'] * 5 + ['attr2'] * 5, 3: expected_value})
expected.columns = ['klass', 'col', 'attribute', 'value']
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_melt.py:295 | Complexity: Intermediate | Last updated: 2026-06-02*