.PHONY: docs up down logs clean-docs help

BACKEND_CONTAINER = transport-company-backend
DOCS_DIR = docs
OPENAPI_FILE = $(DOCS_DIR)/openapi.json
MD_FILE = $(DOCS_DIR)/API-Документация.md

docs:
	@echo "🚀 Генерация API документации..."
	@docker exec $(BACKEND_CONTAINER) python manage.py spectacular \
		--file /app/docs/openapi.json \
		--format openapi-json
	@echo "✅ openapi.json создан"
	@echo "🚀 Генерация Markdown..."
	@docker exec $(BACKEND_CONTAINER) openapi2markdown \
		/app/docs/openapi.json \
		/app/docs/API-Документация.md
	@echo "✅ API-Документация.md готов!"

up:
	@docker compose up -d

down:
	@docker compose down

logs:
	@docker compose logs -f backend

clean-docs:
	@rm -f $(OPENAPI_FILE) $(MD_FILE)

help:
	@echo "Команды:"
	@echo "  make docs       - Генерация документации"
	@echo "  make up         - Запуск контейнеров"
	@echo "  make down       - Остановка"
	@echo "  make logs       - Логи backend"
	@echo "  make clean-docs - Удалить документацию"
