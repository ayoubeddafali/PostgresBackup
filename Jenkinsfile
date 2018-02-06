pipeline{
  agent {
    label "Slave1"
  }
  stages{
    stage("Installing Deps"){
      steps{
        sh "./helper init"
      }
    }
    stage("Unit Testing"){
      steps{
        sh "./helper test"
      }
    }
    stage("Deploy){
      steps{
        sh "./helper deploy"
      }
    }
    stage("Package"){
      steps{
        sh "./helper package"
      }
    }
  }

}
