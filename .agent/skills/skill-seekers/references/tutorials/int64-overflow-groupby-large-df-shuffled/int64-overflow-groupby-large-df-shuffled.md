# How To: Int64 Overflow Groupby Large Df Shuffled

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test int64 overflow groupby large df shuffled

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `collections`
- `datetime`
- `itertools`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.core.algorithms`
- `pandas.core.common`
- `pandas.core.sorting`

**Setup Required:**
```python
# Fixtures: agg
```

## Step-by-Step Guide

### Step 1: Assign rs = np.random.default_rng(...)

```python
rs = np.random.default_rng(2)
```

**Verification:**
```python
assert is_int64_overflow_possible(gr._grouper.shape)
```

### Step 2: Assign arr = rs.integers(...)

```python
arr = rs.integers(-1 << 12, 1 << 12, (1 << 15, 5))
```

### Step 3: Assign i = rs.choice(...)

```python
i = rs.choice(len(arr), len(arr) * 4)
```

### Step 4: Assign arr = np.vstack(...)

```python
arr = np.vstack((arr, arr[i]))
```

### Step 5: Assign i = rs.permutation(...)

```python
i = rs.permutation(len(arr))
```

### Step 6: Assign arr = value

```python
arr = arr[i]
```

### Step 7: Assign df = DataFrame(...)

```python
df = DataFrame(arr, columns=list('abcde'))
```

### Step 8: Assign unknown = np.zeros(...)

```python
df['jim'], df['joe'] = np.zeros((2, len(df)))
```

### Step 9: Assign gr = df.groupby(...)

```python
gr = df.groupby(list('abcde'))
```

**Verification:**
```python
assert is_int64_overflow_possible(gr._grouper.shape)
```

### Step 10: Assign mi = MultiIndex.from_arrays(...)

```python
mi = MultiIndex.from_arrays([ar.ravel() for ar in np.array_split(np.unique(arr, axis=0), 5, axis=1)], names=list('abcde'))
```

### Step 11: Assign res = DataFrame.sort_index(...)

```python
res = DataFrame(np.zeros((len(mi), 2)), columns=['jim', 'joe'], index=mi).sort_index()
```

### Step 12: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(getattr(gr, agg)(), res)
```


## Complete Example

```python
# Setup
# Fixtures: agg

# Workflow
rs = np.random.default_rng(2)
arr = rs.integers(-1 << 12, 1 << 12, (1 << 15, 5))
i = rs.choice(len(arr), len(arr) * 4)
arr = np.vstack((arr, arr[i]))
i = rs.permutation(len(arr))
arr = arr[i]
df = DataFrame(arr, columns=list('abcde'))
df['jim'], df['joe'] = np.zeros((2, len(df)))
gr = df.groupby(list('abcde'))
assert is_int64_overflow_possible(gr._grouper.shape)
mi = MultiIndex.from_arrays([ar.ravel() for ar in np.array_split(np.unique(arr, axis=0), 5, axis=1)], names=list('abcde'))
res = DataFrame(np.zeros((len(mi), 2)), columns=['jim', 'joe'], index=mi).sort_index()
tm.assert_frame_equal(getattr(gr, agg)(), res)
```

## Next Steps


---

*Source: test_sorting.py:95 | Complexity: Advanced | Last updated: 2026-06-02*