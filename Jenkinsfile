pipeline {
      agent {
            label "docker"
      }

            stages {
                  stage ("build") {
                  steps {
                        sh "ls -l ; whoami ; pwd ; docker -v ; echo $WORKSPACE "
                        sh " touch bachir"

                        sh " docker build -t bachirbelkadi/jenkins:latest . "

                        }
                  }
                  stage ("pushimage") {
                  steps {
                        withCredentials([usernamePassword(credentialsId: 'Docker', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                              sh 'docker login -u  ${DOCKER_USERNAME}  -p ${DOCKER_PASSWORD}'
                        }
                        sh " docker push bachirbelkadi/jenkins:latest "
                        
                        
                        }
                  }
                  
            }
            cleanWs()
}
