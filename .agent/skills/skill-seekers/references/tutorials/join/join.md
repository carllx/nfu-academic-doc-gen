# How To: Join

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test join

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
- `pandas.core.reshape.concat`

**Setup Required:**
```python
# Fixtures: multiindex_dataframe_random_data
```

## Step-by-Step Guide

### Step 1: Assign frame = multiindex_dataframe_random_data

```python
frame = multiindex_dataframe_random_data
```

**Verification:**
```python
assert not np.isnan(joined.values).all()
```

### Step 2: Assign a = value

```python
a = frame.loc[frame.index[:5], ['A']]
```

### Step 3: Assign b = value

```python
b = frame.loc[frame.index[2:], ['B', 'C']]
```

### Step 4: Assign joined = a.join.reindex(...)

```python
joined = a.join(b, how='outer').reindex(frame.index)
```

### Step 5: Assign expected = frame.copy.values.copy(...)

```python
expected = frame.copy().values.copy()
```

### Step 6: Assign unknown = value

```python
expected[np.isnan(joined.values)] = np.nan
```

### Step 7: Assign expected = DataFrame(...)

```python
expected = DataFrame(expected, index=frame.index, columns=frame.columns)
```

**Verification:**
```python
assert not np.isnan(joined.values).all()
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(joined, expected)
```


## Complete Example

```python
# Setup
# Fixtures: multiindex_dataframe_random_data

# Workflow
frame = multiindex_dataframe_random_data
a = frame.loc[frame.index[:5], ['A']]
b = frame.loc[frame.index[2:], ['B', 'C']]
joined = a.join(b, how='outer').reindex(frame.index)
expected = frame.copy().values.copy()
expected[np.isnan(joined.values)] = np.nan
expected = DataFrame(expected, index=frame.index, columns=frame.columns)
assert not np.isnan(joined.values).all()
tm.assert_frame_equal(joined, expected)
```

## Next Steps


---

*Source: test_join.py:418 | Complexity: Advanced | Last updated: 2026-06-02*