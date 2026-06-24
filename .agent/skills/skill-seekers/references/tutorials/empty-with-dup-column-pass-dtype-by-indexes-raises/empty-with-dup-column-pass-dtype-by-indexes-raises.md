# How To: Empty With Dup Column Pass Dtype By Indexes Raises

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test empty with dup column pass dtype by indexes raises

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

### Step 2: Assign expected = concat(...)

```python
expected = concat([Series([], name='one', dtype='u1'), Series([], name='one.1', dtype='f')], axis=1)
```

### Step 3: Assign expected.index = expected.index.astype(...)

```python
expected.index = expected.index.astype(object)
```

### Step 4: Assign data = ''

```python
data = ''
```

### Step 5: Call parser.read_csv()

```python
parser.read_csv(StringIO(data), names=['one', 'one'], dtype={0: 'u1', 1: 'f'})
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers

# Workflow
parser = all_parsers
expected = concat([Series([], name='one', dtype='u1'), Series([], name='one.1', dtype='f')], axis=1)
expected.index = expected.index.astype(object)
with pytest.raises(ValueError, match='Duplicate names'):
    data = ''
    parser.read_csv(StringIO(data), names=['one', 'one'], dtype={0: 'u1', 1: 'f'})
```

## Next Steps


---

*Source: test_empty.py:118 | Complexity: Intermediate | Last updated: 2026-06-02*