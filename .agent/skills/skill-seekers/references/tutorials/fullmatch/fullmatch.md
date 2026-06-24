# How To: Fullmatch

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test fullmatch

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

### Step 1: Call self.assertEqual()

```python
self.assertEqual(bool(regex.fullmatch('abc', 'abc')), True)
```

### Step 2: Call self.assertEqual()

```python
self.assertEqual(bool(regex.fullmatch('abc', 'abcx')), False)
```

### Step 3: Call self.assertEqual()

```python
self.assertEqual(bool(regex.fullmatch('abc', 'abcx', endpos=3)), True)
```

### Step 4: Call self.assertEqual()

```python
self.assertEqual(bool(regex.fullmatch('abc', 'xabc', pos=1)), True)
```

### Step 5: Call self.assertEqual()

```python
self.assertEqual(bool(regex.fullmatch('abc', 'xabcy', pos=1)), False)
```

### Step 6: Call self.assertEqual()

```python
self.assertEqual(bool(regex.fullmatch('abc', 'xabcy', pos=1, endpos=4)), True)
```

### Step 7: Call self.assertEqual()

```python
self.assertEqual(bool(regex.fullmatch('(?r)abc', 'abc')), True)
```

### Step 8: Call self.assertEqual()

```python
self.assertEqual(bool(regex.fullmatch('(?r)abc', 'abcx')), False)
```

### Step 9: Call self.assertEqual()

```python
self.assertEqual(bool(regex.fullmatch('(?r)abc', 'abcx', endpos=3)), True)
```

### Step 10: Call self.assertEqual()

```python
self.assertEqual(bool(regex.fullmatch('(?r)abc', 'xabc', pos=1)), True)
```

### Step 11: Call self.assertEqual()

```python
self.assertEqual(bool(regex.fullmatch('(?r)abc', 'xabcy', pos=1)), False)
```

### Step 12: Call self.assertEqual()

```python
self.assertEqual(bool(regex.fullmatch('(?r)abc', 'xabcy', pos=1, endpos=4)), True)
```


## Complete Example

```python
# Workflow
self.assertEqual(bool(regex.fullmatch('abc', 'abc')), True)
self.assertEqual(bool(regex.fullmatch('abc', 'abcx')), False)
self.assertEqual(bool(regex.fullmatch('abc', 'abcx', endpos=3)), True)
self.assertEqual(bool(regex.fullmatch('abc', 'xabc', pos=1)), True)
self.assertEqual(bool(regex.fullmatch('abc', 'xabcy', pos=1)), False)
self.assertEqual(bool(regex.fullmatch('abc', 'xabcy', pos=1, endpos=4)), True)
self.assertEqual(bool(regex.fullmatch('(?r)abc', 'abc')), True)
self.assertEqual(bool(regex.fullmatch('(?r)abc', 'abcx')), False)
self.assertEqual(bool(regex.fullmatch('(?r)abc', 'abcx', endpos=3)), True)
self.assertEqual(bool(regex.fullmatch('(?r)abc', 'xabc', pos=1)), True)
self.assertEqual(bool(regex.fullmatch('(?r)abc', 'xabcy', pos=1)), False)
self.assertEqual(bool(regex.fullmatch('(?r)abc', 'xabcy', pos=1, endpos=4)), True)
```

## Next Steps


---

*Source: test_regex.py:2933 | Complexity: Advanced | Last updated: 2026-06-02*