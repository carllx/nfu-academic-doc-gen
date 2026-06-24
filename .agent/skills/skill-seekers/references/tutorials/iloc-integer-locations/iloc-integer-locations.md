# How To: Iloc Integer Locations

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test iloc integer locations

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign data = value

```python
data = [['str00', 'str01'], ['str10', 'str11'], ['str20', 'srt21'], ['str30', 'str31'], ['str40', 'str41']]
```

### Step 2: Assign index = MultiIndex.from_tuples(...)

```python
index = MultiIndex.from_tuples([('CC', 'A'), ('CC', 'B'), ('CC', 'B'), ('BB', 'a'), ('BB', 'b')])
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame(data)
```

### Step 4: Assign df = DataFrame(...)

```python
df = DataFrame(data, index=index)
```

### Step 5: Assign result = DataFrame(...)

```python
result = DataFrame([[df.iloc[r, c] for c in range(2)] for r in range(5)])
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
data = [['str00', 'str01'], ['str10', 'str11'], ['str20', 'srt21'], ['str30', 'str31'], ['str40', 'str41']]
index = MultiIndex.from_tuples([('CC', 'A'), ('CC', 'B'), ('CC', 'B'), ('BB', 'a'), ('BB', 'b')])
expected = DataFrame(data)
df = DataFrame(data, index=index)
result = DataFrame([[df.iloc[r, c] for c in range(2)] for r in range(5)])
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_iloc.py:118 | Complexity: Intermediate | Last updated: 2026-06-02*