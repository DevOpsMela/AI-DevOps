Starting Minikube locally is straightforward. Here’s a clean step-by-step setup (works on macOS like yours).

---

## ✅ 1. Prerequisites check

Make sure you already have:

* Docker Desktop installed and running (recommended driver)
* kubectl installed
* Minikube installed

Check versions:

```bash
docker --version
kubectl version --client
minikube version
```

---

## 🚀 2. Start Minikube

### Recommended (Docker driver)

```bash
minikube start --driver=docker
```

---

## ⚙️ Optional: allocate more resources

If you want a smoother Kubernetes experience:

```bash
minikube start \
  --driver=docker \
  --cpus=4 \
  --memory=6g \
  --disk-size=20g
```

---

## 📦 3. Verify cluster is running

```bash
minikube status
```

Check nodes:

```bash
kubectl get nodes
```

Expected output:

```
NAME       STATUS   ROLES           AGE   VERSION
minikube   Ready    control-plane   ...
```

---

## 🌐 4. Enable Kubernetes dashboard (optional but useful)

```bash
minikube dashboard
```

This opens a UI in your browser.

---

## 🧪 5. Quick test deployment

```bash
kubectl create deployment nginx --image=nginx
kubectl expose deployment nginx --type=NodePort --port=80
```

Get service URL:

```bash
minikube service nginx
```

---

## 🛑 6. Stop / delete cluster (when needed)

Stop:

```bash
minikube stop
```

Delete:

```bash
minikube delete
```

---

## ⚠️ Common issues

* Docker not running → start Docker Desktop
* Low memory error → increase `--memory`
* kubectl mismatch → reinstall kubectl or use `minikube kubectl --`

---
