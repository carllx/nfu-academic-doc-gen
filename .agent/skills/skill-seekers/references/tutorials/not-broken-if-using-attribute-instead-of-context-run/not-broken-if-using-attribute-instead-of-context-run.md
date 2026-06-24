# How To: Not Broken If Using Attribute Instead Of Context Run

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test not broken if using attribute instead of context run

## Prerequisites

**Required Modules:**
- `__future__`
- `gc`
- `sys`
- `unittest`
- `functools`
- `unittest`
- `unittest`
- `greenlet`
- `greenlet`
- `contextvars`
- `contextvars`
- `contextvars`
- `threading`


## Step-by-Step Guide

### Step 1: Assign let1 = greenlet(...)

```python
let1 = greenlet(getcurrent().switch)
```

### Step 2: Assign let2 = greenlet(...)

```python
let2 = greenlet(getcurrent().switch)
```

### Step 3: Assign let1.gr_context = copy_context(...)

```python
let1.gr_context = copy_context()
```

### Step 4: Assign let2.gr_context = copy_context(...)

```python
let2.gr_context = copy_context()
```

### Step 5: Call let1.switch()

```python
let1.switch()
```

### Step 6: Call let2.switch()

```python
let2.switch()
```

### Step 7: Call let1.switch()

```python
let1.switch()
```

### Step 8: Call let2.switch()

```python
let2.switch()
```


## Complete Example

```python
# Workflow
let1 = greenlet(getcurrent().switch)
let2 = greenlet(getcurrent().switch)
let1.gr_context = copy_context()
let2.gr_context = copy_context()
let1.switch()
let2.switch()
let1.switch()
let2.switch()
```

## Next Steps


---

*Source: test_contextvars.py:132 | Complexity: Advanced | Last updated: 2026-06-02*