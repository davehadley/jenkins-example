pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building'
                sh '''#!/usr/bin/env bash
                    wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -nv -O miniconda.sh
                    bash miniconda.sh -b -p $WORKSPACE/miniconda
                    source $WORKSPACE/miniconda/bin/activate
                    conda config --set always_yes yes
                    conda update -q conda
                    conda env create -n $WORKSPACE -f environment.yaml
                    conda activate $WORKSPACE
                    echo --- Environment Variables
                    env
                    echo --- Python Packages
                    which pip
                    which python
                    pip list
                    '''
                
            }
        }
        stage('Test') {
            steps {
                echo 'Testing'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying'
            }
        }
    }
    post {
        always {
            echo 'This will always run'
        }
        success {
            echo 'This will run only if successful'
        }
        failure {
            echo 'This will run only if failed'
        }
        unstable {
            echo 'This will run only if the run was marked as unstable'
        }
        changed {
            echo 'This will run only if the state of the Pipeline has changed'
            echo 'For example, if the Pipeline was previously failing but is now successful'
        }
    }
}