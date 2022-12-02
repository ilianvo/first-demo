pipeline {
    sshagent(['thistime']) {
    stages {
        stage('apt update') {
            steps {
                echo 'clone the repo'
                sh 'sudo apt-update'
               
           }
        }
        stage('push repo to remote host') {
            steps {
                echo 'connect to remote host and pull down the latest version'
                sh 'ssh -i  ubuntu@54.93.172.221 sudo git -C /var/www/html pull'
            }
        }
        stage('Check website is up') {
            steps {
                echo 'Check website is up'
                sh 'curl -Is 54.93.172.221 | head -n 1'
            }
        }
    }
}
