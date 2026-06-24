# How To: Droplevel

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test droplevel

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: frame_or_series
```

## Step-by-Step Guide

### Step 1: Assign cols = MultiIndex.from_tuples(...)

```python
cols = MultiIndex.from_tuples([('c', 'e'), ('d', 'f')], names=['level_1', 'level_2'])
```

### Step 2: Assign mi = MultiIndex.from_tuples(...)

```python
mi = MultiIndex.from_tuples([(1, 2), (5, 6), (9, 10)], names=['a', 'b'])
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame([[3, 4], [7, 8], [11, 12]], index=mi, columns=cols)
```

### Step 4: Assign expected = df.reset_index(...)

```python
expected = df.reset_index('a', drop=True)
```

### Step 5: Assign result = df.droplevel(...)

```python
result = df.droplevel('a', axis='index')
```

### Step 6: Call tm.assert_equal()

```python
tm.assert_equal(result, expected)
```

### Step 7: Assign df = value

```python
df = df.iloc[:, 0]
```

### Step 8: Assign expected = df.copy(...)

```python
expected = df.copy()
```

### Step 9: Assign expected.columns = Index(...)

```python
expected.columns = Index(['c', 'd'], name='level_1')
```

### Step 10: Assign result = df.droplevel(...)

```python
result = df.droplevel('level_2', axis='columns')
```

### Step 11: Call tm.assert_equal()

```python
tm.assert_equal(result, expected)
```

### Step 12: Call df.droplevel()

```python
df.droplevel(1, axis='columns')
```


## Complete Example

```python
# Setup
# Fixtures: frame_or_series

# Workflow
cols = MultiIndex.from_tuples([('c', 'e'), ('d', 'f')], names=['level_1', 'level_2'])
mi = MultiIndex.from_tuples([(1, 2), (5, 6), (9, 10)], names=['a', 'b'])
df = DataFrame([[3, 4], [7, 8], [11, 12]], index=mi, columns=cols)
if frame_or_series is not DataFrame:
    df = df.iloc[:, 0]
expected = df.reset_index('a', drop=True)
result = df.droplevel('a', axis='index')
tm.assert_equal(result, expected)
if frame_or_series is DataFrame:
    expected = df.copy()
    expected.columns = Index(['c', 'd'], name='level_1')
    result = df.droplevel('level_2', axis='columns')
    tm.assert_equal(result, expected)
else:
    with pytest.raises(ValueError, match='No axis named columns'):
        df.droplevel(1, axis='columns')
```

## Next Steps


---

*Source: test_droplevel.py:12 | Complexity: Advanced | Last updated: 2026-06-02*