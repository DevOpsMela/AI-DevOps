#!/usr/bin/env python
import os
import sys
import logging

# 1. Silence all LiteLLM and OpenTelemetry logging immediately
os.environ["OTEL_PYTHON_DISABLED"] = "True"
os.environ["LITELLM_LOG"] = "CRITICAL"
logging.getLogger('litellm').setLevel(logging.CRITICAL)

from kube_yaml_creator.crew import KubeAdminCrew

def run():
    inputs = {
        'app_name': 'nginx-webapp',
        'container_image': 'nginx:1.21-alpine',
        'replicas': 3,
        'port': 80
    }
    
    os.makedirs('manifests', exist_ok=True)
    
    try:
        # Execute the crew
        KubeAdminCrew().crew().kickoff(inputs=inputs)
        print("\n✅ Manifest generated successfully in 'manifests/nginx-deployment.yaml'")
    except Exception as e:
        print(f"❌ Crew execution error: {e}")
    finally:
        os._exit(0) 

if __name__ == "__main__":
    run()
