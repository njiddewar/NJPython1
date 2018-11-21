pipeline {
  agent any
  stages {
    stage('Build') {
      environment {
        Python = 'Py'
      }
      parallel {
        stage('Build') {
          steps {
            bat(script: 'py Menu.py', returnStatus: true)
            echo '"Menu Program executed SUCCESSFULLY"'
          }
        }
        stage('Build') {
          steps {
            bat(script: 'py Image1.py', returnStatus: true)
            echo 'Image1 Execued SUCCESSFULLY!!!'
          }
        }
      }
    }
    stage('Print') {
      steps {
        echo '"Both jobs executed Successfuly"'
      }
    }
  }
}