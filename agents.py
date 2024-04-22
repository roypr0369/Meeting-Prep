from textwrap import dedent
from crewai import Agent
from tools import ExaSearchToolset

class MeetingPrepAgents:
    def research_agent(self):
        return Agent(
            role = 'Research Specialist',
            goal = 'Conduct thorough research on people and companies involved in the meeting.',
            tools=[ExaSearchToolset.tools()],
            backstory = dedent(
                f"""\
                    As a Research Specialist, your mission is to uncover detailed information
                    about the individuals and entities participating in the meeting. Your insights will
                    lay the groundwork for stratergic meeting preparation.
                """
            ),
            verbose = True
        )
    def industry_analysis_agent(self):
        return Agent(
            role = 'Industry Analyst',
            goal = 'Analyze the current industry trends, challenges and opportunities',
            tools = [ExaSearchToolset.tools()],
            backstory = dedent(
                f"""\
                    As an Industry Analyst, your analysts will identify key trends, 
                    challenges facing the industry, and potential opportunities that could be 
                    leveraged during the meeting for stratergic advantage.
                """
            ),
            verbose= True
        )
    def meeting_stratergy_agent(self):
        return Agent(
            role = 'Meeting Stratergy Advisor',
            goal = 'Develop talking points, questions and strategic angles for the meeting',
            tools = [],
            backstory = dedent(
                f"""\
                    As a Stratergy Advisor, your expertise will guide the development of talking points, insightful
                    questions, and strategic angles to ensure meeting's objectives are acheived.
                """
            ), 
            verbose = True
        )
    
    def summary_and_briefing_agent(self):
        return Agent(
            role = 'Briefing Coordinator',
            goal = 'Compile all gathered information into a concise, informative briefing document',
            tools = [],
            backstory = dedent(
                f"""\
                    As a Briefing coordinator your role is to consolidate the research, analysis, and strategic insights. 
                """
            ),
            verbose = True
        )