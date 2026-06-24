# How To: Long Int Formatting

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test long int formatting

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
df = DataFrame(data=[[1234567890123456789]], columns=['test'])
```

**Verification:**
```python
assert ctx['body'][0][1]['display_value'] == '1234567890123456789'
```

### Step 2: Assign styler = value

```python
styler = df.style
```

**Verification:**
```python
assert ctx['body'][0][1]['display_value'] == '1_234_567_890_123_456_789'
```

### Step 3: Assign ctx = styler._translate(...)

```python
ctx = styler._translate(True, True)
```

**Verification:**
```python
assert ctx['body'][0][1]['display_value'] == '1234567890123456789'
```

### Step 4: Assign styler = df.style.format(...)

```python
styler = df.style.format(thousands='_')
```

### Step 5: Assign ctx = styler._translate(...)

```python
ctx = styler._translate(True, True)
```

**Verification:**
```python
assert ctx['body'][0][1]['display_value'] == '1_234_567_890_123_456_789'
```


## Complete Example

```python
# Workflow
df = DataFrame(data=[[1234567890123456789]], columns=['test'])
styler = df.style
ctx = styler._translate(True, True)
assert ctx['body'][0][1]['display_value'] == '1234567890123456789'
styler = df.style.format(thousands='_')
ctx = styler._translate(True, True)
assert ctx['body'][0][1]['display_value'] == '1_234_567_890_123_456_789'
```

## Next Steps


---

*Source: test_format.py:419 | Complexity: Intermediate | Last updated: 2026-06-02*