# How To: Empty With Multi Index Pass Dtype

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test empty with multi index pass dtype

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `io`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: all_parsers
```

## Step-by-Step Guide

### Step 1: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 2: Assign data = 'one,two,three'

```python
data = 'one,two,three'
```

### Step 3: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(data), index_col=['one', 'two'], dtype={'one': 'u1', 1: 'f8'})
```

### Step 4: Assign exp_idx = MultiIndex.from_arrays(...)

```python
exp_idx = MultiIndex.from_arrays([np.empty(0, dtype='u1'), np.empty(0, dtype=np.float64)], names=['one', 'two'])
```

### Step 5: Assign expected = DataFrame(...)

```python
expected = DataFrame({'three': np.empty(0, dtype=object)}, index=exp_idx)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers

# Workflow
parser = all_parsers
data = 'one,two,three'
result = parser.read_csv(StringIO(data), index_col=['one', 'two'], dtype={'one': 'u1', 1: 'f8'})
exp_idx = MultiIndex.from_arrays([np.empty(0, dtype='u1'), np.empty(0, dtype=np.float64)], names=['one', 'two'])
expected = DataFrame({'three': np.empty(0, dtype=object)}, index=exp_idx)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_empty.py:62 | Complexity: Intermediate | Last updated: 2026-06-02*