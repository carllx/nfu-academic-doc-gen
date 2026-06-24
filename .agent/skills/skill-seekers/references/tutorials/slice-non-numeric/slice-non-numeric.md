# How To: Slice Non Numeric

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test slice non numeric

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: index, idx, frame_or_series, indexer_sli
```

## Step-by-Step Guide

### Step 1: Assign s = gen_obj(...)

```python
s = gen_obj(frame_or_series, index)
```

### Step 2: Assign msg = value

```python
msg = f'cannot do positional indexing on {type(index).__name__} with these indexers \\[(3|4)\\.0\\] of type float'
```

### Step 3: Assign msg = value

```python
msg = f'cannot do slice indexing on {type(index).__name__} with these indexers \\[(3|4)(\\.0)?\\] of type (float|int)'
```

### Step 4: indexer_sli(s)[idx]

```python
indexer_sli(s)[idx]
```

### Step 5: Assign msg = 'slice indices must be integers or None or have an __index__ method'

```python
msg = 'slice indices must be integers or None or have an __index__ method'
```

### Step 6: Assign unknown = 0

```python
indexer_sli(s)[idx] = 0
```


## Complete Example

```python
# Setup
# Fixtures: index, idx, frame_or_series, indexer_sli

# Workflow
s = gen_obj(frame_or_series, index)
if indexer_sli is tm.iloc:
    msg = f'cannot do positional indexing on {type(index).__name__} with these indexers \\[(3|4)\\.0\\] of type float'
else:
    msg = f'cannot do slice indexing on {type(index).__name__} with these indexers \\[(3|4)(\\.0)?\\] of type (float|int)'
with pytest.raises(TypeError, match=msg):
    indexer_sli(s)[idx]
if indexer_sli is tm.iloc:
    msg = 'slice indices must be integers or None or have an __index__ method'
with pytest.raises(TypeError, match=msg):
    indexer_sli(s)[idx] = 0
```

## Next Steps


---

*Source: test_floats.py:230 | Complexity: Intermediate | Last updated: 2026-06-02*