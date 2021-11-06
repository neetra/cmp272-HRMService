pipeline {
    agent any

    stages {
        stage('Prepare') {
            steps {
                echo 'Checking env ...'
                bat 'python --version'
                bat 'pip --version'
            }
        }
        stage('Build') {
            steps {
                echo 'Building..'
                bat 'pip install -r requirements.txt'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
                bat 'start /b flask run'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                bat 'curl http://127.0.0.1:5000/ping'
            }
        }
        stage('cleanup') {
            steps {
                echo 'cleaning up ...'
                bat 'taskkill /f /im flask.exe'
            }
        }
    }
}
