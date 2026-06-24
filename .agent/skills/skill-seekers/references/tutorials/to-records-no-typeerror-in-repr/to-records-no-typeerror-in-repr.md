# How To: To Records No Typeerror In Repr

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test to records no typeerror in repr

## Prerequisites

**Required Modules:**
- `datetime`
- `io`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame([['a', 'b'], ['c', 'd'], ['e', 'f']], columns=['left', 'right'])
```

**Verification:**
```python
assert result == expected
```

### Step 2: Assign unknown = unknown.to_records(...)

```python
df['record'] = df[['left', 'right']].to_records()
```

### Step 3: Assign expected = '  left right     record\n0    a     b  [0, a, b]\n1    c     d  [1, c, d]\n2    e     f  [2, e, f]'

```python
expected = '  left right     record\n0    a     b  [0, a, b]\n1    c     d  [1, c, d]\n2    e     f  [2, e, f]'
```

### Step 4: Assign result = repr(...)

```python
result = repr(df)
```

**Verification:**
```python
assert result == expected
```


## Complete Example

```python
# Workflow
df = DataFrame([['a', 'b'], ['c', 'd'], ['e', 'f']], columns=['left', 'right'])
df['record'] = df[['left', 'right']].to_records()
expected = '  left right     record\n0    a     b  [0, a, b]\n1    c     d  [1, c, d]\n2    e     f  [2, e, f]'
result = repr(df)
assert result == expected
```

## Next Steps


---

*Source: test_repr.py:388 | Complexity: Intermediate | Last updated: 2026-06-02*