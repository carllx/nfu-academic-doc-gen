# How To: Describe With Duplicate Output Column Names

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test describe with duplicate output column names

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
df = DataFrame({'a1': [99, 99, 99, 88, 88, 88], 'a2': [99, 99, 99, 88, 88, 88], 'b': [1, 2, 3, 4, 5, 6], 'c': [10, 20, 30, 40, 50, 60]}, columns=['a1', 'a2', 'b', 'b'], copy=False)
```

### Step 2: Assign expected = value

```python
expected = DataFrame.from_records([('b', 'count', 3.0, 3.0), ('b', 'mean', 5.0, 2.0), ('b', 'std', 1.0, 1.0), ('b', 'min', 4.0, 1.0), ('b', '25%', 4.5, 1.5), ('b', '50%', 5.0, 2.0), ('b', '75%', 5.5, 2.5), ('b', 'max', 6.0, 3.0), ('b', 'count', 3.0, 3.0), ('b', 'mean', 5.0, 2.0), ('b', 'std', 1.0, 1.0), ('b', 'min', 4.0, 1.0), ('b', '25%', 4.5, 1.5), ('b', '50%', 5.0, 2.0), ('b', '75%', 5.5, 2.5), ('b', 'max', 6.0, 3.0)]).set_index([0, 1]).T
```

### Step 3: Assign expected.columns.names = value

```python
expected.columns.names = [None, None]
```

### Step 4: Assign result = df.groupby.describe(...)

```python
result = df.groupby(keys, as_index=as_index).describe()
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 6: Assign df = df.drop(...)

```python
df = df.drop(columns='a2')
```

### Step 7: Assign expected.index = MultiIndex(...)

```python
expected.index = MultiIndex(levels=[[88, 99], [88, 99]], codes=[[0, 1], [0, 1]], names=['a1', 'a2'])
```

### Step 8: Assign expected.index = Index(...)

```python
expected.index = Index([88, 99], name='a1')
```

### Step 9: Assign expected = expected.reset_index(...)

```python
expected = expected.reset_index()
```


## Complete Example

```python
# Setup
# Fixtures: as_index, keys

# Workflow
df = DataFrame({'a1': [99, 99, 99, 88, 88, 88], 'a2': [99, 99, 99, 88, 88, 88], 'b': [1, 2, 3, 4, 5, 6], 'c': [10, 20, 30, 40, 50, 60]}, columns=['a1', 'a2', 'b', 'b'], copy=False)
if keys == ['a1']:
    df = df.drop(columns='a2')
expected = DataFrame.from_records([('b', 'count', 3.0, 3.0), ('b', 'mean', 5.0, 2.0), ('b', 'std', 1.0, 1.0), ('b', 'min', 4.0, 1.0), ('b', '25%', 4.5, 1.5), ('b', '50%', 5.0, 2.0), ('b', '75%', 5.5, 2.5), ('b', 'max', 6.0, 3.0), ('b', 'count', 3.0, 3.0), ('b', 'mean', 5.0, 2.0), ('b', 'std', 1.0, 1.0), ('b', 'min', 4.0, 1.0), ('b', '25%', 4.5, 1.5), ('b', '50%', 5.0, 2.0), ('b', '75%', 5.5, 2.5), ('b', 'max', 6.0, 3.0)]).set_index([0, 1]).T
expected.columns.names = [None, None]
if len(keys) == 2:
    expected.index = MultiIndex(levels=[[88, 99], [88, 99]], codes=[[0, 1], [0, 1]], names=['a1', 'a2'])
else:
    expected.index = Index([88, 99], name='a1')
if not as_index:
    expected = expected.reset_index()
result = df.groupby(keys, as_index=as_index).describe()
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_describe.py:158 | Complexity: Advanced | Last updated: 2026-06-02*