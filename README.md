# finance-rag-production
finance-rag-production


## Production Phases

Phase 1: Core RAG Application (Local Python)
- data, environment, requirements.txt, gitignore
- app.py
- rag_pipeline.py

test the app.py using curl:
curl -X POST -H "Content-Type: application/json" -d '{"question":"What are the main risks?"}' http://localhost:5001/query



Phase 2: Containerization (Docker)
package the flask app and chromadb into docker containers




Phase 3: CI/CD Automation (github actions)
automate testing and deployment with github actions

- ci.yml
- test rag


Phase 4: ML Orchestration (Airflow)
automate the indexing pipeline with airflow

dags - Directed Acyclic Graph - workflow of your pipeline


Phase 5: Monitoring & Observability (Grafana and Prometheus)

add prometheus and grafana(vizualization) for monitoring

- docker-compose.yml
- prometheus.yml

Phase 6: Infrastructure as Code (AWS Deployment)
