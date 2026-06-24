# How To: Ascii And Unicode Flag

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test ascii and unicode flag

## Prerequisites

**Required Modules:**
- `weakref`
- `copy`
- `pickle`
- `regex`
- `string`
- `sys`
- `unittest`
- `array`


## Step-by-Step Guide

### Step 1: Assign pat = regex.compile(...)

```python
pat = regex.compile('À', regex.ASCII | regex.IGNORECASE)
```

### Step 2: Call self.assertEqual()

```python
self.assertEqual(pat.match('à'), None)
```

### Step 3: Assign pat = regex.compile(...)

```python
pat = regex.compile('(?a)À', regex.IGNORECASE)
```

### Step 4: Call self.assertEqual()

```python
self.assertEqual(pat.match('à'), None)
```

### Step 5: Assign pat = regex.compile(...)

```python
pat = regex.compile('\\w', regex.ASCII)
```

### Step 6: Call self.assertEqual()

```python
self.assertEqual(pat.match('à'), None)
```

### Step 7: Assign pat = regex.compile(...)

```python
pat = regex.compile('(?a)\\w')
```

### Step 8: Call self.assertEqual()

```python
self.assertEqual(pat.match('à'), None)
```

### Step 9: Call self.assertRaisesRegex()

```python
self.assertRaisesRegex(ValueError, self.MIXED_FLAGS, lambda: regex.compile('(?au)\\w'))
```

### Step 10: Assign pat = regex.compile(...)

```python
pat = regex.compile('À', flags | regex.IGNORECASE)
```

### Step 11: Call self.assertEqual()

```python
self.assertEqual(bool(pat.match('à')), True)
```

### Step 12: Assign pat = regex.compile(...)

```python
pat = regex.compile('\\w', flags)
```

### Step 13: Call self.assertEqual()

```python
self.assertEqual(bool(pat.match('à')), True)
```

### Step 14: Assign pat = regex.compile(...)

```python
pat = regex.compile(b'\xc0', flags | regex.IGNORECASE)
```

### Step 15: Call self.assertEqual()

```python
self.assertEqual(pat.match(b'\xe0'), None)
```

### Step 16: Assign pat = regex.compile(...)

```python
pat = regex.compile(b'\\w')
```

### Step 17: Call self.assertEqual()

```python
self.assertEqual(pat.match(b'\xe0'), None)
```


## Complete Example

```python
# Workflow
for flags in (0, regex.UNICODE):
    pat = regex.compile('À', flags | regex.IGNORECASE)
    self.assertEqual(bool(pat.match('à')), True)
    pat = regex.compile('\\w', flags)
    self.assertEqual(bool(pat.match('à')), True)
pat = regex.compile('À', regex.ASCII | regex.IGNORECASE)
self.assertEqual(pat.match('à'), None)
pat = regex.compile('(?a)À', regex.IGNORECASE)
self.assertEqual(pat.match('à'), None)
pat = regex.compile('\\w', regex.ASCII)
self.assertEqual(pat.match('à'), None)
pat = regex.compile('(?a)\\w')
self.assertEqual(pat.match('à'), None)
for flags in (0, regex.ASCII):
    pat = regex.compile(b'\xc0', flags | regex.IGNORECASE)
    self.assertEqual(pat.match(b'\xe0'), None)
    pat = regex.compile(b'\\w')
    self.assertEqual(pat.match(b'\xe0'), None)
self.assertRaisesRegex(ValueError, self.MIXED_FLAGS, lambda: regex.compile('(?au)\\w'))
```

## Next Steps


---

*Source: test_regex.py:964 | Complexity: Advanced | Last updated: 2026-06-02*