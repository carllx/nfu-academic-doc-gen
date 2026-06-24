# How To: Weak Keywords Are Lower Priority

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test weak keywords are lower priority

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

### Step 3: Assign best_match = exceptions.by_relevance(...)

```python
best_match = exceptions.by_relevance(weak='a')
```

### Step 4: Assign match = max(...)

```python
match = max([weak, normal], key=best_match)
```

### Step 5: Call self.assertIs()

```python
self.assertIs(match, normal)
```

### Step 6: Assign match = max(...)

```python
match = max([normal, weak], key=best_match)
```

### Step 7: Call self.assertIs()

```python
self.assertIs(match, normal)
```


## Complete Example

```python
# Workflow
weak = exceptions.ValidationError('Oh no!', path=[], validator='a')
normal = exceptions.ValidationError('Oh yes!', path=[], validator='b')
best_match = exceptions.by_relevance(weak='a')
match = max([weak, normal], key=best_match)
self.assertIs(match, normal)
match = max([normal, weak], key=best_match)
self.assertIs(match, normal)
```

## Next Steps


---

*Source: test_exceptions.py:361 | Complexity: Advanced | Last updated: 2026-06-02*