# How To: Ambiguous Width

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test ambiguous width

## Prerequisites

**Required Modules:**
- `string`
- `pandas._config.config`
- `pandas.io.formats`


## Step-by-Step Guide

### Step 1: Assign adj = printing._EastAsianTextAdjustment(...)

```python
adj = printing._EastAsianTextAdjustment()
```

**Verification:**
```python
assert adj.len('¡¡ab') == 4
```

### Step 2: Assign data = value

```python
data = [['あ', 'b', 'c'], ['dd', 'ええ', 'ff'], ['ggg', '¡¡ab', 'いいい']]
```

**Verification:**
```python
assert adj.len('¡¡ab') == 6
```

### Step 3: Assign expected = 'あ  dd    ggg \nb   ええ  ¡¡ab\nc   ff    いいい'

```python
expected = 'あ  dd    ggg \nb   ええ  ¡¡ab\nc   ff    いいい'
```

**Verification:**
```python
assert adjoined == expected
```

### Step 4: Assign adjoined = adj.adjoin(...)

```python
adjoined = adj.adjoin(2, *data)
```

**Verification:**
```python
assert adjoined == expected
```

### Step 5: Assign adj = printing._EastAsianTextAdjustment(...)

```python
adj = printing._EastAsianTextAdjustment()
```

**Verification:**
```python
assert adj.len('¡¡ab') == 6
```


## Complete Example

```python
# Workflow
adj = printing._EastAsianTextAdjustment()
assert adj.len('¡¡ab') == 4
with cf.option_context('display.unicode.ambiguous_as_wide', True):
    adj = printing._EastAsianTextAdjustment()
    assert adj.len('¡¡ab') == 6
data = [['あ', 'b', 'c'], ['dd', 'ええ', 'ff'], ['ggg', '¡¡ab', 'いいい']]
expected = 'あ  dd    ggg \nb   ええ  ¡¡ab\nc   ff    いいい'
adjoined = adj.adjoin(2, *data)
assert adjoined == expected
```

## Next Steps


---

*Source: test_printing.py:118 | Complexity: Intermediate | Last updated: 2026-06-02*