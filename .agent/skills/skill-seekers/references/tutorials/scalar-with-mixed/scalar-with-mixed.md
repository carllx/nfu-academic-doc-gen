# How To: Scalar With Mixed

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test scalar with mixed

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: indexer_sl
```

## Step-by-Step Guide

### Step 1: Assign s2 = Series(...)

```python
s2 = Series([1, 2, 3], index=['a', 'b', 'c'])
```

**Verification:**
```python
assert result == expected
```

### Step 2: Assign s3 = Series(...)

```python
s3 = Series([1, 2, 3], index=['a', 'b', 1.5])
```

**Verification:**
```python
assert result == expected
```

### Step 3: Assign result = value

```python
result = indexer_sl(s2)['b']
```

**Verification:**
```python
assert result == expected
```

### Step 4: Assign expected = 2

```python
expected = 2
```

**Verification:**
```python
assert result == expected
```

### Step 5: Assign result = value

```python
result = indexer_sl(s3)[1.5]
```

### Step 6: Assign expected = 3

```python
expected = 3
```

**Verification:**
```python
assert result == expected
```

### Step 7: indexer_sl(s2)[1.0]

```python
indexer_sl(s2)[1.0]
```

### Step 8: indexer_sl(s2)[1.0]

```python
indexer_sl(s2)[1.0]
```

### Step 9: indexer_sl(s3)[1.0]

```python
indexer_sl(s3)[1.0]
```

### Step 10: Assign msg = 'Series.__getitem__ treating keys as positions is deprecated'

```python
msg = 'Series.__getitem__ treating keys as positions is deprecated'
```

### Step 11: Assign expected = 2

```python
expected = 2
```

**Verification:**
```python
assert result == expected
```

### Step 12: indexer_sl(s3)[1.0]

```python
indexer_sl(s3)[1.0]
```

### Step 13: Assign result = value

```python
result = s3[1]
```


## Complete Example

```python
# Setup
# Fixtures: indexer_sl

# Workflow
s2 = Series([1, 2, 3], index=['a', 'b', 'c'])
s3 = Series([1, 2, 3], index=['a', 'b', 1.5])
with pytest.raises(KeyError, match='^1.0$'):
    indexer_sl(s2)[1.0]
with pytest.raises(KeyError, match='^1\\.0$'):
    indexer_sl(s2)[1.0]
result = indexer_sl(s2)['b']
expected = 2
assert result == expected
with pytest.raises(KeyError, match='^1.0$'):
    indexer_sl(s3)[1.0]
if indexer_sl is not tm.loc:
    msg = 'Series.__getitem__ treating keys as positions is deprecated'
    with tm.assert_produces_warning(FutureWarning, match=msg):
        result = s3[1]
    expected = 2
    assert result == expected
with pytest.raises(KeyError, match='^1\\.0$'):
    indexer_sl(s3)[1.0]
result = indexer_sl(s3)[1.5]
expected = 3
assert result == expected
```

## Next Steps


---

*Source: test_floats.py:99 | Complexity: Advanced | Last updated: 2026-06-02*