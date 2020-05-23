# Devops Challenge Answer

---

This project contains the yaml files required to create a kafka cluster with kubernetes.

For this project, I opted to use minikube for a single pod local build, however this was also successfully tested
using a Google Cloud platform and Google Kubernetes Engine, which utilized 3 pods. I found, however, that the minikube dashboard more
 than made up the visual requirements I desired. Some things to note about this setup:

* The code is based off the official kafka-kubernetes github repo. I initially created a bare metal 
YAML script with the requirements, but felt that I wasn't getting the results I desired with the build.

* I do not believe in reinventing the wheel. That being said, the repo used proved to have robust features 
that I could not ignore for the sake of building the environment. In the end, I only used what I believe was required
for this mini project, which was kafka and zookeper, the 00-namespace configuration, plus yahoo kafka manager so to actually use kafka.
The YAML scripts assemble using Kustomize.

* It is strongly recommended to install these in a particular order:

  - 00-namespace.yml
  - Zookeeper (using Kustomize)
  - Kafka (using Kustomize)
  
* This mini project's only requirement is kubectl. Everything else is optional.


I opted to not pursue the bonus with automated testing. Most of the information
I had found online involved applying Java scripts to the system and running
stress tests on receiving and sending information to Kafka to store.

For future release, I'd want to autoscale Kafka 
once a certain storage percentage was reached, or even a certain CPU percentage was reached
in order to provide redundancy and reliability. Also, self healing would be a tremendous thing to enable in the event
of a pod going down, which could be done by implementing health checks, as well as monitoring with Prometheus.
However, that was not a part of the requirements and was left out.

I would have loved to also test this in EKS, but I was worried about that costing money which I cannot 
afford at this time.
