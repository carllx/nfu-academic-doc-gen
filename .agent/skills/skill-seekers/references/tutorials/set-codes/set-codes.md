# How To: Set Codes

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test set codes

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: idx
```

## Step-by-Step Guide

### Step 1: Assign codes = value

```python
codes = idx.codes
```

**Verification:**
```python
assert_matching(ind2.codes, new_codes)
```

### Step 2: Assign unknown = codes

```python
major_codes, minor_codes = codes
```

**Verification:**
```python
assert_matching(idx.codes, codes)
```

### Step 3: Assign major_codes = value

```python
major_codes = [(x + 1) % 3 for x in major_codes]
```

**Verification:**
```python
assert_matching(ind2.codes, [new_codes[0], codes[1]])
```

### Step 4: Assign minor_codes = value

```python
minor_codes = [(x + 1) % 1 for x in minor_codes]
```

**Verification:**
```python
assert_matching(idx.codes, codes)
```

### Step 5: Assign new_codes = value

```python
new_codes = [major_codes, minor_codes]
```

**Verification:**
```python
assert_matching(ind2.codes, [codes[0], new_codes[1]])
```

### Step 6: Assign ind2 = idx.set_codes(...)

```python
ind2 = idx.set_codes(new_codes)
```

**Verification:**
```python
assert_matching(idx.codes, codes)
```

### Step 7: Call assert_matching()

```python
assert_matching(ind2.codes, new_codes)
```

**Verification:**
```python
assert_matching(ind2.codes, new_codes)
```

### Step 8: Call assert_matching()

```python
assert_matching(idx.codes, codes)
```

**Verification:**
```python
assert_matching(idx.codes, codes)
```

### Step 9: Assign ind2 = idx.set_codes(...)

```python
ind2 = idx.set_codes(new_codes[0], level=0)
```

**Verification:**
```python
assert result.equals(expected)
```

### Step 10: Call assert_matching()

```python
assert_matching(ind2.codes, [new_codes[0], codes[1]])
```

### Step 11: Call assert_matching()

```python
assert_matching(idx.codes, codes)
```

### Step 12: Assign ind2 = idx.set_codes(...)

```python
ind2 = idx.set_codes(new_codes[1], level=1)
```

### Step 13: Call assert_matching()

```python
assert_matching(ind2.codes, [codes[0], new_codes[1]])
```

### Step 14: Call assert_matching()

```python
assert_matching(idx.codes, codes)
```

### Step 15: Assign ind2 = idx.set_codes(...)

```python
ind2 = idx.set_codes(new_codes, level=[0, 1])
```

### Step 16: Call assert_matching()

```python
assert_matching(ind2.codes, new_codes)
```

### Step 17: Call assert_matching()

```python
assert_matching(idx.codes, codes)
```

### Step 18: Assign ind = MultiIndex.from_tuples(...)

```python
ind = MultiIndex.from_tuples([(0, i) for i in range(130)])
```

### Step 19: Assign new_codes = range(...)

```python
new_codes = range(129, -1, -1)
```

### Step 20: Assign expected = MultiIndex.from_tuples(...)

```python
expected = MultiIndex.from_tuples([(0, i) for i in new_codes])
```

### Step 21: Assign result = ind.set_codes(...)

```python
result = ind.set_codes(codes=new_codes, level=1)
```

**Verification:**
```python
assert result.equals(expected)
```


## Complete Example

```python
# Setup
# Fixtures: idx

# Workflow
codes = idx.codes
major_codes, minor_codes = codes
major_codes = [(x + 1) % 3 for x in major_codes]
minor_codes = [(x + 1) % 1 for x in minor_codes]
new_codes = [major_codes, minor_codes]
ind2 = idx.set_codes(new_codes)
assert_matching(ind2.codes, new_codes)
assert_matching(idx.codes, codes)
ind2 = idx.set_codes(new_codes[0], level=0)
assert_matching(ind2.codes, [new_codes[0], codes[1]])
assert_matching(idx.codes, codes)
ind2 = idx.set_codes(new_codes[1], level=1)
assert_matching(ind2.codes, [codes[0], new_codes[1]])
assert_matching(idx.codes, codes)
ind2 = idx.set_codes(new_codes, level=[0, 1])
assert_matching(ind2.codes, new_codes)
assert_matching(idx.codes, codes)
ind = MultiIndex.from_tuples([(0, i) for i in range(130)])
new_codes = range(129, -1, -1)
expected = MultiIndex.from_tuples([(0, i) for i in new_codes])
result = ind.set_codes(codes=new_codes, level=1)
assert result.equals(expected)
```

## Next Steps


---

*Source: test_get_set.py:207 | Complexity: Advanced | Last updated: 2026-06-02*