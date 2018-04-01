# grpc-kubernetes

Simple grpc client/server, with the server being deployed using kubernetes

## Requirements

You need to have:

- docker
- kubectl
- minikube (optional)

## Try it out !

Here is an example to make an rpc call to a server deployed inside a minikube

```bash
git clone git@github.com:CLevasseur/grpc-kubernetes.git
minikube start
cd grpc-kubernetes
# create server deployment and service
kubectl apply -f kubernetes/
# make an rpc call to the minikube ip
docker run clevasseur/simple_grpc_client python grpc-kubernetes/client.py --server-ip $(minikube ip)
```

You should get the answer from the server:

```
received: Hello, you!
```
