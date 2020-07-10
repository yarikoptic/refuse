# REFUSE
# Simple cross-plattform ctypes bindings for libfuse / FUSE for macOS / WinFsp
# https://github.com/pleiszenburg/refuse
#
#   makefile: GNU makefile for project management
#
#   Copyright (C) 2008-2020 refuse contributors
#
# <LICENSE_BLOCK>
# The contents of this file are subject to the Internet Systems Consortium (ISC)
# license ("ISC license" or "License"). You may not use this file except in
# compliance with the License. You may obtain a copy of the License at
# https://opensource.org/licenses/ISC
# https://github.com/pleiszenburg/refuse/blob/master/LICENSE
#
# Software distributed under the License is distributed on an "AS IS" basis,
# WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License for the
# specific language governing rights and limitations under the License.
# </LICENSE_BLOCK>


clean:
	-rm -r build/*
	-rm -r dist/*
	-rm -r src/*.egg-info
	# -rm -r htmlconv/*
	# -rm .coverage*
	coverage erase
	find src/ tests/ -name '*.pyc' -exec rm -f {} +
	find src/ tests/ -name '*.pyo' -exec rm -f {} +
	# find src/ tests/ -name '*~' -exec rm -f {} +
	find src/ tests/ -name '__pycache__' -exec rm -fr {} +
	# find src/ tests/ -name '*.htm' -exec rm -f {} +
	# find src/ tests/ -name '*.html' -exec rm -f {} +
	# find src/ tests/ -name '*.so' -exec rm -f {} +

release:
	make clean
	python setup.py sdist bdist_wheel
	gpg --detach-sign -a dist/refuse*.whl
	gpg --detach-sign -a dist/refuse*.tar.gz

upload:
	for filename in $$(ls dist/*.tar.gz dist/*.whl) ; do \
		twine upload $$filename $$filename.asc ; \
	done

upload_test:
	for filename in $$(ls dist/*.tar.gz dist/*.whl) ; do \
		twine upload $$filename $$filename.asc -r pypitest ; \
	done

install:
	pip install .[dev]

install_link:
	pip install -e .[dev]

# test:
# 	pytest

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ANALYSIS
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

dump_header:
	python -m refuse._inventory
