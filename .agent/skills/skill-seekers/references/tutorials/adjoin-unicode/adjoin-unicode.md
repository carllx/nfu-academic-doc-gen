# How To: Adjoin Unicode

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test adjoin unicode

## Prerequisites

**Required Modules:**
- `string`
- `pandas._config.config`
- `pandas.io.formats`


## Step-by-Step Guide

### Step 1: Assign data = value

```python
data = [['あ', 'b', 'c'], ['dd', 'ええ', 'ff'], ['ggg', 'hhh', 'いいい']]
```

**Verification:**
```python
assert adjoined == expected
```

### Step 2: Assign expected = 'あ  dd  ggg\nb  ええ  hhh\nc  ff  いいい'

```python
expected = 'あ  dd  ggg\nb  ええ  hhh\nc  ff  いいい'
```

**Verification:**
```python
assert adjoined == expected
```

### Step 3: Assign adjoined = printing.adjoin(...)

```python
adjoined = printing.adjoin(2, *data)
```

**Verification:**
```python
assert adj.len(cols[0]) == 13
```

### Step 4: Assign adj = printing._EastAsianTextAdjustment(...)

```python
adj = printing._EastAsianTextAdjustment()
```

**Verification:**
```python
assert adj.len(cols[1]) == 13
```

### Step 5: Assign expected = 'あ  dd    ggg\nb   ええ  hhh\nc   ff    いいい'

```python
expected = 'あ  dd    ggg\nb   ええ  hhh\nc   ff    いいい'
```

**Verification:**
```python
assert adj.len(cols[2]) == 16
```

### Step 6: Assign adjoined = adj.adjoin(...)

```python
adjoined = adj.adjoin(2, *data)
```

**Verification:**
```python
assert adjoined == expected
```

### Step 7: Assign cols = adjoined.split(...)

```python
cols = adjoined.split('\n')
```

**Verification:**
```python
assert adj.len(cols[0]) == 23
```

### Step 8: Assign expected = 'あ       dd         ggg\nb        ええ       hhh\nc        ff         いいい'

```python
expected = 'あ       dd         ggg\nb        ええ       hhh\nc        ff         いいい'
```

**Verification:**
```python
assert adj.len(cols[1]) == 23
```

### Step 9: Assign adjoined = adj.adjoin(...)

```python
adjoined = adj.adjoin(7, *data)
```

**Verification:**
```python
assert adj.len(cols[2]) == 26
```

### Step 10: Assign cols = adjoined.split(...)

```python
cols = adjoined.split('\n')
```

**Verification:**
```python
assert adj.len(cols[0]) == 23
```


## Complete Example

```python
# Workflow
data = [['あ', 'b', 'c'], ['dd', 'ええ', 'ff'], ['ggg', 'hhh', 'いいい']]
expected = 'あ  dd  ggg\nb  ええ  hhh\nc  ff  いいい'
adjoined = printing.adjoin(2, *data)
assert adjoined == expected
adj = printing._EastAsianTextAdjustment()
expected = 'あ  dd    ggg\nb   ええ  hhh\nc   ff    いいい'
adjoined = adj.adjoin(2, *data)
assert adjoined == expected
cols = adjoined.split('\n')
assert adj.len(cols[0]) == 13
assert adj.len(cols[1]) == 13
assert adj.len(cols[2]) == 16
expected = 'あ       dd         ggg\nb        ええ       hhh\nc        ff         いいい'
adjoined = adj.adjoin(7, *data)
assert adjoined == expected
cols = adjoined.split('\n')
assert adj.len(cols[0]) == 23
assert adj.len(cols[1]) == 23
assert adj.len(cols[2]) == 26
```

## Next Steps


---

*Source: test_printing.py:55 | Complexity: Advanced | Last updated: 2026-06-02*