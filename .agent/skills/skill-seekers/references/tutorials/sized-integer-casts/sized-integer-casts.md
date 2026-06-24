# How To: Sized Integer Casts

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test sized integer casts

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `copy`
- `itertools`
- `os`
- `pickle`
- `string`
- `sys`
- `tempfile`
- `pytest`
- `numpy`
- `numpy._core.tests._natype`
- `numpy.dtypes`
- `numpy.testing`
- `numpy.lib._stride_tricks_impl`

**Setup Required:**
```python
# Fixtures: bitsize, signed
```

## Step-by-Step Guide

### Step 1: Assign idtype = value

```python
idtype = f'int{bitsize}'
```

**Verification:**
```python
assert_array_equal(ainp, ainp.astype('T').astype(idtype))
```

### Step 2: Assign ainp = np.array(...)

```python
ainp = np.array(inp, dtype=idtype)
```

### Step 3: Call assert_array_equal()

```python
assert_array_equal(ainp, ainp.astype('T').astype(idtype))
```

### Step 4: Call ainp.astype()

```python
ainp.astype('T', casting='safe')
```

### Step 5: Assign oob = value

```python
oob = [str(2 ** bitsize), str(-2 ** bitsize)]
```

### Step 6: Assign inp = value

```python
inp = [-(2 ** p - 1) for p in reversed(range(bitsize - 1))]
```

### Step 7: Assign idtype = value

```python
idtype = 'u' + idtype
```

### Step 8: Assign inp = value

```python
inp = [2 ** p - 1 for p in range(bitsize)]
```

### Step 9: Call ainp.astype.astype()

```python
ainp.astype('T').astype(idtype, casting='safe')
```

### Step 10: Call np.array.astype()

```python
np.array(oob, dtype='T').astype(idtype)
```

### Step 11: Call np.array.astype()

```python
np.array(['1', np.nan, '3'], dtype=StringDType(na_object=np.nan)).astype(idtype)
```


## Complete Example

```python
# Setup
# Fixtures: bitsize, signed

# Workflow
idtype = f'int{bitsize}'
if signed:
    inp = [-(2 ** p - 1) for p in reversed(range(bitsize - 1))]
    inp += [2 ** p - 1 for p in range(1, bitsize - 1)]
else:
    idtype = 'u' + idtype
    inp = [2 ** p - 1 for p in range(bitsize)]
ainp = np.array(inp, dtype=idtype)
assert_array_equal(ainp, ainp.astype('T').astype(idtype))
ainp.astype('T', casting='safe')
with pytest.raises(TypeError):
    ainp.astype('T').astype(idtype, casting='safe')
oob = [str(2 ** bitsize), str(-2 ** bitsize)]
with pytest.raises(OverflowError):
    np.array(oob, dtype='T').astype(idtype)
with pytest.raises(ValueError):
    np.array(['1', np.nan, '3'], dtype=StringDType(na_object=np.nan)).astype(idtype)
```

## Next Steps


---

*Source: test_stringdtype.py:703 | Complexity: Advanced | Last updated: 2026-06-02*