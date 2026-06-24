# How To: Format Subset

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test format subset

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas.io.formats.style`
- `pandas.io.formats.style_render`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame([[0.1234, 0.1234], [1.1234, 1.1234]], columns=['a', 'b'])
```

**Verification:**
```python
assert ctx['body'][0][1]['display_value'] == expected
```

### Step 2: Assign ctx = df.style.format._translate(...)

```python
ctx = df.style.format({'a': '{:0.1f}', 'b': '{0:.2%}'}, subset=IndexSlice[0, :])._translate(True, True)
```

**Verification:**
```python
assert ctx['body'][1][1]['display_value'] == raw_11
```

### Step 3: Assign expected = '0.1'

```python
expected = '0.1'
```

**Verification:**
```python
assert ctx['body'][0][2]['display_value'] == '12.34%'
```

### Step 4: Assign raw_11 = '1.123400'

```python
raw_11 = '1.123400'
```

**Verification:**
```python
assert ctx['body'][0][1]['display_value'] == expected
```

### Step 5: Assign ctx = df.style.format._translate(...)

```python
ctx = df.style.format('{:0.1f}', subset=IndexSlice[0, :])._translate(True, True)
```

**Verification:**
```python
assert ctx['body'][1][1]['display_value'] == raw_11
```

### Step 6: Assign ctx = df.style.format._translate(...)

```python
ctx = df.style.format('{:0.1f}', subset=IndexSlice['a'])._translate(True, True)
```

**Verification:**
```python
assert ctx['body'][0][1]['display_value'] == expected
```

### Step 7: Assign ctx = df.style.format._translate(...)

```python
ctx = df.style.format('{:0.1f}', subset=IndexSlice[0, 'a'])._translate(True, True)
```

**Verification:**
```python
assert ctx['body'][0][2]['display_value'] == '0.123400'
```

### Step 8: Assign ctx = df.style.format._translate(...)

```python
ctx = df.style.format('{:0.1f}', subset=IndexSlice[[0, 1], ['a']])._translate(True, True)
```

**Verification:**
```python
assert ctx['body'][0][1]['display_value'] == expected
```


## Complete Example

```python
# Workflow
df = DataFrame([[0.1234, 0.1234], [1.1234, 1.1234]], columns=['a', 'b'])
ctx = df.style.format({'a': '{:0.1f}', 'b': '{0:.2%}'}, subset=IndexSlice[0, :])._translate(True, True)
expected = '0.1'
raw_11 = '1.123400'
assert ctx['body'][0][1]['display_value'] == expected
assert ctx['body'][1][1]['display_value'] == raw_11
assert ctx['body'][0][2]['display_value'] == '12.34%'
ctx = df.style.format('{:0.1f}', subset=IndexSlice[0, :])._translate(True, True)
assert ctx['body'][0][1]['display_value'] == expected
assert ctx['body'][1][1]['display_value'] == raw_11
ctx = df.style.format('{:0.1f}', subset=IndexSlice['a'])._translate(True, True)
assert ctx['body'][0][1]['display_value'] == expected
assert ctx['body'][0][2]['display_value'] == '0.123400'
ctx = df.style.format('{:0.1f}', subset=IndexSlice[0, 'a'])._translate(True, True)
assert ctx['body'][0][1]['display_value'] == expected
assert ctx['body'][1][1]['display_value'] == raw_11
ctx = df.style.format('{:0.1f}', subset=IndexSlice[[0, 1], ['a']])._translate(True, True)
assert ctx['body'][0][1]['display_value'] == expected
assert ctx['body'][1][1]['display_value'] == '1.1'
assert ctx['body'][0][2]['display_value'] == '0.123400'
assert ctx['body'][1][2]['display_value'] == raw_11
```

## Next Steps


---

*Source: test_format.py:334 | Complexity: Advanced | Last updated: 2026-06-02*