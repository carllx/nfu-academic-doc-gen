# How To: Merge Na Keys

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test merge na keys

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.reshape.concat`
- `pandas.core.reshape.merge`


## Step-by-Step Guide

### Step 1: Assign data = value

```python
data = [[1950, 'A', 1.5], [1950, 'B', 1.5], [1955, 'B', 1.5], [1960, 'B', np.nan], [1970, 'B', 4.0], [1950, 'C', 4.0], [1960, 'C', np.nan], [1965, 'C', 3.0], [1970, 'C', 4.0]]
```

### Step 2: Assign frame = DataFrame(...)

```python
frame = DataFrame(data, columns=['year', 'panel', 'data'])
```

### Step 3: Assign other_data = value

```python
other_data = [[1960, 'A', np.nan], [1970, 'A', np.nan], [1955, 'A', np.nan], [1965, 'A', np.nan], [1965, 'B', np.nan], [1955, 'C', np.nan]]
```

### Step 4: Assign other = DataFrame(...)

```python
other = DataFrame(other_data, columns=['year', 'panel', 'data'])
```

### Step 5: Assign result = frame.merge(...)

```python
result = frame.merge(other, how='outer')
```

### Step 6: Assign expected = frame.fillna.merge(...)

```python
expected = frame.fillna(-999).merge(other.fillna(-999), how='outer')
```

### Step 7: Assign expected = expected.replace(...)

```python
expected = expected.replace(-999, np.nan)
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
data = [[1950, 'A', 1.5], [1950, 'B', 1.5], [1955, 'B', 1.5], [1960, 'B', np.nan], [1970, 'B', 4.0], [1950, 'C', 4.0], [1960, 'C', np.nan], [1965, 'C', 3.0], [1970, 'C', 4.0]]
frame = DataFrame(data, columns=['year', 'panel', 'data'])
other_data = [[1960, 'A', np.nan], [1970, 'A', np.nan], [1955, 'A', np.nan], [1965, 'A', np.nan], [1965, 'B', np.nan], [1955, 'C', np.nan]]
other = DataFrame(other_data, columns=['year', 'panel', 'data'])
result = frame.merge(other, how='outer')
expected = frame.fillna(-999).merge(other.fillna(-999), how='outer')
expected = expected.replace(-999, np.nan)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_multi.py:418 | Complexity: Advanced | Last updated: 2026-06-02*