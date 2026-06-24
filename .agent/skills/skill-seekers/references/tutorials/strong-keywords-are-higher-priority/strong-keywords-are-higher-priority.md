# How To: Strong Keywords Are Higher Priority

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test strong keywords are higher priority

## Prerequisites

**Required Modules:**
- `unittest`
- `textwrap`
- `jsonpath_ng`
- `jsonschema`
- `jsonschema.validators`


## Step-by-Step Guide

### Step 1: Assign weak = exceptions.ValidationError(...)

```python
weak = exceptions.ValidationError('Oh no!', path=[], validator='a')
```

### Step 2: Assign normal = exceptions.ValidationError(...)

```python
normal = exceptions.ValidationError('Oh yes!', path=[], validator='b')
```

### Step 3: Assign strong = exceptions.ValidationError(...)

```python
strong = exceptions.ValidationError('Oh fine!', path=[], validator='c')
```

### Step 4: Assign best_match = exceptions.by_relevance(...)

```python
best_match = exceptions.by_relevance(weak='a', strong='c')
```

### Step 5: Assign match = max(...)

```python
match = max([weak, normal, strong], key=best_match)
```

### Step 6: Call self.assertIs()

```python
self.assertIs(match, strong)
```

### Step 7: Assign match = max(...)

```python
match = max([strong, normal, weak], key=best_match)
```

### Step 8: Call self.assertIs()

```python
self.assertIs(match, strong)
```


## Complete Example

```python
# Workflow
weak = exceptions.ValidationError('Oh no!', path=[], validator='a')
normal = exceptions.ValidationError('Oh yes!', path=[], validator='b')
strong = exceptions.ValidationError('Oh fine!', path=[], validator='c')
best_match = exceptions.by_relevance(weak='a', strong='c')
match = max([weak, normal, strong], key=best_match)
self.assertIs(match, strong)
match = max([strong, normal, weak], key=best_match)
self.assertIs(match, strong)
```

## Next Steps


---

*Source: test_exceptions.py:373 | Complexity: Advanced | Last updated: 2026-06-02*