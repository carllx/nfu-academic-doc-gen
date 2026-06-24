# How To: Default Na Values

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test default na values

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `io`
- `numpy`
- `pytest`
- `pandas._libs.parsers`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: all_parsers
```

## Step-by-Step Guide

### Step 1: Assign _NA_VALUES = value

```python
_NA_VALUES = {'-1.#IND', '1.#QNAN', '1.#IND', '-1.#QNAN', '#N/A', 'N/A', 'n/a', 'NA', '<NA>', '#NA', 'NULL', 'null', 'NaN', 'nan', '-NaN', '-nan', '#N/A N/A', '', 'None'}
```

**Verification:**
```python
assert _NA_VALUES == STR_NA_VALUES
```

### Step 2: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 3: Assign nv = len(...)

```python
nv = len(_NA_VALUES)
```

### Step 4: Assign data = StringIO(...)

```python
data = StringIO('\n'.join([f(i, v) for i, v in enumerate(_NA_VALUES)]))
```

### Step 5: Assign expected = DataFrame(...)

```python
expected = DataFrame(np.nan, columns=range(nv), index=range(nv))
```

### Step 6: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(data, header=None)
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 8: Assign buf = value

```python
buf = f'{buf}{v}'
```

### Step 9: Assign buf = ''

```python
buf = ''
```

### Step 10: Assign joined = unknown.join(...)

```python
joined = ''.join([','] * (nv - i - 1))
```

### Step 11: Assign buf = value

```python
buf = f'{buf}{joined}'
```

### Step 12: Assign buf = unknown.join(...)

```python
buf = ''.join([','] * i)
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers

# Workflow
_NA_VALUES = {'-1.#IND', '1.#QNAN', '1.#IND', '-1.#QNAN', '#N/A', 'N/A', 'n/a', 'NA', '<NA>', '#NA', 'NULL', 'null', 'NaN', 'nan', '-NaN', '-nan', '#N/A N/A', '', 'None'}
assert _NA_VALUES == STR_NA_VALUES
parser = all_parsers
nv = len(_NA_VALUES)

def f(i, v):
    if i == 0:
        buf = ''
    elif i > 0:
        buf = ''.join([','] * i)
    buf = f'{buf}{v}'
    if i < nv - 1:
        joined = ''.join([','] * (nv - i - 1))
        buf = f'{buf}{joined}'
    return buf
data = StringIO('\n'.join([f(i, v) for i, v in enumerate(_NA_VALUES)]))
expected = DataFrame(np.nan, columns=range(nv), index=range(nv))
result = parser.read_csv(data, header=None)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_na_values.py:113 | Complexity: Advanced | Last updated: 2026-06-02*