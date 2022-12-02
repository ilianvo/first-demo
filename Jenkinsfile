node {
   sshagent(['thistime']) {
     sh """
     ssh -T -o StrictHostKeyChecking=no -i index.html ubuntu@54.93.172.221 << EOF
     sudo apt update
     hostname -I
     ip a
     << EOF
     """
      
        stage('apt update') {
            
              echo 'clone the repo'
                sh 'ip a'
               
           }
        }
        stage('push repo to remote host') {
            
         echo 'connect to remote host and pull down the latest version'
            sh 'git clone https://github.com/ilianvo/first-demo.git /home/ubuntu/first-demo'
         
                sshagent(['thistime']) {
                sh 'scp -r /home/ubuntu/first-demo ubuntu@54.93.172.221:/home/ubuntu/'
            }
        }
        stage('Check website is up') {
        
                echo 'Check website is up'
                sh 'curl -Is 54.93.172.221 | head -n 1'
            }
}
