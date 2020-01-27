def mensagemResult = ''
def tagName = 'brazildatacube/bdc-core:build-' + currentBuild.number

env.tagName = tagName

def checkoutProject() {
    stage('checkout') {
        checkout([
            $class: 'GitSCM',
            branches: [[name: '${ghprbActualCommit}']],
            doGenerateSubmoduleConfigurations: false,
            extensions: [],
            gitTool: 'Default',
            submoduleCfg: [],
            userRemoteConfigs: [[
                name: 'origin',
                refspec: '+refs/pull/*:refs/remotes/origin/pr/*',
                url: 'https://github.com/brazil-data-cube/bdc-core.git'
            ]]
        ])
    }
}

def prepareEnvironment() {
    stage('prepare-environment') {
        sh 'docker build --tag ${tagName} -f docker/Dockerfile .'
    }
}

def codeCheck() {
    stage('code check') {
        sh 'docker run --rm -i -v $(pwd):/data --name core_code_check ${tagName} bash -c "pylint --exit-zero --output-format=parseable --reports=yes bdc_core/ > /data/pylint.log"'

        recordIssues minimumSeverity: 'NORMAL',
            qualityGates: [
                [threshold: 1, type: 'DELTA_ERROR', unstable: false],
                [threshold: 1, type: 'DELTA_HIGH', unstable: true],
                [threshold: 1, type: 'DELTA_NORMAL', unstable: true],
                [threshold: 1, type: 'NEW_HIGH', unstable: false],
                [threshold: 1, type: 'TOTAL_HIGH', unstable: true],
                [threshold: 1, type: 'TOTAL_ERROR', unstable: false]
            ],
            tools: [pyLint(pattern: 'pylint.log')]
    }
}

def generateDocs() {
    stage('generate docs') {
        sh 'docker run --rm -i -v $(pwd):/bdc-core -w /bdc-core/docs --name core_docs ${tagName} make html'
    }
}

def unittest() {
    stage('unittest') {
        sh 'docker run --rm -i --name core_test ${tagName} python3 -m pytest -v'
    }
}

def deploy() {
    stage('deploy') {
        // TODO
        sh 'echo "Deploy development server"'
    }
}

def notifySlack(String buildStatus = 'STARTED', String mensagem = '') {
    buildStatus = buildStatus ?: 'SUCCESS'

    def color

    if (buildStatus == 'STARTED') {
        color = '#D4DADF'
        mensagem = mensagem ?: 'Iniciado'
    } else if (buildStatus == 'SUCCESS') {
        color = '#BDFFC3'
        mensagem = mensagem ?: 'Finalizado'
    } else if (buildStatus == 'UNSTABLE') {
        color = '#FFFE89'
        mensagem = mensagem ?: 'Travado'
    } else {
        color = '#FF9FA1'
        mensagem = mensagem ?: 'Erro'
    }

    def msg = "${buildStatus}: `${env.JOB_NAME}` #${env.BUILD_NUMBER}:\n${env.BUILD_URL}\n${mensagem}"

    echo "${env}"

    slackSend(color: color, message: msg)
}

def cleanEnvironment() {
    sh 'docker rmi ${tagName} || exit 0'
}

node("ubuntu-16.04"){
    try {
        checkoutProject()
        notifySlack()

        prepareEnvironment()

        codeCheck()

        generateDocs()

        unittest()

        deploy()
    } catch (e) {
        currentBuild.result = 'FAILURE'
        mensagemResult = e.toString()
        throw e
    } finally {
        notifySlack(currentBuild.result, mensagemResult)
        cleanEnvironment()
    }
}