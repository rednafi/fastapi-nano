path := .

define Comment
	- Run `make help` to see all the available options.
	- Run `make lint` to run the linter.
	- Run `make lint-check` to check linter conformity.
	- Run `dep-lock` to lock the deps in 'requirements.txt' and 'requirements-dev.txt'.
	- Run `dep-sync` to sync current environment up to date with the locked deps.
endef


.PHONY: lint
lint: ruff mypy	## Apply all the linters.

.PHONY: lint-check
lint-check:  ## Check whether the codebase satisfies the linter rules.
	@echo
	@echo "Checking linter rules..."
	@echo "========================"
	@echo
	@uv run ruff check $(path)
	@uv run mypy $(path)

.PHONY: ruff
ruff: ## Apply ruff.
	@echo "Applying ruff..."
	@echo "================"
	@echo
	@uv run ruff check --fix $(path)
	@uv run ruff format $(path)

.PHONY: mypy
mypy: ## Apply mypy.
	@echo
	@echo "Applying mypy..."
	@echo "================="
	@echo
	@uv run mypy $(path)

.PHONY: help
help: ## Show this help message.
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.PHONY: test
test: ## Run the tests against the current version of Python.
	cd svc && uv run pytest -vv && cd ..

.PHONY: dep-lock
dep-lock: ## Freeze deps in 'requirements*.txt' files.
	@uv lock

.PHONY: dep-sync
dep-sync: ## Sync venv installation with 'requirements.txt' file.
	@uv sync

.PHONY: dep-update
dep-update: ## Update all the deps.
	@chmod +x ./bin/update_deps.sh
	@./bin/update_deps.sh

.PHONY: run-container
run-container: ## Run the app in a docker container.
	docker compose up -d

.PHONY: kill-container
kill-container: ## Stop the running docker container.
	docker compose down

.PHONY: run-local
run-local: ## Run the app locally.
	uvicorn svc.main:app --port 5002 --reload
