pipeline {
  agent any
  stages {
    stage('Checkout') {
      steps { checkout scm }
    }
    stage('Build Images') {
      steps {
        sh 'docker build -t localhost:5000/shop-backend:latest ./backend'
        sh 'docker build -t localhost:5000/shop-frontend:latest ./frontend'
      }
    }
    stage('Push to Local Registry') {
      steps {
        sh 'docker push localhost:5000/shop-backend:latest'
        sh 'docker push localhost:5000/shop-frontend:latest'
      }
    }
    stage('Deploy to Kubernetes') {
      steps {
        sh 'kubectl apply -f deploy/k8s-backend.yaml'
        sh 'kubectl apply -f deploy/k8s-frontend.yaml'
      }
    }
  }
}
