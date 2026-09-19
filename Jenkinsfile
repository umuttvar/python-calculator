pipeline {
    agent none

    environment {
        UYGULAMA_ADI = 'python_calculator'
    }

    triggers {
        pollSCM('H/5 * * * *')
    }

    stages {
        stage('Bagimliliklari kur') {
            agent {
                label 'python-k8s-agent'
            }
            steps {
                sh '''
                    pip3 install pytest --break-system-packages
                    python3 -m pytest test_calculator.py -v --junitxml=test-sonuclari.xml
                '''
                junit 'test-sonuclari.xml'
            }
        }
    }

    post {
        success {
            echo "Build BASARILI ${UYGULAMA_ADI}"
        }
        failure {
            echo "Build BASARISIZ OLDU ${UYGULAMA_ADI}"
        }
    }
}