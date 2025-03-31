# 📘 Kubernetes Glossary

A list of important terms you need to know for CKAD and general Kubernetes use:

| Term             | Definition |
|------------------|------------|
| **Pod**          | The smallest deployable unit in Kubernetes that can contain one or more containers. |
| **Deployment**   | A controller that ensures a specified number of pod replicas are running. |
| **ReplicaSet**   | Maintains a stable set of replica Pods running at any given time. |
| **Service**      | An abstraction that defines a logical set of Pods and a policy by which to access them. |
| **ConfigMap**    | Stores configuration data as key-value pairs. |
| **Secret**       | Stores sensitive information, such as passwords, in base64-encoded form. |
| **StatefulSet**  | Manages stateful applications and provides stable identity. |
| **Ingress**      | Manages external access to services, typically via HTTP/HTTPS. |
| **Job**          | A resource to run one-off tasks. |
| **CronJob**      | Runs jobs on a repeating schedule. |
| **Volume**       | Directory accessible to containers in a pod for persistent or shared storage. |
| **PersistentVolume (PV)** | A piece of storage in the cluster provisioned by an admin. |
| **PersistentVolumeClaim (PVC)** | A request for storage by a user. |
| **Namespace**    | Provides a way to divide cluster resources between multiple users. |
| **Node**         | A worker machine in Kubernetes. |
| **Label**        | Key-value pairs used to group and select objects. |
| **Annotation**   | Key-value metadata not used to select objects. |
| **Selector**     | Expression used to identify a set of objects. |
| **Probe**        | Used to check container health (readiness/liveness/startup). |
| **RBAC**         | Role-Based Access Control - governs who can do what. |
