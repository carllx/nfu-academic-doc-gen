# How To: Format Options

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test format options

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
df = DataFrame({'int': [2000, 1], 'float': [1.009, None], 'str': ['&<', '&~']})
```

**Verification:**
```python
assert ctx['body'][1][2]['display_value'] == 'nan'
```

### Step 2: Assign ctx = df.style._translate(...)

```python
ctx = df.style._translate(True, True)
```

**Verification:**
```python
assert ctx_with_op['body'][1][2]['display_value'] == 'MISSING'
```

### Step 3: Assign ctx_with_op = df.style._translate(...)

```python
ctx_with_op = df.style._translate(True, True)
```

**Verification:**
```python
assert ctx['body'][0][2]['display_value'] == '1.009000'
```

### Step 4: Assign ctx_with_op = df.style._translate(...)

```python
ctx_with_op = df.style._translate(True, True)
```

**Verification:**
```python
assert ctx_with_op['body'][0][2]['display_value'] == '1_009000'
```

### Step 5: Assign ctx_with_op = df.style._translate(...)

```python
ctx_with_op = df.style._translate(True, True)
```

**Verification:**
```python
assert ctx_with_op['body'][0][2]['display_value'] == '1.01'
```

### Step 6: Assign ctx_with_op = df.style._translate(...)

```python
ctx_with_op = df.style._translate(True, True)
```

**Verification:**
```python
assert ctx['body'][0][1]['display_value'] == '2000'
```

### Step 7: Assign ctx_with_op = df.style._translate(...)

```python
ctx_with_op = df.style._translate(True, True)
```

**Verification:**
```python
assert ctx_with_op['body'][0][1]['display_value'] == '2_000'
```

### Step 8: Assign ctx_with_op = df.style._translate(...)

```python
ctx_with_op = df.style._translate(True, True)
```

**Verification:**
```python
assert ctx['body'][0][3]['display_value'] == '&<'
```

### Step 9: Assign ctx_with_op = df.style._translate(...)

```python
ctx_with_op = df.style._translate(True, True)
```

**Verification:**
```python
assert ctx['body'][1][3]['display_value'] == '&~'
```

### Step 10: Assign ctx_with_op = df.style._translate(...)

```python
ctx_with_op = df.style._translate(True, True)
```

**Verification:**
```python
assert ctx_with_op['body'][0][3]['display_value'] == '&amp;&lt;'
```


## Complete Example

```python
# Workflow
df = DataFrame({'int': [2000, 1], 'float': [1.009, None], 'str': ['&<', '&~']})
ctx = df.style._translate(True, True)
assert ctx['body'][1][2]['display_value'] == 'nan'
with option_context('styler.format.na_rep', 'MISSING'):
    ctx_with_op = df.style._translate(True, True)
    assert ctx_with_op['body'][1][2]['display_value'] == 'MISSING'
assert ctx['body'][0][2]['display_value'] == '1.009000'
with option_context('styler.format.decimal', '_'):
    ctx_with_op = df.style._translate(True, True)
    assert ctx_with_op['body'][0][2]['display_value'] == '1_009000'
with option_context('styler.format.precision', 2):
    ctx_with_op = df.style._translate(True, True)
    assert ctx_with_op['body'][0][2]['display_value'] == '1.01'
assert ctx['body'][0][1]['display_value'] == '2000'
with option_context('styler.format.thousands', '_'):
    ctx_with_op = df.style._translate(True, True)
    assert ctx_with_op['body'][0][1]['display_value'] == '2_000'
assert ctx['body'][0][3]['display_value'] == '&<'
assert ctx['body'][1][3]['display_value'] == '&~'
with option_context('styler.format.escape', 'html'):
    ctx_with_op = df.style._translate(True, True)
    assert ctx_with_op['body'][0][3]['display_value'] == '&amp;&lt;'
with option_context('styler.format.escape', 'latex'):
    ctx_with_op = df.style._translate(True, True)
    assert ctx_with_op['body'][1][3]['display_value'] == '\\&\\textasciitilde '
with option_context('styler.format.escape', 'latex-math'):
    ctx_with_op = df.style._translate(True, True)
    assert ctx_with_op['body'][1][3]['display_value'] == '\\&\\textasciitilde '
with option_context('styler.format.formatter', {'int': '{:,.2f}'}):
    ctx_with_op = df.style._translate(True, True)
    assert ctx_with_op['body'][0][1]['display_value'] == '2,000.00'
```

## Next Steps


---

*Source: test_format.py:430 | Complexity: Advanced | Last updated: 2026-06-02*