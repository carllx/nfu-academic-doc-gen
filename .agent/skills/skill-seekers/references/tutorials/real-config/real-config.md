# How To: Real Config

**Difficulty**: Beginner
**Estimated Time**: 5 minutes
**Tags**: pytest

## Overview

Configuration example: Create a real minimal config that can be scraped

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `json`
- `subprocess`
- `sys`
- `pathlib`
- `unittest.mock`
- `pytest`
- `skill_seekers.mcp.tools.packaging_tools`
- `mcp.types`
- `skill_seekers.mcp.server`
- `skill_seekers.mcp.server`

**Setup Required:**
```python
# Fixtures: tmp_path
```

## Step-by-Step Guide

### Step 1: Assign config = value

```python
config = {'name': 'test-real-e2e', 'description': 'Real E2E test', 'sources': [{'type': 'documentation', 'base_url': 'https://httpbin.org/html', 'selectors': {'main_content': 'body', 'title': 'title', 'code_blocks': 'code'}, 'url_patterns': {'include': [], 'exclude': []}, 'categories': {}, 'rate_limit': 0.5, 'max_pages': 1}]}
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path

# Workflow
config = {'name': 'test-real-e2e', 'description': 'Real E2E test', 'sources': [{'type': 'documentation', 'base_url': 'https://httpbin.org/html', 'selectors': {'main_content': 'body', 'title': 'title', 'code_blocks': 'code'}, 'url_patterns': {'include': [], 'exclude': []}, 'categories': {}, 'rate_limit': 0.5, 'max_pages': 1}]}
```

## Next Steps


---

*Source: test_install_skill_e2e.py:465 | Complexity: Beginner | Last updated: 2026-06-02*