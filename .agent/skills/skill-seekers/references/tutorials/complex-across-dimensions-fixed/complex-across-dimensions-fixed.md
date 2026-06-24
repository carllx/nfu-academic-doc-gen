# How To: Complex Across Dimensions Fixed

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test complex across dimensions fixed

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tests.io.pytables.common`
- `pandas.io.pytables`

**Setup Required:**
```python
# Fixtures: tmp_path, setup_path
```

## Step-by-Step Guide

### Step 1: Assign complex128 = np.array(...)

```python
complex128 = np.array([1.0 + 1j, 1.0 + 1j, 1.0 + 1j, 1.0 + 1j])
```

### Step 2: Assign s = Series(...)

```python
s = Series(complex128, index=list('abcd'))
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame({'A': s, 'B': s})
```

### Step 4: Assign objs = value

```python
objs = [s, df]
```

### Step 5: Assign comps = value

```python
comps = [tm.assert_series_equal, tm.assert_frame_equal]
```

### Step 6: Assign path = value

```python
path = tmp_path / setup_path
```

### Step 7: Call obj.to_hdf()

```python
obj.to_hdf(path, key='obj', format='fixed')
```

### Step 8: Assign reread = read_hdf(...)

```python
reread = read_hdf(path, 'obj')
```

### Step 9: Call comp()

```python
comp(obj, reread)
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path, setup_path

# Workflow
complex128 = np.array([1.0 + 1j, 1.0 + 1j, 1.0 + 1j, 1.0 + 1j])
s = Series(complex128, index=list('abcd'))
df = DataFrame({'A': s, 'B': s})
objs = [s, df]
comps = [tm.assert_series_equal, tm.assert_frame_equal]
for obj, comp in zip(objs, comps):
    path = tmp_path / setup_path
    obj.to_hdf(path, key='obj', format='fixed')
    reread = read_hdf(path, 'obj')
    comp(obj, reread)
```

## Next Steps


---

*Source: test_complex.py:114 | Complexity: Advanced | Last updated: 2026-06-02*