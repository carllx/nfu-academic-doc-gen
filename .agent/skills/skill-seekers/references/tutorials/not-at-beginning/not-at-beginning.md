# How To: Not At Beginning

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test not at beginning

## Prerequisites

**Required Modules:**
- `__future__`
- `decimal`
- `unittest`
- `dirtyjson`


## Step-by-Step Guide

### Step 1: Assign s = '\n// here are some comments\nvar a = 1; // here is a line of regular JS\n\nvar b = {test: 1, \'aack\': 0x80, "bar": [1, 2, 3]};\nconsole.log(b);\n'

```python
s = '\n// here are some comments\nvar a = 1; // here is a line of regular JS\n\nvar b = {test: 1, \'aack\': 0x80, "bar": [1, 2, 3]};\nconsole.log(b);\n'
```

### Step 2: Assign first_object_index = s.index(...)

```python
first_object_index = s.index('{')
```

### Step 3: Assign rval = dirtyjson.loads(...)

```python
rval = dirtyjson.loads(s, start_index=first_object_index)
```

### Step 4: Call self.assertEqual()

```python
self.assertEqual(rval, {'test': 1, 'aack': 128, 'bar': [1, 2, 3]})
```

### Step 5: Assign rval = dirtyjson.loads(...)

```python
rval = dirtyjson.loads(s, start_index=first_object_index + 1, search_for_first_object=True)
```

### Step 6: Call self.assertEqual()

```python
self.assertEqual(rval, [1, 2, 3])
```

### Step 7: Assign rval = dirtyjson.loads(...)

```python
rval = dirtyjson.loads(s, search_for_first_object=True)
```

### Step 8: Call self.assertEqual()

```python
self.assertEqual(rval, {'test': 1, 'aack': 128, 'bar': [1, 2, 3]})
```


## Complete Example

```python
# Workflow
s = '\n// here are some comments\nvar a = 1; // here is a line of regular JS\n\nvar b = {test: 1, \'aack\': 0x80, "bar": [1, 2, 3]};\nconsole.log(b);\n'
first_object_index = s.index('{')
rval = dirtyjson.loads(s, start_index=first_object_index)
self.assertEqual(rval, {'test': 1, 'aack': 128, 'bar': [1, 2, 3]})
rval = dirtyjson.loads(s, start_index=first_object_index + 1, search_for_first_object=True)
self.assertEqual(rval, [1, 2, 3])
rval = dirtyjson.loads(s, search_for_first_object=True)
self.assertEqual(rval, {'test': 1, 'aack': 128, 'bar': [1, 2, 3]})
```

## Next Steps


---

*Source: test_decode.py:72 | Complexity: Advanced | Last updated: 2026-06-02*