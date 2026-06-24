# How To: Mixed Source Types

**Difficulty**: Beginner
**Estimated Time**: 5 minutes

## Overview

Configuration example: Test config with documentation, GitHub, and PDF sources

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
config = {'name': 'test_mixed', 'description': 'Test mixed sources', 'merge_mode': 'rule-based', 'sources': [{'type': 'documentation', 'base_url': 'https://example.com'}, {'type': 'github', 'repo': 'test/repo'}, {'type': 'pdf', 'path': '/path/to/manual.pdf'}]}
```


## Complete Example

```python
# Workflow
config = {'name': 'test_mixed', 'description': 'Test mixed sources', 'merge_mode': 'rule-based', 'sources': [{'type': 'documentation', 'base_url': 'https://example.com'}, {'type': 'github', 'repo': 'test/repo'}, {'type': 'pdf', 'path': '/path/to/manual.pdf'}]}
```

## Next Steps


---

*Source: test_unified_simple.py:97 | Complexity: Beginner | Last updated: 2026-06-02*