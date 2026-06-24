# How To: Config File

**Difficulty**: Beginner
**Estimated Time**: 5 minutes
**Tags**: pytest

## Overview

Configuration example: Create a minimal test config file

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
config = {'name': 'test-cli-e2e', 'description': 'Test skill for CLI E2E testing', 'base_url': 'https://example.com/docs/', 'selectors': {'main_content': 'article', 'title': 'title', 'code_blocks': 'pre'}, 'url_patterns': {'include': ['/docs/'], 'exclude': []}, 'categories': {}, 'rate_limit': 0.1, 'max_pages': 3}
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path

# Workflow
config = {'name': 'test-cli-e2e', 'description': 'Test skill for CLI E2E testing', 'base_url': 'https://example.com/docs/', 'selectors': {'main_content': 'article', 'title': 'title', 'code_blocks': 'pre'}, 'url_patterns': {'include': ['/docs/'], 'exclude': []}, 'categories': {}, 'rate_limit': 0.1, 'max_pages': 3}
```

## Next Steps


---

*Source: test_install_skill_e2e.py:325 | Complexity: Beginner | Last updated: 2026-06-02*