# How To: Loc Getitem With Non String Categories

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test loc getitem with non string categories

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: idx_values, ordered
```

## Step-by-Step Guide

### Step 1: Assign cat_idx = CategoricalIndex(...)

```python
cat_idx = CategoricalIndex(idx_values, ordered=ordered)
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame({'A': ['foo', 'bar', 'baz']}, index=cat_idx)
```

### Step 3: Assign sl = slice(...)

```python
sl = slice(idx_values[0], idx_values[1])
```

### Step 4: Assign result = value

```python
result = df.loc[idx_values[0]]
```

### Step 5: Assign expected = Series(...)

```python
expected = Series(['foo'], index=['A'], name=idx_values[0])
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 7: Assign result = value

```python
result = df.loc[idx_values[:2]]
```

### Step 8: Assign expected = DataFrame(...)

```python
expected = DataFrame(['foo', 'bar'], index=cat_idx[:2], columns=['A'])
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 10: Assign result = value

```python
result = df.loc[sl]
```

### Step 11: Assign expected = DataFrame(...)

```python
expected = DataFrame(['foo', 'bar'], index=cat_idx[:2], columns=['A'])
```

### Step 12: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 13: Assign result = df.copy(...)

```python
result = df.copy()
```

### Step 14: Assign unknown = 'qux'

```python
result.loc[idx_values[0]] = 'qux'
```

### Step 15: Assign expected = DataFrame(...)

```python
expected = DataFrame({'A': ['qux', 'bar', 'baz']}, index=cat_idx)
```

### Step 16: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 17: Assign result = df.copy(...)

```python
result = df.copy()
```

### Step 18: Assign unknown = value

```python
result.loc[idx_values[:2], 'A'] = ['qux', 'qux2']
```

### Step 19: Assign expected = DataFrame(...)

```python
expected = DataFrame({'A': ['qux', 'qux2', 'baz']}, index=cat_idx)
```

### Step 20: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 21: Assign result = df.copy(...)

```python
result = df.copy()
```

### Step 22: Assign unknown = value

```python
result.loc[sl, 'A'] = ['qux', 'qux2']
```

### Step 23: Assign expected = DataFrame(...)

```python
expected = DataFrame({'A': ['qux', 'qux2', 'baz']}, index=cat_idx)
```

### Step 24: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: idx_values, ordered

# Workflow
cat_idx = CategoricalIndex(idx_values, ordered=ordered)
df = DataFrame({'A': ['foo', 'bar', 'baz']}, index=cat_idx)
sl = slice(idx_values[0], idx_values[1])
result = df.loc[idx_values[0]]
expected = Series(['foo'], index=['A'], name=idx_values[0])
tm.assert_series_equal(result, expected)
result = df.loc[idx_values[:2]]
expected = DataFrame(['foo', 'bar'], index=cat_idx[:2], columns=['A'])
tm.assert_frame_equal(result, expected)
result = df.loc[sl]
expected = DataFrame(['foo', 'bar'], index=cat_idx[:2], columns=['A'])
tm.assert_frame_equal(result, expected)
result = df.copy()
result.loc[idx_values[0]] = 'qux'
expected = DataFrame({'A': ['qux', 'bar', 'baz']}, index=cat_idx)
tm.assert_frame_equal(result, expected)
result = df.copy()
result.loc[idx_values[:2], 'A'] = ['qux', 'qux2']
expected = DataFrame({'A': ['qux', 'qux2', 'baz']}, index=cat_idx)
tm.assert_frame_equal(result, expected)
result = df.copy()
result.loc[sl, 'A'] = ['qux', 'qux2']
expected = DataFrame({'A': ['qux', 'qux2', 'baz']}, index=cat_idx)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_categorical.py:523 | Complexity: Advanced | Last updated: 2026-06-02*