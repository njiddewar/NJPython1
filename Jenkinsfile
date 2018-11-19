pipeline {
  agent none
  stages {
    stage('Build') {
      environment {
        Python = 'Py'
      }
      parallel {
        stage('Build') {
          steps {
            build(job: 'Py Menu.py', wait: true)
          }
        }
        stage('Build') {
          steps {
            build 'Py Image1.py'
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