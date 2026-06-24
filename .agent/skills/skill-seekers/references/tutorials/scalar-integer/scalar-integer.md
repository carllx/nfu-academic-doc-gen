# How To: Scalar Integer

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test scalar integer

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: index, frame_or_series, indexer_sl
```

## Step-by-Step Guide

### Step 1: Assign getitem = value

```python
getitem = indexer_sl is not tm.loc
```

**Verification:**
```python
assert x == y
```

### Step 2: Assign i = index

```python
i = index
```

### Step 3: Assign obj = gen_obj(...)

```python
obj = gen_obj(frame_or_series, i)
```

### Step 4: Assign result = value

```python
result = indexer_sl(obj)[3.0]
```

### Step 5: Call self.check()

```python
self.check(result, obj, 3, getitem)
```

### Step 6: Assign s2 = obj.copy(...)

```python
s2 = obj.copy()
```

### Step 7: Assign unknown = 100

```python
indexer_sl(s2)[3.0] = 100
```

### Step 8: Assign result = value

```python
result = indexer_sl(s2)[3.0]
```

### Step 9: Call compare()

```python
compare(result, expected)
```

### Step 10: Assign result = value

```python
result = indexer_sl(s2)[3]
```

### Step 11: Call compare()

```python
compare(result, expected)
```

### Step 12: Assign expected = 100

```python
expected = 100
```

### Step 13: Assign compare = value

```python
compare = tm.assert_series_equal
```

**Verification:**
```python
assert x == y
```

### Step 14: Assign expected = Series(...)

```python
expected = Series(100, index=range(len(obj)), name=3)
```

### Step 15: Assign expected = Series(...)

```python
expected = Series(100.0, index=range(len(obj)), name=3)
```


## Complete Example

```python
# Setup
# Fixtures: index, frame_or_series, indexer_sl

# Workflow
getitem = indexer_sl is not tm.loc
i = index
obj = gen_obj(frame_or_series, i)
result = indexer_sl(obj)[3.0]
self.check(result, obj, 3, getitem)
if isinstance(obj, Series):

    def compare(x, y):
        assert x == y
    expected = 100
else:
    compare = tm.assert_series_equal
    if getitem:
        expected = Series(100, index=range(len(obj)), name=3)
    else:
        expected = Series(100.0, index=range(len(obj)), name=3)
s2 = obj.copy()
indexer_sl(s2)[3.0] = 100
result = indexer_sl(s2)[3.0]
compare(result, expected)
result = indexer_sl(s2)[3]
compare(result, expected)
```

## Next Steps


---

*Source: test_floats.py:138 | Complexity: Advanced | Last updated: 2026-06-02*