# How To: Unsortedindex Doc Examples

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test unsortedindex doc examples

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas._testing`
- `pandas.core.indexes.frozen`


## Step-by-Step Guide

### Step 1: Assign dfm = DataFrame(...)

```python
dfm = DataFrame({'jim': [0, 0, 1, 1], 'joe': ['x', 'x', 'z', 'y'], 'jolie': np.random.default_rng(2).random(4)})
```

**Verification:**
```python
assert not dfm.index._is_lexsorted()
```

### Step 2: Assign dfm = dfm.set_index(...)

```python
dfm = dfm.set_index(['jim', 'joe'])
```

**Verification:**
```python
assert dfm.index._lexsort_depth == 1
```

### Step 3: Assign msg = 'Key length \\(2\\) was greater than MultiIndex lexsort depth \\(1\\)'

```python
msg = 'Key length \\(2\\) was greater than MultiIndex lexsort depth \\(1\\)'
```

**Verification:**
```python
assert dfm.index._is_lexsorted()
```

### Step 4: Assign dfm = dfm.sort_index(...)

```python
dfm = dfm.sort_index()
```

**Verification:**
```python
assert dfm.index._lexsort_depth == 2
```

### Step 5: dfm.loc[1, 'z']

```python
dfm.loc[1, 'z']
```

### Step 6: dfm.loc[(0, 'y'):(1, 'z')]

```python
dfm.loc[(0, 'y'):(1, 'z')]
```

**Verification:**
```python
assert dfm.index._is_lexsorted()
```

### Step 7: dfm.loc[1, 'z']

```python
dfm.loc[1, 'z']
```

### Step 8: dfm.loc[(0, 'y'):(1, 'z')]

```python
dfm.loc[(0, 'y'):(1, 'z')]
```


## Complete Example

```python
# Workflow
dfm = DataFrame({'jim': [0, 0, 1, 1], 'joe': ['x', 'x', 'z', 'y'], 'jolie': np.random.default_rng(2).random(4)})
dfm = dfm.set_index(['jim', 'joe'])
with tm.assert_produces_warning(PerformanceWarning):
    dfm.loc[1, 'z']
msg = 'Key length \\(2\\) was greater than MultiIndex lexsort depth \\(1\\)'
with pytest.raises(UnsortedIndexError, match=msg):
    dfm.loc[(0, 'y'):(1, 'z')]
assert not dfm.index._is_lexsorted()
assert dfm.index._lexsort_depth == 1
dfm = dfm.sort_index()
dfm.loc[1, 'z']
dfm.loc[(0, 'y'):(1, 'z')]
assert dfm.index._is_lexsorted()
assert dfm.index._lexsort_depth == 2
```

## Next Steps


---

*Source: test_sorting.py:138 | Complexity: Advanced | Last updated: 2026-06-02*