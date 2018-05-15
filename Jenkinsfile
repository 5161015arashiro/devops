def jenkins_path= "/var/lib/jenkins"
 
node {
 
    stage('scm'){
        checkout scm
    }
 
    stage('terraform'){
        sh"cd /var/lib/jenkins & terraform apply"
    }
}