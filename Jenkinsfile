pipeline {
      agent any 

            stages {
                  stage ("build") {
                  steps {
                        sh "ls -l ; whoami ; pwd ; docker -v"

                        sh " docker build -t bachirbelkadi/jenkins:latest . "

                        }
                  }
                  stage ("pushimage") {
                  steps {
                        withCredentials([usernamePassword(credentialsId: 'Docker', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                              sh 'docker login -u  ${USERNAME}  -p ${PASSWORD}'
                        }
                        sh """
                              - docker push bachirbelkadi/jenkins:latest 
                        
                        """
                        }
                  }
                  
            }
}
