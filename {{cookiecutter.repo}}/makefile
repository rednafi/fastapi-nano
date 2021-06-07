path := .

.PHONY: help
help: ## Show this help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'


.PHONY: lint
lint: black isort flake mypy	## Apply all the linters


.PHONY: lint-check
lint-check:
	@echo
	@echo "Checking linter rules..."
	@echo "========================"
	@echo
	@black --check $(path)
	@isort --check $(path)
	@flake8 $(path)
	@mypy $(path)


.PHONY: black
black: ## Apply black
	@echo
	@echo "Applying black..."
	@echo "================="
	@echo
	@ # --fast was added to circumnavigate a black bug
	@black --fast $(path)
	@echo


.PHONY: isort
isort: ## Apply isort
	@echo "Applying isort..."
	@echo "================="
	@echo
	@isort $(path)


.PHONY: flake
flake: ## Apply flake8
	@echo
	@echo "Applying flake8..."
	@echo "================="
	@echo
	@flake8 $(path)


.PHONY: mypy
mypy: ## Apply mypy
	@echo
	@echo "Applying mypy..."
	@echo "================="
	@echo
	@mypy $(path)


.PHONY: trim-imports
trim-imports: ## Remove unused imports
	@autoflake --remove-all-unused-imports \
	--ignore-init-module-imports \
	--in-place \
	--recursive \
	$(path)


.PHONY: dep-lock
dep-lock: ## Freeze deps in `requirements.txt` file
	@sort --ignore-case -o requirements.in requirements.in
	@pip-compile requirements.in --output-file=requirements.txt


.PHONY: dep-sync
dep-sync: ## Sync venv installation with `requirements.txt`
	@pip-sync
