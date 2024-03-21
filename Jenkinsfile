pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Check out your code from the source control
                bat "git clone 'http://github.com/AnnaDinaburgVulikh/TestAssignment.git'"
            }
        }

        stage('Run Python Script') {
            steps {
                script {
                    try {
                        // Execute your Python script
                        def pythonOutput = bat(script: "python system_info.py", returnStdout: true).trim()
                        // Save the output to a file or environment variable for later use
                        writeFile(file: 'pythonOutput.txt', text: pythonOutput)
                    } catch(Exception e) {
                        // Handle errors gracefully
                        echo "An error occurred in Python script: ${e.getMessage()}"
                        currentBuild.result = 'FAILURE'
                    }
                }
            }
        }

        stage('Run Pytest') {
            steps {
                script {
                    try {
                        // Execute your Pytest
                        def pytestOutput = bat(script: "pytest", returnStdout: true).trim()
                        // Save the output to a file or environment variable for later use
                        writeFile(file: 'pytestOutput.txt', text: pytestOutput)
                    } catch(Exception e) {
                        // Handle errors gracefully
                        echo "An error occurred in Python script: ${e.getMessage()}"
                        currentBuild.result = 'FAILURE'
                    }
                }
            }
        }

        stage('Run PowerShell Script') {
            steps {
                script {
                    try {
                        // Execute your PowerShell script
                        def powershellOutput = powershell(script: ".\\check_services.ps1 -ServiceNames 'wuauserv', 'Dhcp'", returnStdout: true).trim()
                        // Save the output to a file or environment variable for later use
                        writeFile(file: 'powershellOutput.txt', text: powershellOutput)
                    } catch(Exception e) {
                        // Handle errors gracefully
                        echo "An error occurred in PowerShell script: ${e.getMessage()}"
                        currentBuild.result = 'FAILURE'
                    }
                }
            }
        }

        stage('Generate HTML Report') {
            steps {
                script {
                    try {
                        // Read outputs from files
                        def pythonOutput = readFile('pythonOutput.txt').trim()
                        def pytestOutput = readFile('pytestOutput.txt').trim()
                        def powershellOutput = readFile('powershellOutput.txt').trim()

                        // Compile HTML report
                        def htmlReport = """
                        <!DOCTYPE html>
                        <html>
                        <head>
                        <title>Workflow Report</title>
                        </head>
                        <body>
                        <h1>Workflow Execution Report</h1>
                        <h2>Python Script Output:</h2>
                        <pre>${pythonOutput}</pre>
                        <h2>Pytest Output:</h2>
                        <pre>${pytestOutput}</pre>
                        <h2>PowerShell Script Output:</h2>
                        <pre>${powershellOutput}</pre>
                        </body>
                        </html>
                        """

                        // Write the HTML report to a file
                        writeFile(file: 'report.html', text: htmlReport)
                    } catch(Exception e) {
                        echo "An error occurred while generating HTML report: ${e.getMessage()}"
                        currentBuild.result = 'FAILURE'
                    }
                }
            }
        }

        stage('Archive Artifacts') {
            steps {
                // Archive the HTML report
                archiveArtifacts artifacts: 'report.html', onlyIfSuccessful: true
            }
        }
    }

}
