# How To: Aline

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test aline

## Prerequisites

**Required Modules:**
- `nltk.metrics`


## Step-by-Step Guide

### Step 1: Assign result = aline.align(...)

```python
result = aline.align('θin', 'tenwis')
```

**Verification:**
```python
assert result == expected
```

### Step 2: Assign expected = value

```python
expected = [[('θ', 't'), ('i', 'e'), ('n', 'n')]]
```

**Verification:**
```python
assert result == expected
```

### Step 3: Assign result = aline.align(...)

```python
result = aline.align('jo', 'ʒə')
```

**Verification:**
```python
assert result == expected
```

### Step 4: Assign expected = value

```python
expected = [[('j', 'ʒ'), ('o', 'ə')]]
```

**Verification:**
```python
assert result == expected
```

### Step 5: Assign result = aline.align(...)

```python
result = aline.align('pematesiweni', 'pematesewen')
```

### Step 6: Assign expected = value

```python
expected = [[('p', 'p'), ('e', 'e'), ('m', 'm'), ('a', 'a'), ('t', 't'), ('e', 'e'), ('s', 's'), ('i', 'e'), ('w', 'w'), ('e', 'e'), ('n', 'n')]]
```

**Verification:**
```python
assert result == expected
```

### Step 7: Assign result = aline.align(...)

```python
result = aline.align('tuwθ', 'dentis')
```

### Step 8: Assign expected = value

```python
expected = [[('t', 't'), ('u', 'i'), ('w', '-'), ('θ', 's')]]
```

**Verification:**
```python
assert result == expected
```


## Complete Example

```python
# Workflow
result = aline.align('θin', 'tenwis')
expected = [[('θ', 't'), ('i', 'e'), ('n', 'n')]]
assert result == expected
result = aline.align('jo', 'ʒə')
expected = [[('j', 'ʒ'), ('o', 'ə')]]
assert result == expected
result = aline.align('pematesiweni', 'pematesewen')
expected = [[('p', 'p'), ('e', 'e'), ('m', 'm'), ('a', 'a'), ('t', 't'), ('e', 'e'), ('s', 's'), ('i', 'e'), ('w', 'w'), ('e', 'e'), ('n', 'n')]]
assert result == expected
result = aline.align('tuwθ', 'dentis')
expected = [[('t', 't'), ('u', 'i'), ('w', '-'), ('θ', 's')]]
assert result == expected
```

## Next Steps


---

*Source: test_aline.py:8 | Complexity: Advanced | Last updated: 2026-06-02*