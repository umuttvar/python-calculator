pipeline{
    agent{
        label "python-agent"
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
    }
    
}