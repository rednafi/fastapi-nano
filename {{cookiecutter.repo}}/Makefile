# REDNAFI contact: redowan.nafi@gmail.com

# Make sure your environment is named venv

# Usage (line =black line length, path = action path)
# ------
# make pylinter
#
# or,
#
# make pylinter line=79 path=myfolder

path := .
line := 88

pylinter:
# raises error if environment is not active
ifeq ("$(VIRTUAL_ENV)","")
	@echo "Venv is not activated!"
	@echo "Activate venv first."
	@echo
	exit 1
endif

# checks if black is installed
ifeq ("$(wildcard venv/bin/black)","")
	@echo "Installing Black..."
	@pip install black
endif

# checks if isort is installed
ifeq ("$(wildcard venv/bin/isort)","")
	@echo "Installing Isort..."
	@pip install isort
endif

# checks if flake8 is installed
ifeq ("$(wildcard venv/bin/flake8)","")
	@echo -e "Installing flake8..."
	@pip install flake8
	@echo
endif

# black
	@echo "Applying Black"
	@echo "----------------\n"
	@black -l $(line) $(path)
	@echo

# isort
	@echo "Applying Isort"
	@echo "----------------\n"
	@isort --atomic --profile black $(path)
	@echo

# flake8
	@echo "Applying Flake8"
	@echo "----------------\n"
	@flake8 --max-line-length "$(line)" \
			--max-complexity "18" \
			--select "B,C,E,F,W,T4,B9" \
			--ignore "E203,E266,E501,W503,F403,F401,E402" \
			--exclude ".git,__pycache__,old, build, \
						dist, venv" $(path)
