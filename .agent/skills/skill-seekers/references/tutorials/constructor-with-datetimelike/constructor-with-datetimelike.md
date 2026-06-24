# How To: Constructor With Datetimelike

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test constructor with datetimelike

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas.compat`
- `pandas.core.dtypes.common`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: dtl
```

## Step-by-Step Guide

### Step 1: Assign s = Series(...)

```python
s = Series(dtl)
```

**Verification:**
```python
assert 'NaT' in result
```

### Step 2: Assign c = Categorical(...)

```python
c = Categorical(s)
```

### Step 3: Assign expected = type(...)

```python
expected = type(dtl)(s)
```

### Step 4: Assign expected._data.freq = None

```python
expected._data.freq = None
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(c.categories, expected)
```

### Step 6: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(c.codes, np.arange(5, dtype='int8'))
```

### Step 7: Assign s2 = s.copy(...)

```python
s2 = s.copy()
```

### Step 8: Assign unknown = NaT

```python
s2.iloc[-1] = NaT
```

### Step 9: Assign c = Categorical(...)

```python
c = Categorical(s2)
```

### Step 10: Assign expected = type(...)

```python
expected = type(dtl)(s2.dropna())
```

### Step 11: Assign expected._data.freq = None

```python
expected._data.freq = None
```

### Step 12: Call tm.assert_index_equal()

```python
tm.assert_index_equal(c.categories, expected)
```

### Step 13: Assign exp = np.array(...)

```python
exp = np.array([0, 1, 2, 3, -1], dtype=np.int8)
```

### Step 14: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(c.codes, exp)
```

### Step 15: Assign result = repr(...)

```python
result = repr(c)
```

**Verification:**
```python
assert 'NaT' in result
```


## Complete Example

```python
# Setup
# Fixtures: dtl

# Workflow
s = Series(dtl)
c = Categorical(s)
expected = type(dtl)(s)
expected._data.freq = None
tm.assert_index_equal(c.categories, expected)
tm.assert_numpy_array_equal(c.codes, np.arange(5, dtype='int8'))
s2 = s.copy()
s2.iloc[-1] = NaT
c = Categorical(s2)
expected = type(dtl)(s2.dropna())
expected._data.freq = None
tm.assert_index_equal(c.categories, expected)
exp = np.array([0, 1, 2, 3, -1], dtype=np.int8)
tm.assert_numpy_array_equal(c.codes, exp)
result = repr(c)
assert 'NaT' in result
```

## Next Steps


---

*Source: test_constructors.py:334 | Complexity: Advanced | Last updated: 2026-06-02*