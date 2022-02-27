# Database creation
```sqlite3
sqlite3 development-db.db
.tables
.exit
```

```python
from sinntelligence.database import db
db.create_all()
```