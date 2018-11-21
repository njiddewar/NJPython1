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
            echo '"Image Job executed SUCCESSFULLY"'
          }
        }
        stage('Build') {
          steps {
            bat(script: 'py Image.py', returnStatus: true)
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
    stage('Deploy') {
      steps {
        mail(subject: 'Success', body: 'Job executed with Pipeline', from: 'nilesh.jiddewar@tieto.com', to: 'nilesh.jiddewar@tieto.com')
      }
    }
  }
}