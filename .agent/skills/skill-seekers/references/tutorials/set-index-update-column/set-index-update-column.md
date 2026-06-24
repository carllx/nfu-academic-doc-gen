# How To: Set Index Update Column

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test set index update column

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.tests.copy_view.util`

**Setup Required:**
```python
# Fixtures: using_copy_on_write, warn_copy_on_write
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'a': [1, 2], 'b': 1})
```

### Step 2: Assign df = df.set_index(...)

```python
df = df.set_index('a', drop=False)
```

### Step 3: Assign expected = df.index.copy(...)

```python
expected = df.index.copy(deep=True)
```

### Step 4: Assign unknown = 100

```python
df.iloc[0, 0] = 100
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(df.index, expected)
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(df.index, Index([100, 2], name='a'))
```


## Complete Example

```python
# Setup
# Fixtures: using_copy_on_write, warn_copy_on_write

# Workflow
df = DataFrame({'a': [1, 2], 'b': 1})
df = df.set_index('a', drop=False)
expected = df.index.copy(deep=True)
with tm.assert_cow_warning(warn_copy_on_write):
    df.iloc[0, 0] = 100
if using_copy_on_write:
    tm.assert_index_equal(df.index, expected)
else:
    tm.assert_index_equal(df.index, Index([100, 2], name='a'))
```

## Next Steps


---

*Source: test_index.py:22 | Complexity: Intermediate | Last updated: 2026-06-02*