from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class KubeAdminCrew():
    """KubeAdmin crew for automated manifest generation"""

    @agent
    def kube_admin(self) -> Agent:
        return Agent(config=self.agents_config['kube_admin'], verbose=True)

    @task
    def create_nginx_manifest(self) -> Task:
        return Task(config=self.tasks_config['create_nginx_manifest'])

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )
