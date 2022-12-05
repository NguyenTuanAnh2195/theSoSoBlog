local-up:
	docker-compose -f local.yml up -d

local-stop:
	docker-compose -f local.yml stop

local-down:
	docker-compose -f local.yml down

local-build:
	docker-compose -f local.yml build

local-command:
	docker-compose -f local.yml run django $(command)
