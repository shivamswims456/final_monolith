import pymysql, sys
from pathlib import Path
pymysql.install_as_MySQLdb()

SUPER_BASE = str(Path(__file__).resolve().parent.parent.parent)
sys.path.append(SUPER_BASE)
