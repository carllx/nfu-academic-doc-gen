# How To: Size On Categorical

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test size on categorical

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: as_index
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame([[1, 1], [2, 2]], columns=['A', 'B'])
```

### Step 2: Assign unknown = unknown.astype(...)

```python
df['A'] = df['A'].astype('category')
```

### Step 3: Assign result = df.groupby.size(...)

```python
result = df.groupby(['A', 'B'], as_index=as_index, observed=False).size()
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame([[1, 1, 1], [1, 2, 0], [2, 1, 0], [2, 2, 1]], columns=['A', 'B', 'size'])
```

### Step 5: Assign unknown = unknown.astype(...)

```python
expected['A'] = expected['A'].astype('category')
```

### Step 6: Call tm.assert_equal()

```python
tm.assert_equal(result, expected)
```

### Step 7: Assign expected = unknown.rename(...)

```python
expected = expected.set_index(['A', 'B'])['size'].rename(None)
```


## Complete Example

```python
# Setup
# Fixtures: as_index

# Workflow
df = DataFrame([[1, 1], [2, 2]], columns=['A', 'B'])
df['A'] = df['A'].astype('category')
result = df.groupby(['A', 'B'], as_index=as_index, observed=False).size()
expected = DataFrame([[1, 1, 1], [1, 2, 0], [2, 1, 0], [2, 2, 1]], columns=['A', 'B', 'size'])
expected['A'] = expected['A'].astype('category')
if as_index:
    expected = expected.set_index(['A', 'B'])['size'].rename(None)
tm.assert_equal(result, expected)
```

## Next Steps


---

*Source: test_size.py:85 | Complexity: Intermediate | Last updated: 2026-06-02*