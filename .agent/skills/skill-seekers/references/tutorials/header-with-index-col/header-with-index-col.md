# How To: Header With Index Col

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test header with index col

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

### Step 2: Assign data = '\nI11,A,A\nI12,B,B\nI2,1,3\n'

```python
data = '\nI11,A,A\nI12,B,B\nI2,1,3\n'
```

### Step 3: Assign midx = MultiIndex.from_tuples(...)

```python
midx = MultiIndex.from_tuples([('A', 'B'), ('A', 'B.1')], names=['I11', 'I12'])
```

### Step 4: Assign idx = Index(...)

```python
idx = Index(['I2'])
```

### Step 5: Assign expected = DataFrame(...)

```python
expected = DataFrame([[1, 3]], index=idx, columns=midx)
```

### Step 6: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(data), index_col=0, header=[0, 1])
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 8: Assign col_idx = Index(...)

```python
col_idx = Index(['A', 'A.1'])
```

### Step 9: Assign idx = Index(...)

```python
idx = Index(['I12', 'I2'], name='I11')
```

### Step 10: Assign expected = DataFrame(...)

```python
expected = DataFrame([['B', 'B'], ['1', '3']], index=idx, columns=col_idx)
```

### Step 11: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(data), index_col='I11', header=0)
```

### Step 12: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers

# Workflow
parser = all_parsers
data = '\nI11,A,A\nI12,B,B\nI2,1,3\n'
midx = MultiIndex.from_tuples([('A', 'B'), ('A', 'B.1')], names=['I11', 'I12'])
idx = Index(['I2'])
expected = DataFrame([[1, 3]], index=idx, columns=midx)
result = parser.read_csv(StringIO(data), index_col=0, header=[0, 1])
tm.assert_frame_equal(result, expected)
col_idx = Index(['A', 'A.1'])
idx = Index(['I12', 'I2'], name='I11')
expected = DataFrame([['B', 'B'], ['1', '3']], index=idx, columns=col_idx)
result = parser.read_csv(StringIO(data), index_col='I11', header=0)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_index_col.py:218 | Complexity: Advanced | Last updated: 2026-06-02*