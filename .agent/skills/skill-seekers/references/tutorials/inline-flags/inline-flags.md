# How To: Inline Flags

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test inline flags

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

### Step 1: Assign upper_char = chr(...)

```python
upper_char = chr(7840)
```

### Step 2: Assign lower_char = chr(...)

```python
lower_char = chr(7841)
```

### Step 3: Assign p = regex.compile(...)

```python
p = regex.compile(upper_char, regex.I | regex.U)
```

### Step 4: Call self.assertEqual()

```python
self.assertEqual(bool(p.match(lower_char)), True)
```

### Step 5: Assign p = regex.compile(...)

```python
p = regex.compile(lower_char, regex.I | regex.U)
```

### Step 6: Call self.assertEqual()

```python
self.assertEqual(bool(p.match(upper_char)), True)
```

### Step 7: Assign p = regex.compile(...)

```python
p = regex.compile('(?i)' + upper_char, regex.U)
```

### Step 8: Call self.assertEqual()

```python
self.assertEqual(bool(p.match(lower_char)), True)
```

### Step 9: Assign p = regex.compile(...)

```python
p = regex.compile('(?i)' + lower_char, regex.U)
```

### Step 10: Call self.assertEqual()

```python
self.assertEqual(bool(p.match(upper_char)), True)
```

### Step 11: Assign p = regex.compile(...)

```python
p = regex.compile('(?iu)' + upper_char)
```

### Step 12: Call self.assertEqual()

```python
self.assertEqual(bool(p.match(lower_char)), True)
```

### Step 13: Assign p = regex.compile(...)

```python
p = regex.compile('(?iu)' + lower_char)
```

### Step 14: Call self.assertEqual()

```python
self.assertEqual(bool(p.match(upper_char)), True)
```

### Step 15: Call self.assertEqual()

```python
self.assertEqual(bool(regex.match('(?i)a', 'A')), True)
```

### Step 16: Call self.assertEqual()

```python
self.assertEqual(regex.match('a(?i)', 'A'), None)
```


## Complete Example

```python
# Workflow
upper_char = chr(7840)
lower_char = chr(7841)
p = regex.compile(upper_char, regex.I | regex.U)
self.assertEqual(bool(p.match(lower_char)), True)
p = regex.compile(lower_char, regex.I | regex.U)
self.assertEqual(bool(p.match(upper_char)), True)
p = regex.compile('(?i)' + upper_char, regex.U)
self.assertEqual(bool(p.match(lower_char)), True)
p = regex.compile('(?i)' + lower_char, regex.U)
self.assertEqual(bool(p.match(upper_char)), True)
p = regex.compile('(?iu)' + upper_char)
self.assertEqual(bool(p.match(lower_char)), True)
p = regex.compile('(?iu)' + lower_char)
self.assertEqual(bool(p.match(upper_char)), True)
self.assertEqual(bool(regex.match('(?i)a', 'A')), True)
self.assertEqual(regex.match('a(?i)', 'A'), None)
```

## Next Steps


---

*Source: test_regex.py:891 | Complexity: Advanced | Last updated: 2026-06-02*