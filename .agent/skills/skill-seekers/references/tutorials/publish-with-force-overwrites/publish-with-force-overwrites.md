# How To: Publish With Force Overwrites

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: mock, workflow, integration

## Overview

Workflow: Test that force=True overwrites an existing plugin.

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
# Fixtures: skill_dir, tmp_path
```

## Step-by-Step Guide

### Step 1: 'Test that force=True overwrites an existing plugin.'

```python
'Test that force=True overwrites an existing plugin.'
```

**Verification:**
```python
assert result['success'] is True
```

### Step 2: Assign working_path = value

```python
working_path = tmp_path / 'working'
```

### Step 3: Call working_path.mkdir()

```python
working_path.mkdir()
```

### Step 4: Assign repo = gitmodule.Repo.init(...)

```python
repo = gitmodule.Repo.init(working_path, initial_branch='main')
```

### Step 5: Call repo.config_writer.set_value.release()

```python
repo.config_writer().set_value('user', 'name', 'Test').release()
```

### Step 6: Call repo.config_writer.set_value.release()

```python
repo.config_writer().set_value('user', 'email', 't@t.com').release()
```

### Step 7: Assign mp_dir = value

```python
mp_dir = working_path / '.claude-plugin'
```

### Step 8: Call mp_dir.mkdir()

```python
mp_dir.mkdir()
```

### Step 9: Call unknown.mkdir()

```python
(working_path / 'plugins' / 'test-skill' / '.claude-plugin').mkdir(parents=True)
```

### Step 10: Call repo.index.add()

```python
repo.index.add(['.claude-plugin/marketplace.json'])
```

### Step 11: Call repo.index.commit()

```python
repo.index.commit('Initial')
```

### Step 12: Assign bare_repo_path = value

```python
bare_repo_path = tmp_path / 'remote.git'
```

### Step 13: Call gitmodule.Repo.clone_from()

```python
gitmodule.Repo.clone_from(str(working_path), str(bare_repo_path), bare=True)
```

### Step 14: Assign config_dir = value

```python
config_dir = tmp_path / 'config'
```

### Step 15: Call config_dir.mkdir()

```python
config_dir.mkdir()
```

### Step 16: Assign manager = MarketplaceManager(...)

```python
manager = MarketplaceManager(config_dir=str(config_dir))
```

### Step 17: Call manager.add_marketplace()

```python
manager.add_marketplace(name='local-test', git_url=f'file://{bare_repo_path}', token_env='DUMMY_TOKEN', branch='main', author={'name': 'Test', 'email': 't@t.com'})
```

### Step 18: Assign cache_dir = value

```python
cache_dir = tmp_path / 'cache'
```

### Step 19: Call cache_dir.mkdir()

```python
cache_dir.mkdir()
```

### Step 20: Assign publisher = MarketplacePublisher.__new__(...)

```python
publisher = MarketplacePublisher.__new__(MarketplacePublisher)
```

### Step 21: Assign publisher.git_repo = GitConfigRepo(...)

```python
publisher.git_repo = GitConfigRepo(cache_dir=str(cache_dir))
```

**Verification:**
```python
assert result['success'] is True
```

### Step 22: Call json.dump()

```python
json.dump({'$schema': '', 'name': 't', 'description': '', 'owner': {}, 'plugins': []}, f)
```

### Step 23: Assign result = publisher.publish(...)

```python
result = publisher.publish(skill_dir=skill_dir, marketplace_name='local-test', category='testing', force=True)
```


## Complete Example

```python
# Setup
# Fixtures: skill_dir, tmp_path

# Workflow
'Test that force=True overwrites an existing plugin.'
import git as gitmodule
working_path = tmp_path / 'working'
working_path.mkdir()
repo = gitmodule.Repo.init(working_path, initial_branch='main')
repo.config_writer().set_value('user', 'name', 'Test').release()
repo.config_writer().set_value('user', 'email', 't@t.com').release()
mp_dir = working_path / '.claude-plugin'
mp_dir.mkdir()
with open(mp_dir / 'marketplace.json', 'w') as f:
    json.dump({'$schema': '', 'name': 't', 'description': '', 'owner': {}, 'plugins': []}, f)
(working_path / 'plugins' / 'test-skill' / '.claude-plugin').mkdir(parents=True)
repo.index.add(['.claude-plugin/marketplace.json'])
repo.index.commit('Initial')
bare_repo_path = tmp_path / 'remote.git'
gitmodule.Repo.clone_from(str(working_path), str(bare_repo_path), bare=True)
config_dir = tmp_path / 'config'
config_dir.mkdir()
from skill_seekers.mcp.marketplace_manager import MarketplaceManager
manager = MarketplaceManager(config_dir=str(config_dir))
manager.add_marketplace(name='local-test', git_url=f'file://{bare_repo_path}', token_env='DUMMY_TOKEN', branch='main', author={'name': 'Test', 'email': 't@t.com'})
cache_dir = tmp_path / 'cache'
cache_dir.mkdir()
publisher = MarketplacePublisher.__new__(MarketplacePublisher)
from skill_seekers.mcp.git_repo import GitConfigRepo
publisher.git_repo = GitConfigRepo(cache_dir=str(cache_dir))
with patch.dict(os.environ, {'DUMMY_TOKEN': 'x'}), patch('skill_seekers.mcp.marketplace_publisher.MarketplaceManager', return_value=manager):
    result = publisher.publish(skill_dir=skill_dir, marketplace_name='local-test', category='testing', force=True)
assert result['success'] is True
```

## Next Steps


---

*Source: test_marketplace_publisher.py:380 | Complexity: Advanced | Last updated: 2026-06-02*