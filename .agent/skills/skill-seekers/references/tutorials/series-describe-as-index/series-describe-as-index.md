# How To: Series Describe As Index

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test series describe as index

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: as_index, keys
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'key1': ['one', 'two', 'two', 'three', 'two'], 'key2': ['one', 'two', 'two', 'three', 'two'], 'foo2': [1, 2, 4, 4, 6]})
```

### Step 2: Assign gb = value

```python
gb = df.groupby(keys, as_index=as_index)['foo2']
```

### Step 3: Assign result = gb.describe(...)

```python
result = gb.describe()
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame({'key1': ['one', 'three', 'two'], 'count': [1.0, 1.0, 3.0], 'mean': [1.0, 4.0, 4.0], 'std': [np.nan, np.nan, 2.0], 'min': [1.0, 4.0, 2.0], '25%': [1.0, 4.0, 3.0], '50%': [1.0, 4.0, 4.0], '75%': [1.0, 4.0, 5.0], 'max': [1.0, 4.0, 6.0]})
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 6: Call expected.insert()

```python
expected.insert(1, 'key2', expected['key1'])
```

### Step 7: Assign expected = expected.set_index(...)

```python
expected = expected.set_index(keys)
```


## Complete Example

```python
# Setup
# Fixtures: as_index, keys

# Workflow
df = DataFrame({'key1': ['one', 'two', 'two', 'three', 'two'], 'key2': ['one', 'two', 'two', 'three', 'two'], 'foo2': [1, 2, 4, 4, 6]})
gb = df.groupby(keys, as_index=as_index)['foo2']
result = gb.describe()
expected = DataFrame({'key1': ['one', 'three', 'two'], 'count': [1.0, 1.0, 3.0], 'mean': [1.0, 4.0, 4.0], 'std': [np.nan, np.nan, 2.0], 'min': [1.0, 4.0, 2.0], '25%': [1.0, 4.0, 3.0], '50%': [1.0, 4.0, 4.0], '75%': [1.0, 4.0, 5.0], 'max': [1.0, 4.0, 6.0]})
if len(keys) == 2:
    expected.insert(1, 'key2', expected['key1'])
if as_index:
    expected = expected.set_index(keys)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_describe.py:43 | Complexity: Intermediate | Last updated: 2026-06-02*