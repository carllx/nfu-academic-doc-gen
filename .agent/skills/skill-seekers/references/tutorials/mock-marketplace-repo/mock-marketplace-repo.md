# How To: Mock Marketplace Repo

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, mock, workflow, integration

## Overview

Workflow: mock marketplace repo

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
# Fixtures: tmp_path
```

## Step-by-Step Guide

### Step 1: Assign repo_path = value

```python
repo_path = tmp_path / 'marketplace_repo'
```

### Step 2: Call repo_path.mkdir()

```python
repo_path.mkdir()
```

### Step 3: Assign repo = git.Repo.init(...)

```python
repo = git.Repo.init(repo_path)
```

### Step 4: Assign mp_dir = value

```python
mp_dir = repo_path / '.claude-plugin'
```

### Step 5: Call mp_dir.mkdir()

```python
mp_dir.mkdir()
```

### Step 6: Assign mp_json = value

```python
mp_json = {'$schema': 'https://anthropic.com/claude-code/marketplace.schema.json', 'name': 'test-marketplace', 'description': 'Test marketplace', 'owner': {'name': 'Test', 'email': 'test@example.com'}, 'plugins': [{'name': 'existing-plugin', 'description': 'An existing plugin', 'author': {'name': 'Test', 'email': 'test@example.com'}, 'source': './plugins/existing-plugin', 'category': 'development'}]}
```

### Step 7: Call unknown.mkdir()

```python
(repo_path / 'plugins').mkdir()
```

### Step 8: Call repo.index.add()

```python
repo.index.add(['.claude-plugin/marketplace.json'])
```

### Step 9: Call repo.index.commit()

```python
repo.index.commit('Initial commit')
```

### Step 10: Call json.dump()

```python
json.dump(mp_json, f, indent=2)
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path

# Workflow
import git
repo_path = tmp_path / 'marketplace_repo'
repo_path.mkdir()
repo = git.Repo.init(repo_path)
mp_dir = repo_path / '.claude-plugin'
mp_dir.mkdir()
mp_json = {'$schema': 'https://anthropic.com/claude-code/marketplace.schema.json', 'name': 'test-marketplace', 'description': 'Test marketplace', 'owner': {'name': 'Test', 'email': 'test@example.com'}, 'plugins': [{'name': 'existing-plugin', 'description': 'An existing plugin', 'author': {'name': 'Test', 'email': 'test@example.com'}, 'source': './plugins/existing-plugin', 'category': 'development'}]}
with open(mp_dir / 'marketplace.json', 'w') as f:
    json.dump(mp_json, f, indent=2)
(repo_path / 'plugins').mkdir()
repo.index.add(['.claude-plugin/marketplace.json'])
repo.index.commit('Initial commit')
return repo_path
```

## Next Steps


---

*Source: test_marketplace_publisher.py:43 | Complexity: Advanced | Last updated: 2026-06-02*