node {
   sshagent(['thistime']) {
     sh 'scp -o https://github.com/ilianvo/first-demo.git ubuntu@54.93.172.221:var/www/html'
      
        stage('apt update') {
            
              echo 'clone the repo'
                sh 'ip a'
               
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
