# OttoBot


## Start docker

## Start le Minikube

```bash
minikube start
```

## Change to manifests directory
```bash
cd kubernetes_manifests
```

## Mount ollama directory in le Minikube
```bash
minikube mount D:/Programs/Ollama/models:/mnt/models
```

## Deploy kubernetes objects
```bash
kubectl apply -f ollama.yaml
kubectl apply -f ottobot_ui.yaml
```

## Expose the ui service outside le Minikube
```bash
minikube service ottobot-ui --url
```
