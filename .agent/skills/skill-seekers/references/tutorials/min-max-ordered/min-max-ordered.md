# How To: Min Max Ordered

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test min max ordered

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `re`
- `sys`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas`
- `pandas._testing`
- `pandas.api.types`

**Setup Required:**
```python
# Fixtures: index_or_series_or_array
```

## Step-by-Step Guide

### Step 1: Assign cat = Categorical(...)

```python
cat = Categorical(['a', 'b', 'c', 'd'], ordered=True)
```

**Verification:**
```python
assert _min == 'a'
```

### Step 2: Assign obj = index_or_series_or_array(...)

```python
obj = index_or_series_or_array(cat)
```

**Verification:**
```python
assert _max == 'd'
```

### Step 3: Assign _min = obj.min(...)

```python
_min = obj.min()
```

**Verification:**
```python
assert np.minimum.reduce(obj) == 'a'
```

### Step 4: Assign _max = obj.max(...)

```python
_max = obj.max()
```

**Verification:**
```python
assert np.maximum.reduce(obj) == 'd'
```

### Step 5: Assign cat = Categorical(...)

```python
cat = Categorical(['a', 'b', 'c', 'd'], categories=['d', 'c', 'b', 'a'], ordered=True)
```

**Verification:**
```python
assert _min == 'd'
```

### Step 6: Assign obj = index_or_series_or_array(...)

```python
obj = index_or_series_or_array(cat)
```

**Verification:**
```python
assert _max == 'a'
```

### Step 7: Assign _min = obj.min(...)

```python
_min = obj.min()
```

**Verification:**
```python
assert np.minimum.reduce(obj) == 'd'
```

### Step 8: Assign _max = obj.max(...)

```python
_max = obj.max()
```

**Verification:**
```python
assert np.maximum.reduce(obj) == 'a'
```


## Complete Example

```python
# Setup
# Fixtures: index_or_series_or_array

# Workflow
cat = Categorical(['a', 'b', 'c', 'd'], ordered=True)
obj = index_or_series_or_array(cat)
_min = obj.min()
_max = obj.max()
assert _min == 'a'
assert _max == 'd'
assert np.minimum.reduce(obj) == 'a'
assert np.maximum.reduce(obj) == 'd'
cat = Categorical(['a', 'b', 'c', 'd'], categories=['d', 'c', 'b', 'a'], ordered=True)
obj = index_or_series_or_array(cat)
_min = obj.min()
_max = obj.max()
assert _min == 'd'
assert _max == 'a'
assert np.minimum.reduce(obj) == 'd'
assert np.maximum.reduce(obj) == 'a'
```

## Next Steps


---

*Source: test_analytics.py:37 | Complexity: Advanced | Last updated: 2026-06-02*