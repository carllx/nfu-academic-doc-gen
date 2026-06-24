# How To: Guards

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test guards

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

### Step 1: Assign m = regex.search(...)

```python
m = regex.search('(X.*?Y\\s*){3}(X\\s*)+AB:', 'XY\nX Y\nX  Y\nXY\nXX AB:')
```

### Step 2: Call self.assertEqual()

```python
self.assertEqual(m.span(0, 1, 2), ((3, 21), (12, 15), (16, 18)))
```

### Step 3: Assign m = regex.search(...)

```python
m = regex.search('(X.*?Y\\s*){3,}(X\\s*)+AB:', 'XY\nX Y\nX  Y\nXY\nXX AB:')
```

### Step 4: Call self.assertEqual()

```python
self.assertEqual(m.span(0, 1, 2), ((0, 21), (12, 15), (16, 18)))
```

### Step 5: Assign m = regex.search(...)

```python
m = regex.search('\\d{4}(\\s*\\w)?\\W*((?!\\d)\\w){2}', '9999XX')
```

### Step 6: Call self.assertEqual()

```python
self.assertEqual(m.span(0, 1, 2), ((0, 6), (-1, -1), (5, 6)))
```

### Step 7: Assign m = regex.search(...)

```python
m = regex.search('A\\s*?.*?(\\n+.*?\\s*?){0,2}\\(X', 'A\n1\nS\n1 (X')
```

### Step 8: Call self.assertEqual()

```python
self.assertEqual(m.span(0, 1), ((0, 10), (5, 8)))
```

### Step 9: Assign m = regex.search(...)

```python
m = regex.search('Derde\\s*:', 'aaaaaa:\nDerde:')
```

### Step 10: Call self.assertEqual()

```python
self.assertEqual(m.span(), (8, 14))
```

### Step 11: Assign m = regex.search(...)

```python
m = regex.search('Derde\\s*:', 'aaaaa:\nDerde:')
```

### Step 12: Call self.assertEqual()

```python
self.assertEqual(m.span(), (7, 13))
```


## Complete Example

```python
# Workflow
m = regex.search('(X.*?Y\\s*){3}(X\\s*)+AB:', 'XY\nX Y\nX  Y\nXY\nXX AB:')
self.assertEqual(m.span(0, 1, 2), ((3, 21), (12, 15), (16, 18)))
m = regex.search('(X.*?Y\\s*){3,}(X\\s*)+AB:', 'XY\nX Y\nX  Y\nXY\nXX AB:')
self.assertEqual(m.span(0, 1, 2), ((0, 21), (12, 15), (16, 18)))
m = regex.search('\\d{4}(\\s*\\w)?\\W*((?!\\d)\\w){2}', '9999XX')
self.assertEqual(m.span(0, 1, 2), ((0, 6), (-1, -1), (5, 6)))
m = regex.search('A\\s*?.*?(\\n+.*?\\s*?){0,2}\\(X', 'A\n1\nS\n1 (X')
self.assertEqual(m.span(0, 1), ((0, 10), (5, 8)))
m = regex.search('Derde\\s*:', 'aaaaaa:\nDerde:')
self.assertEqual(m.span(), (8, 14))
m = regex.search('Derde\\s*:', 'aaaaa:\nDerde:')
self.assertEqual(m.span(), (7, 13))
```

## Next Steps


---

*Source: test_regex.py:2512 | Complexity: Advanced | Last updated: 2026-06-02*