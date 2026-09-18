pipeline{
    agent{
        label "python-agent"
    }
    stages{
        stage('Bağımlılıkları kur'){
            steps {
                sh 'pip3 install pytest'
            }
        }
        stage ('Test et') {
            steps {
                sh 'python3 -m pytest test_calculator.py -v'
            }
        }
    }
    
}