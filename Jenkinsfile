pipeline {
    agent any
  
    stages{
        stage('Access Github'){
            steps{
                git branch: 'main', credentialsId: 'github', url: 'git@github.com:ilianvo/first-demo.git'             
                 }
           }
            stage('Docker Build'){
              steps{
                script{           
                   sh 'sudo docker build -t demo .'
        }
    }
}
        stage('Push to Docker Registry'){
            steps{
                script{
                    withCredentials([string(credentialsId: 'Token', variable: 'mytoken')]) {
                     sh 'sudo docker login -u ilianvo -p ${mytoken}'
}
                     sh 'sudo docker tag demo ilianvo/demo'
                     sh 'sudo docker push ilianvo/demo'
                     sh 'sudo docker system prune -a -f'
                    }
                }
            }
        stage ('Deploy Docker image'){
            steps{
                script{
                    sshagent(['ec2_machine']) {
                     sh """
                     ssh ubuntu@3.75.213.28 << EOF
                     sudo docker stop demo
                     sudo docker system prune -a -f
                     sudo docker pull ilianvo/demo
                     sudo docker run -t -d -p 8888:5000 --name demo ilianvo/demo
                     << EOF
                     """
}
                }
            }
        }
    }
}
