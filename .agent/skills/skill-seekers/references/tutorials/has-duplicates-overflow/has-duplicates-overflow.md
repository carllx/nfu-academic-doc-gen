# How To: Has Duplicates Overflow

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test has duplicates overflow

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `itertools`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: nlevels, with_nulls
```

## Step-by-Step Guide

### Step 1: Assign codes = np.tile(...)

```python
codes = np.tile(np.arange(500), 2)
```

**Verification:**
```python
assert not mi.has_duplicates
```

### Step 2: Assign level = np.arange(...)

```python
level = np.arange(500)
```

**Verification:**
```python
assert mi.has_duplicates
```

### Step 3: Assign levels = value

```python
levels = [level] * nlevels + [[0, 1]]
```

### Step 4: Assign mi = MultiIndex(...)

```python
mi = MultiIndex(levels=levels, codes=codes)
```

**Verification:**
```python
assert not mi.has_duplicates
```

### Step 5: Assign unknown = value

```python
codes[500] = -1
```

### Step 6: Assign codes = value

```python
codes = [codes.copy() for i in range(nlevels)]
```

### Step 7: Assign codes = value

```python
codes = [codes] * nlevels + [np.arange(2).repeat(500)]
```

### Step 8: Assign codes = list(...)

```python
codes = list(map(f, codes))
```

### Step 9: Assign mi = MultiIndex(...)

```python
mi = MultiIndex(levels=levels, codes=codes)
```

### Step 10: Assign values = mi.values.tolist(...)

```python
values = mi.values.tolist()
```

### Step 11: Assign mi = MultiIndex.from_tuples(...)

```python
mi = MultiIndex.from_tuples(values + [values[0]])
```

### Step 12: Assign unknown = value

```python
codes[i][500 + i - nlevels // 2] = -1
```


## Complete Example

```python
# Setup
# Fixtures: nlevels, with_nulls

# Workflow
codes = np.tile(np.arange(500), 2)
level = np.arange(500)
if with_nulls:
    codes[500] = -1
    codes = [codes.copy() for i in range(nlevels)]
    for i in range(nlevels):
        codes[i][500 + i - nlevels // 2] = -1
    codes += [np.array([-1, 1]).repeat(500)]
else:
    codes = [codes] * nlevels + [np.arange(2).repeat(500)]
levels = [level] * nlevels + [[0, 1]]
mi = MultiIndex(levels=levels, codes=codes)
assert not mi.has_duplicates
if with_nulls:

    def f(a):
        return np.insert(a, 1000, a[0])
    codes = list(map(f, codes))
    mi = MultiIndex(levels=levels, codes=codes)
else:
    values = mi.values.tolist()
    mi = MultiIndex.from_tuples(values + [values[0]])
assert mi.has_duplicates
```

## Next Steps


---

*Source: test_duplicates.py:205 | Complexity: Advanced | Last updated: 2026-06-02*