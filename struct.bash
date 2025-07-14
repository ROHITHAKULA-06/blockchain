mkdir protocol-upgrade-monitor
cd protocol-upgrade-monitor
mkdir -p app/{api,models,services,utils,tests} data
touch app/{__init__,main,config}.py
touch app/api/{endpoints,dependencies}.py
touch app/models/{blockchain,risk}.py
touch app/services/{data_fetchers,analytics,cache}.py
touch app/utils/{logging,helpers}.py
touch requirements.txt .env Dockerfile README.md