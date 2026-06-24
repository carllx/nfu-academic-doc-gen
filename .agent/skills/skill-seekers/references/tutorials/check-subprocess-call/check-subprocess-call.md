# How To: Check Subprocess Call

**Difficulty**: Beginner
**Estimated Time**: 5 minutes
**Tags**: workflow, integration

## Overview

Workflow: test check subprocess call

## Prerequisites

**Required Modules:**
- `re`
- `sys`
- `joblib.testing`


## Step-by-Step Guide

### Step 1: Assign code = unknown.join(...)

```python
code = '\n'.join(['result = 1 + 2 * 3', 'print(result)', 'my_list = [1, 2, 3]', 'print(my_list)'])
```

### Step 2: Call check_subprocess_call()

```python
check_subprocess_call([sys.executable, '-c', code])
```

### Step 3: Call check_subprocess_call()

```python
check_subprocess_call([sys.executable, '-c', code], stdout_regex='7\\s{1,2}\\[1, 2, 3\\]')
```


## Complete Example

```python
# Workflow
code = '\n'.join(['result = 1 + 2 * 3', 'print(result)', 'my_list = [1, 2, 3]', 'print(my_list)'])
check_subprocess_call([sys.executable, '-c', code])
check_subprocess_call([sys.executable, '-c', code], stdout_regex='7\\s{1,2}\\[1, 2, 3\\]')
```

## Next Steps


---

*Source: test_testing.py:7 | Complexity: Beginner | Last updated: 2026-06-02*