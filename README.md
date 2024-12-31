# OttoBot




```
# Start docker

# Start le Minikube
minikube start

# Change to manifests directory
cd kubernetes_manifests

# Mount ollama directory in le Minikube
minikube mount D:/Programs/Ollama/models:/mnt/models

# Deploy kubernetes objects
kubectl apply -f ollama.yaml
kubectl apply -f ottobot_ui.yaml

# Expose the ui service outside le Minikube
minikube service ottobot-ui --url

```
