.PHONY: sql-grammars
./artifacts/cockroachdb.y:
	./scripts/download/cockroachdb.y.py
./artifacts/mysql.g4:
	./scripts/download/mysql.g4.py
./artifacts/mysql.y:
	./scripts/download/mysql.y.py
./artifacts/mariadb.y:
	./scripts/download/mariadb.y.py
./artifacts/vitesse.y:
	./scripts/download/vitesse.y.py
./artifacts/postgres.y:
	./scripts/download/postgres.y.py
./artifacts/sqlite.g4:
	./scripts/download/sqlite.g4.py
./artifacts/sqlite.y:
	./scripts/download/sqlite.y.py
./artifacts/monetdb.y:
	./scripts/download/monetdb.y.py
./artifacts/sql92.bnf:
	./scripts/download/sql92.bnf.py
./artifacts/sql99.bnf:
	./scripts/download/sql99.bnf.py
./artifacts/sql2003.bnf:
	./scripts/download/sql2003.bnf.py

SQL_GRAMMARS = \
	./artifacts/cockroachdb.y \
	./artifacts/mysql.g4 \
	./artifacts/mysql.y \
	./artifacts/mariadb.y \
	./artifacts/vitesse.y \
	./artifacts/postgres.y \
	./artifacts/sqlite.g4 \
	./artifacts/sqlite.y \
	./artifacts/monetdb.y \
	./artifacts/sql92.bnf \
	./artifacts/sql99.bnf \
	./artifacts/sql2003.bnf

sql-grammars: $(SQL_GRAMMARS)
