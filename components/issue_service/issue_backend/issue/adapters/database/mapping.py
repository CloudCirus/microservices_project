from sqlalchemy.orm import registry

from issue.application.dataclasses import Issue

from .tables import issue_table

mapper = registry()

mapper.map_imperatively(Issue, issue_table)
