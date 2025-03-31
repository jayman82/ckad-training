#!/bin/bash
kubectl create ns app
kubectl create ns db
kubectl apply -f k8s/base
