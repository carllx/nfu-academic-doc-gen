# How To: Update Sorts Plugins Alphabetically

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: mock, workflow, integration

## Overview

Workflow: test update sorts plugins alphabetically

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `json`
- `os`
- `unittest.mock`
- `pytest`
- `skill_seekers.mcp.marketplace_publisher`
- `git`
- `skill_seekers.mcp.marketplace_manager`
- `git`
- `skill_seekers.mcp.marketplace_manager`
- `skill_seekers.mcp.marketplace_manager`
- `git`
- `skill_seekers.mcp.marketplace_manager`
- `skill_seekers.mcp.git_repo`
- `git`
- `skill_seekers.mcp.marketplace_manager`
- `skill_seekers.mcp.git_repo`
- `pathlib`

**Setup Required:**
```python
# Fixtures: mock_marketplace_repo
```

## Step-by-Step Guide

### Step 1: Assign publisher = MarketplacePublisher.__new__(...)

```python
publisher = MarketplacePublisher.__new__(MarketplacePublisher)
```

**Verification:**
```python
assert names == sorted(names)
```

### Step 2: Assign author = value

```python
author = {'name': 'Test', 'email': 'test@example.com'}
```

### Step 3: Call publisher._update_marketplace_json()

```python
publisher._update_marketplace_json(mock_marketplace_repo, 'aaa-plugin', 'First', author, 'dev')
```

### Step 4: Assign names = value

```python
names = [p['name'] for p in data['plugins']]
```

**Verification:**
```python
assert names == sorted(names)
```

### Step 5: Assign data = json.load(...)

```python
data = json.load(f)
```


## Complete Example

```python
# Setup
# Fixtures: mock_marketplace_repo

# Workflow
publisher = MarketplacePublisher.__new__(MarketplacePublisher)
author = {'name': 'Test', 'email': 'test@example.com'}
publisher._update_marketplace_json(mock_marketplace_repo, 'aaa-plugin', 'First', author, 'dev')
with open(mock_marketplace_repo / '.claude-plugin' / 'marketplace.json') as f:
    data = json.load(f)
names = [p['name'] for p in data['plugins']]
assert names == sorted(names)
```

## Next Steps


---

*Source: test_marketplace_publisher.py:157 | Complexity: Intermediate | Last updated: 2026-06-02*