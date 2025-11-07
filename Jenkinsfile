pipeline {
    agent any

    environment {
        NODE_ENV = 'production'
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                // Install Node.js dependencies
                sh 'npm install'
            }
        }

        stage('Run Tests') {
            steps {
                // Run frontend tests
                sh 'npm test'
            }
        }

        stage('Build') {
            steps {
                // Build production bundle
                sh 'npm run build'
            }
        }

        stage('Deploy') {
            steps {
                // Optional: add your deployment commands here
                sh 'echo "Deploy your frontend here"'
            }
        }
    }

    post {
        success {
            echo "✅ Frontend pipeline completed successfully!"
        }
        failure {
            echo "❌ Pipeline failed. Check the console output."
        }
    }
}
