node {
   sshagent(['thistime']) {
     sh 'sh StrictHostKeyChecking=no -i ubuntu ubuntu@54.93.172.221'
        stage('apt update') {
            
              echo 'clone the repo'
                sh 'sudo apt-get update'
               
           }
        }
        stage('push repo to remote host') {
            
                echo 'connect to remote host and pull down the latest version'
                sh 'ssh -i  ubuntu ubuntu@54.93.172.221 sudo git -C /var/www/html pull'
            }
        }
        stage('Check website is up') {
        
                echo 'Check website is up'
                sh 'curl -Is 54.93.172.221 | head -n 1'
            }
