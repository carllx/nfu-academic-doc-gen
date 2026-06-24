# How To: To String With Formatters Unicode

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test to string with formatters unicode

## Prerequisites

**Required Modules:**
- `datetime`
- `io`
- `re`
- `sys`
- `textwrap`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'c/σ': [1, 2, 3]})
```

**Verification:**
```python
assert result == expected
```

### Step 2: Assign result = df.to_string(...)

```python
result = df.to_string(formatters={'c/σ': str})
```

**Verification:**
```python
assert rs == xp
```

### Step 3: Assign expected = dedent(...)

```python
expected = dedent('              c/σ\n            0   1\n            1   2\n            2   3')
```

**Verification:**
```python
assert result == expected
```

### Step 4: Assign df = DataFrame(...)

```python
df = DataFrame([range(5), range(5, 10), range(10, 15)])
```

### Step 5: Assign rs = df.to_string(...)

```python
rs = df.to_string(formatters={'__index__': lambda x: 'abc'[x]})
```

### Step 6: Assign xp = dedent(...)

```python
xp = dedent('                0   1   2   3   4\n            a   0   1   2   3   4\n            b   5   6   7   8   9\n            c  10  11  12  13  14            ')
```

**Verification:**
```python
assert rs == xp
```


## Complete Example

```python
# Workflow
df = DataFrame({'c/σ': [1, 2, 3]})
result = df.to_string(formatters={'c/σ': str})
expected = dedent('              c/σ\n            0   1\n            1   2\n            2   3')
assert result == expected

def test_to_string_index_formatter(self):
    df = DataFrame([range(5), range(5, 10), range(10, 15)])
    rs = df.to_string(formatters={'__index__': lambda x: 'abc'[x]})
    xp = dedent('                0   1   2   3   4\n            a   0   1   2   3   4\n            b   5   6   7   8   9\n            c  10  11  12  13  14            ')
    assert rs == xp
```

## Next Steps


---

*Source: test_to_string.py:113 | Complexity: Intermediate | Last updated: 2026-06-02*