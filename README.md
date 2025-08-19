# AI-Powered Observability Pipeline with Gemini and Grafana

This project provides a complete, containerized AIOps pipeline that automatically analyzes application errors and sends intelligent reports to Slack. It uses Grafana for alerting, n8n for workflow automation, and Google's Gemini for AI-powered analysis.

This guide covers the automated setup, which gets the entire stack running with a single command.

<img width="732" height="366" alt="image" src="https://github.com/user-attachments/assets/ba9d0842-4123-43a7-a766-d29b92d19839" />


## Prerequisites

Before you begin, you will need to generate two security tokens. This pipeline will not be fully functional without them.

1. **Google Gemini API Key:** This is required for the n8n workflow to access the AI model for log analysis.
    
    - You can generate a key from [**Google AI Studio**](https://aistudio.google.com/app/apikey "null").
        
2. **Slack Bot Token:** This allows the n8n workflow to post messages to your Slack workspace.
    
    - Follow the instructions [**here**](https://docs.n8n.io/integrations/builtin/credentials/slack/#using-api-access-token).
        

## Quick Start: Automatic Provisioning

These steps will launch the entire observability stack. You will then add your secret keys in the n8n user interface to complete the setup.

### Step 1: Clone the Repository

Open your terminal and clone the project files to your local machine.

```
git clone https://github.com/deeepak-tyagii/ai-monitoring-n8n-grafana.git
```

### Step 2: Navigate to the Project Directory

Change into the directory containing the AIOps project.

```
cd ai-monitoring-n8n-grafana
```

### Step 3: Launch the Stack

Use Docker Compose to build the application image and start all services.

```
docker-compose up -d --build
```

The first time you run this, it may take a few minutes to download all the necessary Docker images. Once the command completes, all services are running.

### Step 4: Configure Secrets in n8n

The final step is to add your API keys to the n8n workflow.

1. Navigate to the n8n UI at `http://localhost:5678`.
    
2. Login and Click on **Build from Scratch**.
3. Import the Workflow using the [**n8n_workflow.json**](https://raw.githubusercontent.com/deeepak-tyagii/ai-monitoring-n8n-grafana/c4b2d27ae7b60c81ed1b1a8d74fd541dd883bdca/n8n_workflow.json) file by clicking on **Import File** option from top right menu.
4. Click on the **Google Gemini Chat Model** node.
    
5. In the properties panel on the right, under **Credential**, click **Create New** and paste in your **Google Gemini API Key**.
    
6. Next, click on the **Slack** node (connected to the Gemini node).
    
7. Under **Credential**, click **Create New**. Paste your **Slack Bot Token** (`xoxb-...`) into the **Access Token** field.
    
8. Click the **Save** button to finalize your workflow.
9. 
<img width="1600" height="478" alt="AD_4nXc6Y9UQHuv430xmJWrJ7QlKu46XhPXn0SE_KJSqAij4QCvlJKAtQel8ZC_-_ntP7yVwWj10o4yVCZnwxRx3mCJxtKZ5cSVcLLtbYyFoWnqUr312VlGdltmY" src="https://github.com/user-attachments/assets/298d14ea-c08a-4d9c-b03a-633f376aaa54" />

## Testing the Pipeline

1. **Test the Log-Based Alert:**
    
    - Open your web browser and navigate to `http://localhost:8080/error` **several times**.
        
    - Within about a minute, Grafana will fire the alert, and you should see the full AI analysis in Slack.

   <img width="3767" height="1302" alt="Pasted Graphic 66" src="https://github.com/user-attachments/assets/1af58249-c2e2-41ac-959f-1536eb6e84e9" />

        
