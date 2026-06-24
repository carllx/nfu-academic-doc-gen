# How To: Set Index Drop Update Column

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test set index drop update column

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
# Fixtures: using_copy_on_write
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'a': [1, 2], 'b': 1.5})
```

### Step 2: Assign view = value

```python
view = df[:]
```

### Step 3: Assign df = df.set_index(...)

```python
df = df.set_index('a', drop=True)
```

### Step 4: Assign expected = df.index.copy(...)

```python
expected = df.index.copy(deep=True)
```

### Step 5: Assign unknown = 100

```python
view.iloc[0, 0] = 100
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(df.index, expected)
```


## Complete Example

```python
# Setup
# Fixtures: using_copy_on_write

# Workflow
df = DataFrame({'a': [1, 2], 'b': 1.5})
view = df[:]
df = df.set_index('a', drop=True)
expected = df.index.copy(deep=True)
view.iloc[0, 0] = 100
tm.assert_index_equal(df.index, expected)
```

## Next Steps


---

*Source: test_index.py:34 | Complexity: Intermediate | Last updated: 2026-06-02*