pipeline {
    agent {
        label "python-agent"
    }
    environment {
        UYGULAMA_ADI = 'python-calculator'
    }
    stages {
        stage('Bagimliliklari kur') {
            steps {
                sh 'pip3 install pytest --break-system-packages'
            }
        }
        stage('Test et') {
            steps {
                sh 'python3 -m pytest test_calculator.py -v'
            }
        }
        stage('Sadece main branch') {
            when {
                branch 'main'
            }
            steps {
                echo 'Bu MAIN branch'
            }
        }
    }
    post {
        success {
            echo "Build basarili"
        }
    }
}