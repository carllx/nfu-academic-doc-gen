# How To: Groupby Dropna With Multiindex Input

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test groupby dropna with multiindex input

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.compat.pyarrow`
- `pandas.core.dtypes.missing`
- `pandas`
- `pandas._testing`
- `pandas.tests.groupby`

**Setup Required:**
```python
# Fixtures: input_index, keys, series
```

## Step-by-Step Guide

### Step 1: Assign obj = pd.DataFrame(...)

```python
obj = pd.DataFrame({'a': [1, np.nan], 'b': [1, 1], 'c': [2, 3]})
```

### Step 2: Assign expected = obj.set_index(...)

```python
expected = obj.set_index(keys)
```

### Step 3: Assign gb = obj.groupby(...)

```python
gb = obj.groupby(keys, dropna=False)
```

### Step 4: Assign result = gb.sum(...)

```python
result = gb.sum()
```

### Step 5: Call tm.assert_equal()

```python
tm.assert_equal(result, expected)
```

### Step 6: Assign expected = value

```python
expected = expected['c']
```

### Step 7: Assign obj = obj.set_index(...)

```python
obj = obj.set_index(input_index)
```

### Step 8: Assign gb = value

```python
gb = gb['c']
```

### Step 9: Assign expected = value

```python
expected = expected[['c']]
```


## Complete Example

```python
# Setup
# Fixtures: input_index, keys, series

# Workflow
obj = pd.DataFrame({'a': [1, np.nan], 'b': [1, 1], 'c': [2, 3]})
expected = obj.set_index(keys)
if series:
    expected = expected['c']
elif input_index == ['a', 'b'] and keys == ['a']:
    expected = expected[['c']]
if input_index is not None:
    obj = obj.set_index(input_index)
gb = obj.groupby(keys, dropna=False)
if series:
    gb = gb['c']
result = gb.sum()
tm.assert_equal(result, expected)
```

## Next Steps


---

*Source: test_groupby_dropna.py:345 | Complexity: Advanced | Last updated: 2026-06-02*