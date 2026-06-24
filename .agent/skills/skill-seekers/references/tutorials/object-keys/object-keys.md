# How To: Object Keys

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test object keys

## Prerequisites

**Required Modules:**
- `__future__`
- `decimal`
- `unittest`
- `dirtyjson`


## Step-by-Step Guide

### Step 1: Assign result = value

```python
result = {'key': 'value', 'k': 'v'}
```

### Step 2: Assign rval = dirtyjson.loads(...)

```python
rval = dirtyjson.loads('{"key": "value", "k": "v"}')
```

### Step 3: Call self.assertEqual()

```python
self.assertEqual(rval, result)
```

### Step 4: Assign rval = dirtyjson.loads(...)

```python
rval = dirtyjson.loads("{'key': 'value', 'k': 'v'}")
```

### Step 5: Call self.assertEqual()

```python
self.assertEqual(rval, result)
```

### Step 6: Assign rval = dirtyjson.loads(...)

```python
rval = dirtyjson.loads("{key: 'value', k: 'v'}")
```

### Step 7: Call self.assertEqual()

```python
self.assertEqual(rval, result)
```

### Step 8: Assign rval = dirtyjson.loads(...)

```python
rval = dirtyjson.loads("{key: 'value', k: 'v',}")
```

### Step 9: Call self.assertEqual()

```python
self.assertEqual(rval, result)
```


## Complete Example

```python
# Workflow
result = {'key': 'value', 'k': 'v'}
rval = dirtyjson.loads('{"key": "value", "k": "v"}')
self.assertEqual(rval, result)
rval = dirtyjson.loads("{'key': 'value', 'k': 'v'}")
self.assertEqual(rval, result)
rval = dirtyjson.loads("{key: 'value', k: 'v'}")
self.assertEqual(rval, result)
rval = dirtyjson.loads("{key: 'value', k: 'v',}")
self.assertEqual(rval, result)
```

## Next Steps


---

*Source: test_decode.py:61 | Complexity: Advanced | Last updated: 2026-06-02*