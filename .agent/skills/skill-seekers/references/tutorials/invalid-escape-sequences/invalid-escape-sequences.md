# How To: Invalid Escape Sequences

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test invalid escape sequences

## Prerequisites

**Required Modules:**
- `sys`
- `unittest`
- `dirtyjson`
- `dirtyjson.compat`


## Step-by-Step Guide

### Step 1: Call self.assertRaises()

```python
self.assertRaises(dirtyjson.Error, dirtyjson.loads, '"\\u"')
```

### Step 2: Call self.assertRaises()

```python
self.assertRaises(dirtyjson.Error, dirtyjson.loads, '"\\u1"')
```

### Step 3: Call self.assertRaises()

```python
self.assertRaises(dirtyjson.Error, dirtyjson.loads, '"\\u12"')
```

### Step 4: Call self.assertRaises()

```python
self.assertRaises(dirtyjson.Error, dirtyjson.loads, '"\\u123"')
```

### Step 5: Call self.assertRaises()

```python
self.assertRaises(dirtyjson.Error, dirtyjson.loads, '"\\u123x"')
```

### Step 6: Call self.assertRaises()

```python
self.assertRaises(dirtyjson.Error, dirtyjson.loads, '"\\u12x4"')
```

### Step 7: Call self.assertRaises()

```python
self.assertRaises(dirtyjson.Error, dirtyjson.loads, '"\\u1x34"')
```

### Step 8: Call self.assertRaises()

```python
self.assertRaises(dirtyjson.Error, dirtyjson.loads, '"\\ux234"')
```

### Step 9: Call self.assertRaises()

```python
self.assertRaises(dirtyjson.Error, dirtyjson.loads, '"\\ud800\\u"')
```

### Step 10: Call self.assertRaises()

```python
self.assertRaises(dirtyjson.Error, dirtyjson.loads, '"\\ud800\\u0"')
```

### Step 11: Call self.assertRaises()

```python
self.assertRaises(dirtyjson.Error, dirtyjson.loads, '"\\ud800\\u00"')
```

### Step 12: Call self.assertRaises()

```python
self.assertRaises(dirtyjson.Error, dirtyjson.loads, '"\\ud800\\u000"')
```

### Step 13: Call self.assertRaises()

```python
self.assertRaises(dirtyjson.Error, dirtyjson.loads, '"\\ud800\\u000x"')
```

### Step 14: Call self.assertRaises()

```python
self.assertRaises(dirtyjson.Error, dirtyjson.loads, '"\\ud800\\u00x0"')
```

### Step 15: Call self.assertRaises()

```python
self.assertRaises(dirtyjson.Error, dirtyjson.loads, '"\\ud800\\u0x00"')
```

### Step 16: Call self.assertRaises()

```python
self.assertRaises(dirtyjson.Error, dirtyjson.loads, '"\\ud800\\ux000"')
```


## Complete Example

```python
# Workflow
self.assertRaises(dirtyjson.Error, dirtyjson.loads, '"\\u"')
self.assertRaises(dirtyjson.Error, dirtyjson.loads, '"\\u1"')
self.assertRaises(dirtyjson.Error, dirtyjson.loads, '"\\u12"')
self.assertRaises(dirtyjson.Error, dirtyjson.loads, '"\\u123"')
self.assertRaises(dirtyjson.Error, dirtyjson.loads, '"\\u123x"')
self.assertRaises(dirtyjson.Error, dirtyjson.loads, '"\\u12x4"')
self.assertRaises(dirtyjson.Error, dirtyjson.loads, '"\\u1x34"')
self.assertRaises(dirtyjson.Error, dirtyjson.loads, '"\\ux234"')
if sys.maxunicode > 65535:
    self.assertRaises(dirtyjson.Error, dirtyjson.loads, '"\\ud800\\u"')
    self.assertRaises(dirtyjson.Error, dirtyjson.loads, '"\\ud800\\u0"')
    self.assertRaises(dirtyjson.Error, dirtyjson.loads, '"\\ud800\\u00"')
    self.assertRaises(dirtyjson.Error, dirtyjson.loads, '"\\ud800\\u000"')
    self.assertRaises(dirtyjson.Error, dirtyjson.loads, '"\\ud800\\u000x"')
    self.assertRaises(dirtyjson.Error, dirtyjson.loads, '"\\ud800\\u00x0"')
    self.assertRaises(dirtyjson.Error, dirtyjson.loads, '"\\ud800\\u0x00"')
    self.assertRaises(dirtyjson.Error, dirtyjson.loads, '"\\ud800\\ux000"')
```

## Next Steps


---

*Source: test_unicode.py:29 | Complexity: Advanced | Last updated: 2026-06-02*