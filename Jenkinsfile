node {
 
        stage('Github Clone') {
            sshagent(['ssh_git','ec2_machine']) {
              echo 'clone the repo'
                sh 'ip a'
                sh  'sudo rm -r /home/jenkins/first-demo'
                sh 'sudo git clone git@github.com:ilianvo/first-demo.git /home/jenkins/first-demo'
                sh 'rsync -r /home/jenkins/first-demo/server1/ /var/www/html'
         
           }
        }
        stage('Sending files for containerization') {
            
         echo 'connect to remote host and pull down the latest version'
           
                sshagent(['ec2_machine']) {
                sh 'rsync -r -e ssh /home/jenkins/first-demo ubuntu@54.93.172.221:/home/ubuntu/jenkins_project'
                sh """
                ssh ubuntu@54.93.172.221 << EOF
                docker stop demo
                docker rm demo 
                docker system prune -a -y
                docker build -t demo /home/ubuntu/jenkins_project/first-demo
                docker run -d -p 8888:5000 --name demo demo
                exit 0
                << EOF
                """
            }
        }
        stage('Creating backup') {
        
                echo 'Check website is up'
                sshagent(['ec2_machine']) {
                sh """
                ssh ubuntu@54.93.172.221 << EOF
                rsync -r -e 'ssh -p 15984 -o StrictHostKeyChecking=no' /home/ubuntu/jenkins_project/first-demo guru96@4.tcp.eu.ngrok.io:/home/guru96/first-demo
                << EOF
                """
            }
}
}
