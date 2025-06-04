#!/bin/bash

minikube stop
minikube delete

sudo chmod o+w /usr/local/share/metaflow/ -R
MINIKUBE_MEMORY=2200mb MINIKUBE_CPUS=3 metaflow-dev up
