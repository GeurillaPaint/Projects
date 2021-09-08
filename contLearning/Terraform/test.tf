resource "kubernetes_pod" "example" {
    metadata {
        name = "terraform-example"
    }

    spec {
        container {
            image = "nginx:1.7"
            name  = "example"
        }
    }
}