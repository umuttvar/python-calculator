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
                sh 'echo Bu KUBERNETES agentta calisti'
                sh 'hostname'
                junit 'test-sonuclari.xml'
            }
        }

        stage ('Docker Agent - Syntax Kontrolu') {
            agent {
                label 'python-agent'
            }
            steps {
                sh 'python3 -m py_compile calculator.py'
                echo 'Syntax Kontrolu tamamlandi'
                sh 'echo BU DOCKER agentta calisti'
                sh 'hostname'
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