# How To: Basic Indexing

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test basic indexing

## Prerequisites

**Required Modules:**
- `datetime`
- `re`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.errors`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign s = Series(...)

```python
s = Series(np.random.default_rng(2).standard_normal(5), index=['a', 'b', 'a', 'a', 'b'])
```

### Step 2: Assign warn_msg = 'Series.__[sg]etitem__ treating keys as positions is deprecated'

```python
warn_msg = 'Series.__[sg]etitem__ treating keys as positions is deprecated'
```

### Step 3: Assign msg = 'index 5 is out of bounds for axis 0 with size 5'

```python
msg = 'index 5 is out of bounds for axis 0 with size 5'
```

### Step 4: Assign s = s.sort_index(...)

```python
s = s.sort_index()
```

### Step 5: Assign msg = 'index 5 is out of bounds for axis (0|1) with size 5|^5$'

```python
msg = 'index 5 is out of bounds for axis (0|1) with size 5|^5$'
```

### Step 6: s['c']

```python
s['c']
```

### Step 7: s[5]

```python
s[5]
```

### Step 8: Assign unknown = 0

```python
s[5] = 0
```

### Step 9: s[5]

```python
s[5]
```

### Step 10: Assign unknown = 0

```python
s[5] = 0
```


## Complete Example

```python
# Workflow
s = Series(np.random.default_rng(2).standard_normal(5), index=['a', 'b', 'a', 'a', 'b'])
warn_msg = 'Series.__[sg]etitem__ treating keys as positions is deprecated'
msg = 'index 5 is out of bounds for axis 0 with size 5'
with pytest.raises(IndexError, match=msg):
    with tm.assert_produces_warning(FutureWarning, match=warn_msg):
        s[5]
with pytest.raises(IndexError, match=msg):
    with tm.assert_produces_warning(FutureWarning, match=warn_msg):
        s[5] = 0
with pytest.raises(KeyError, match="^'c'$"):
    s['c']
s = s.sort_index()
with pytest.raises(IndexError, match=msg):
    with tm.assert_produces_warning(FutureWarning, match=warn_msg):
        s[5]
msg = 'index 5 is out of bounds for axis (0|1) with size 5|^5$'
with pytest.raises(IndexError, match=msg):
    with tm.assert_produces_warning(FutureWarning, match=warn_msg):
        s[5] = 0
```

## Next Steps


---

*Source: test_indexing.py:30 | Complexity: Advanced | Last updated: 2026-06-02*