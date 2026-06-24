# How To: Add Marketplace Full Parameters

**Difficulty**: Beginner
**Estimated Time**: 5 minutes
**Tags**: workflow, integration

## Overview

Workflow: test add marketplace full parameters

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `json`
- `pathlib`
- `pytest`
- `skill_seekers.mcp.marketplace_manager`

**Setup Required:**
```python
# Fixtures: manager
```

## Step-by-Step Guide

### Step 1: Assign author = value

```python
author = {'name': 'Spyke Team', 'email': 'team@spyke.com'}
```

**Verification:**
```python
assert mp['token_env'] == 'SPYKE_TOKEN'
```

### Step 2: Assign mp = manager.add_marketplace(...)

```python
mp = manager.add_marketplace(name='spyke', git_url='https://github.com/spykegames/plugins.git', token_env='SPYKE_TOKEN', branch='develop', author=author, enabled=False)
```

**Verification:**
```python
assert mp['branch'] == 'develop'
```


## Complete Example

```python
# Setup
# Fixtures: manager

# Workflow
author = {'name': 'Spyke Team', 'email': 'team@spyke.com'}
mp = manager.add_marketplace(name='spyke', git_url='https://github.com/spykegames/plugins.git', token_env='SPYKE_TOKEN', branch='develop', author=author, enabled=False)
assert mp['token_env'] == 'SPYKE_TOKEN'
assert mp['branch'] == 'develop'
assert mp['author'] == author
assert mp['enabled'] is False
```

## Next Steps


---

*Source: test_marketplace_manager.py:69 | Complexity: Beginner | Last updated: 2026-06-02*