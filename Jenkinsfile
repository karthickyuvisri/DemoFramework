pipeline{
 agent any
 stages{
  stage('Clone Repository'){
    steps{
     git branch:'main'
     url:'https://github.com/karthickyuvisri/DemoFramework.git'
    }
  }
  stage('setup virtual env'){
    steps{
     bat "python -m venv venv"
     bat "./venv/scripts/activate"
    }
  }
  stage("Install requirements"){
  steps{
    bat "pip install -r requirements.txt"
  }
  }
  stage("Run tests"){
  steps{
    bat "pytest"
  }
  }
 }
}