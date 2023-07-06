pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        sh 'python3 --version'
        sh ' hostname'
      }
    }
    stage('hello') {
      steps {
        sh 'python3 hello.py'
      }
    }
  }
}
