import logging
import os

from dotenv import load_dotenv
from fastapi import Depends, FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from permit import Permit

load_dotenv()

app = FastAPI(
    title="Permit.io API Integration",
    description="A FastAPI-based backend using Permit.io SDK for role and resource management.",
    version="1.0.0",
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

origins = [
    "http://localhost:3000",  
    "http://127.0.0.1:3000",
    "*",  
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  
    allow_credentials=True, 
    allow_methods=["*"],  
    allow_headers=["*"],  
)

PERMIT_API_KEY = os.getenv("PERMIT_API_KEY")
ENV_ID = os.getenv("ENV_ID")
PROJECT_ID = os.getenv("PROJECT_ID")

permit = Permit(
    token=PERMIT_API_KEY,
    options={
        "environment": ENV_ID,
        "project": PROJECT_ID
    }
)


def get_permit_client() -> Permit:
    if not PERMIT_API_KEY or not ENV_ID or not PROJECT_ID:
        logger.error("Permit.io API configuration is missing in environment variables.")
        raise HTTPException(status_code=500, detail="Permit.io API configuration is incomplete.")
    return permit


@app.get(
    "/projects",
    summary="Get Projects",
    description="Fetch all projects using the Permit.io SDK.",
    tags=["Projects"]
)
async def get_projects(client: Permit = Depends(get_permit_client)):
    try:
        projects = await client.api.projects.list()
        return projects
    except Exception as e:
        logger.error(f"Error fetching projects: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error while fetching projects.")


@app.get(
    "/environments",
    summary="Get Environments",
    description="Fetch all environments for the current project using the Permit.io SDK.",
    tags=["Environments"]
)
async def get_environments(client: Permit = Depends(get_permit_client)):
    try:
        environments = await client.api.environments.list(project_key=PROJECT_ID)
        return environments
    except Exception as e:
        logger.error(f"Error fetching environments: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error while fetching environments.")


@app.get(
    "/resources",
    summary="Get Resources",
    description="Fetch all resources for the current environment using the Permit.io SDK.",
    tags=["Resources"]
)
async def get_resources(client: Permit = Depends(get_permit_client)):
    try:
        resources = await client.api.resources.list()
        return resources
    except Exception as e:
        logger.error(f"Error fetching resources: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error while fetching resources.")


@app.get(
    '/resource_relationships',
    summary="Get Resource Relationships",
    description="Fetch all resource relationships for the current environment using the Permit.io SDK.",
    tags=["Resource Relationships"]
)
async def get_resource_relationships(client: Permit = Depends(get_permit_client)):
    try:
        erorr_api ={
    
    "data": [
            {
            "description": "Relation expresses possible 'member_of' relation between subject of type 'User' to object of type 'Organization'",
            "subject_resource": "User",
            "key": "member_of",
            "name": "member_of",
            "id": "c9b7da28152a45b2b22aa295aa0a5d12",
            "organization_id": "519ffeac17c94c6180d03cbfc0d956fd",
            "project_id": "9ffb2d6842a347b3abd2df9bbd89bcdf",
            "environment_id": "14664ff2afdb431a906bb57d836e82b4",
            "created_at": "2024-11-17T06:46:28+00:00",
            "updated_at": "2024-11-17T06:46:28+00:00",
            "object_resource_id": "f5f471253c394a2f8fd8309d858b0ef7",
            "object_resource": "Organization",
            "subject_resource_id": "ee1f33736f5c40f8ad5be059ef34b505"
            },
            {
            "description": "Relation expresses possible 'parent' relation between subject of type 'Repository' to object of type 'Issue'",
            "subject_resource": "Repository",
            "key": "parent",
            "name": "parent",
            "id": "d4fb7fbb246e49fc88936c3a307391d4",
            "organization_id": "519ffeac17c94c6180d03cbfc0d956fd",
            "project_id": "9ffb2d6842a347b3abd2df9bbd89bcdf",
            "environment_id": "14664ff2afdb431a906bb57d836e82b4",
            "created_at": "2024-11-17T06:45:38+00:00",
            "updated_at": "2024-11-17T06:45:38+00:00",
            "object_resource_id": "452a17df735a48989497dfe31fc82e75",
            "object_resource": "Issue",
            "subject_resource_id": "e67bd7668c1d4a22b6c10266cdbf39e9"
            },
            {
            "description": "Relation expresses possible 'parent' relation between subject of type 'Organization' to object of type 'Repository'",
            "subject_resource": "Organization",
            "key": "parent",
            "name": "parent",
            "id": "90ad0df1f06946bf8aa32449b914a09b",
            "organization_id": "519ffeac17c94c6180d03cbfc0d956fd",
            "project_id": "9ffb2d6842a347b3abd2df9bbd89bcdf",
            "environment_id": "14664ff2afdb431a906bb57d836e82b4",
            "created_at": "2024-11-17T06:45:53+00:00",
            "updated_at": "2024-11-17T06:45:53+00:00",
            "object_resource_id": "e67bd7668c1d4a22b6c10266cdbf39e9",
            "object_resource": "Repository",
            "subject_resource_id": "f5f471253c394a2f8fd8309d858b0ef7"
            },
            {
            "description": "Relation expresses possible 'member_of' relation between subject of type 'User' to object of type 'Repository'",
            "subject_resource": "User",
            "key": "member_of",
            "name": "member_of",
            "id": "b17f5dc3bd5843d48c97e571e4bf6c84",
            "organization_id": "519ffeac17c94c6180d03cbfc0d956fd",
            "project_id": "9ffb2d6842a347b3abd2df9bbd89bcdf",
            "environment_id": "14664ff2afdb431a906bb57d836e82b4",
            "created_at": "2024-11-17T07:11:37+00:00",
            "updated_at": "2024-11-17T07:11:37+00:00",
            "object_resource_id": "e67bd7668c1d4a22b6c10266cdbf39e9",
            "object_resource": "Repository",
            "subject_resource_id": "ee1f33736f5c40f8ad5be059ef34b505"
            }
        ],
        "total_count": 4,
        "page_count": 1
        }

        # resource_relation_list = {}
        # resources_list = await get_resources(client)
        # for resource in resources_list:
        #     # /v2/schema/{proj_id}/{env_id}/resources/{resource_id}/relations
        #     print(resource.key)
        #     resource_relation = await client.api.resource_relations.list(resource_key=resource.key)
           
        #     resource_relation_list[resource.key] = resource_relation
        return erorr_api
    except Exception as e:
        logger.error(f"Error fetching resources: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error while fetching resources.")
    