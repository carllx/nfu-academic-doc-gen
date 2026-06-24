# How To: Config Validation Errors

**Difficulty**: Beginner
**Estimated Time**: 5 minutes

## Overview

Configuration example: Test that invalid configs are rejected

## Prerequisites

**Required Modules:**
- `json`
- `os`
- `sys`
- `tempfile`
- `pathlib`
- `config_validator`
- `traceback`


## Step-by-Step Guide

### Step 1: Assign config = value

```python
config = {'name': 'test', 'description': 'Test', 'sources': [{'type': 'invalid_type', 'url': 'https://example.com'}]}
```


## Complete Example

```python
# Workflow
config = {'name': 'test', 'description': 'Test', 'sources': [{'type': 'invalid_type', 'url': 'https://example.com'}]}
```

## Next Steps


---

*Source: test_unified_simple.py:131 | Complexity: Beginner | Last updated: 2026-06-02*