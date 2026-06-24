# How To: Loc Slice Negative Stepsize

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test loc slice negative stepsize

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tests.indexing.common`

**Setup Required:**
```python
# Fixtures: dtype, loc, iloc
```

## Step-by-Step Guide

### Step 1: Assign labels = value

```python
labels = {'str': list('abcde'), 'int': range(5)}[dtype]
```

### Step 2: Assign mi = MultiIndex.from_arrays(...)

```python
mi = MultiIndex.from_arrays([labels] * 2)
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame(1.0, index=mi, columns=['A'])
```

### Step 4: Assign SLC = value

```python
SLC = pd.IndexSlice
```

### Step 5: Assign expected = value

```python
expected = df.iloc[iloc, :]
```

### Step 6: Assign result_get_loc = value

```python
result_get_loc = df.loc[SLC[loc], :]
```

### Step 7: Assign result_get_locs_level_0 = value

```python
result_get_locs_level_0 = df.loc[SLC[loc, :], :]
```

### Step 8: Assign result_get_locs_level_1 = value

```python
result_get_locs_level_1 = df.loc[SLC[:, loc], :]
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result_get_loc, expected)
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result_get_locs_level_0, expected)
```

### Step 11: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result_get_locs_level_1, expected)
```


## Complete Example

```python
# Setup
# Fixtures: dtype, loc, iloc

# Workflow
labels = {'str': list('abcde'), 'int': range(5)}[dtype]
mi = MultiIndex.from_arrays([labels] * 2)
df = DataFrame(1.0, index=mi, columns=['A'])
SLC = pd.IndexSlice
expected = df.iloc[iloc, :]
result_get_loc = df.loc[SLC[loc], :]
result_get_locs_level_0 = df.loc[SLC[loc, :], :]
result_get_locs_level_1 = df.loc[SLC[:, loc], :]
tm.assert_frame_equal(result_get_loc, expected)
tm.assert_frame_equal(result_get_locs_level_0, expected)
tm.assert_frame_equal(result_get_locs_level_1, expected)
```

## Next Steps


---

*Source: test_slice.py:777 | Complexity: Advanced | Last updated: 2026-06-02*