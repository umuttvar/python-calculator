pipeline{
    agent{
        label "python-agent"
    }

    environment{
        UYGULAMA_ADI = 'python_calculator'
    }

    triggers {
        pollSCM('H/5 * * * *')
    }
    stages{
        stage('Bağımlılıkları kur'){
            steps {
                sh 'pip3 install pytest --break-system-packages'
            }
        }
        
        stage ('Test et') {
            steps {
                sh 'python3 -m pytest test_calculator.py -v'
            }
        }
         stage ('Trigger testi') {
            steps {
                sh 'echo Trigger Testi'
            }
        }

        stage ('Sadece main branch\'te calis') {
            when {
                branch 'main'
            }
            steps {
                echo "Bu, ${UYGULAMA_ADI} projesinin main branch'i"
            }
        }

        stage ('Paralel Kontroller'){
            parallel {
                stage('Testleri calistir') {
                    steps {
                        sh 'python3 -m pytest test_calculator.py -v'
                    }
                }
                stage('Syntax kontrolu') {
                    steps {
                    sh 'python3 -m py_compile calculator.py'
                    echo 'Syntax Kontrolu tamamlandi'
                    }
                }
            }
        }
    }

    post {
     success {
        echo "Build BASARILLI ${UYGULAMA_ADI}"
     }
     failure {
        echo "Build BASARISIZ OLDU ${UYGULAMA_ADI}"
     }
     always {
        echo "Pipeline tamamlandi!"
     }
    }
    
}

