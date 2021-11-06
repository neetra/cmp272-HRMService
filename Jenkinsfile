pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                pip -V
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
