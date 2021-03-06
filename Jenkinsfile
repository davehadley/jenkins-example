pipeline {
    agent any

    stages {
        stage('Setup') {
            steps {
                echo 'Setup'
                sh '''#!/usr/bin/env bash
                    echo --- Environment
                    echo Working Directory: $(pwd)
                    echo Directory contents:
                    ls
                    echo --- Install Conda
                    wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -nv -O miniconda.sh
                    bash miniconda.sh -b -p $WORKSPACE/miniconda
                    source $WORKSPACE/miniconda/bin/activate
                    conda config --set always_yes yes
                    conda update -q conda
                    conda env create -f environment.yml --prefix $WORKSPACE/conda-env
                    conda activate $WORKSPACE/conda-env
                    # echo --- Install Poetry
                    # curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
                    echo --- Environment Variables
                    env
                    echo --- Python Packages
                    echo pip = $(which pip)
                    echo python = $(which python)
                    echo poetry = $(which poetry)
                    echo conda = $(which conda)
                    pip list
                    '''
                
            }
        }
        stage('Build') {
            steps {
                echo 'Build'
                sh '''#!/usr/bin/env bash
                source $WORKSPACE/miniconda/bin/activate
                conda activate $WORKSPACE/conda-env
                poetry install
                '''
            }
        }
        stage('Test') {
            steps {
                echo 'Testing'
                sh '''#!/usr/bin/env bash
                source $WORKSPACE/miniconda/bin/activate
                conda activate $WORKSPACE/conda-env
                poetry run pytest tests
                '''
            }
        }
        stage('Lint') {
            stages {
                stage('Black') {
                    steps {
                        sh '''#!/usr/bin/env bash
                        source $WORKSPACE/miniconda/bin/activate
                        conda activate $WORKSPACE/conda-env
                        poetry run black --check src tests
                        '''
                    }
                }
                stage('MyPy') {
                    steps {
                        sh '''#!/usr/bin/env bash
                        source $WORKSPACE/miniconda/bin/activate
                        conda activate $WORKSPACE/conda-env
                        poetry run mypy src tests
                        '''
                    }
                }
                stage('Flake8') {
                    steps {
                        sh '''#!/usr/bin/env bash
                        source $WORKSPACE/miniconda/bin/activate
                        conda activate $WORKSPACE/conda-env
                        poetry run flake8 src tests
                        '''
                    }
                }
            }
        }
        stage('Dist') {
            steps {
                echo 'Deploying'
                sh '''#!/usr/bin/env bash
                 source $WORKSPACE/miniconda/bin/activate
                 conda activate $WORKSPACE/conda-env
                 poetry build
                 '''
            }
        }
        // stage('Publish') {
        //     steps {
        //         echo 'Publish'
        //          '''#!/usr/bin/env bash
        //          source $WORKSPACE/miniconda/bin/activate
        //          conda activate $WORKSPACE/conda-env
        //          poetry publish
        //          '''
        //     }
        // }
    }
    post {
        always {
            echo 'Build completed'
        }
        success {
            echo 'Build was successful'
            cleanWs()
        }
        failure {
            echo 'Build failed'
        }
        unstable {
            echo 'Build unstable'
        }
        changed {
            echo 'Build status changed'
        }
    }
}