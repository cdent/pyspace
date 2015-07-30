
# Test related targets don't do anything yet

test: .venv runtests

runtests:
	.venv/bin/py.test -svx --tb=short test

.venv:
	python -m virtualenv -p python3 .venv
	.venv/bin/pip install -U -r requirements.txt

clean:
	rm -r .venv || true
	find . -name "*.pyc" -delete

run: .venv
	.venv/bin/python -c 'import pyspace; pyspace.main_loop()' < info
