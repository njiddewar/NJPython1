pipeline {
  agent any
  stages {
    stage('Build') {
      parallel {
        stage('Build') {
          steps {
            build(propagate: true, job: 'Menu.py', quietPeriod: 2, wait: true)
          }
        }
        stage('Build') {
          steps {
            build(job: 'Image1.py', propagate: true, quietPeriod: 2, wait: true)
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