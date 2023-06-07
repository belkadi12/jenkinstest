pipeline {
      agent any 

      environment {
            DOCKER = credentials ('Docker')
                  }

            stages {
                  stage ("build") {
                  steps {
                        sh "ls -l ; whoami ; pwd ; docker -v"

                        sh " docker build -t bachirbelkadi/jenkins:latest . "

                        }
                  }
                  stage ("pushimage") {
                  steps {
                        sh """
                              
                              - docker login -u  ${DOCKER_USERNAME}  -p ${DOCKER_PASSWORD}
                              - docker push bachirbelkadi/jenkins:latest 
                        
                        """
                        }
                  }
                  
            }
}
