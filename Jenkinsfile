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
            bat(script: 'py Menu.py', returnStatus: true)
            build(job: 'py Menu.py', wait: true, quietPeriod: 5)
            echo '"Image Job executed SUCCESSFULLY"'
          }
        }
        stage('Build') {
          steps {
            bat(script: 'py Image.py', returnStatus: true)
            build(job: 'py Image1.py', quietPeriod: 5, wait: true)
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