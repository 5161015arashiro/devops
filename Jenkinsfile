def bit_name= "devops"
def bit_url= "git@bitbucket.org:hirocomarashiro/${bit_name}.git"
def jenkins_path= "/var/lib/jenkins"
 
node {
 
    stage('scm'){
        checkout scm
    }
 
    stage('first job'){
        sh"echo hello"
    }
}