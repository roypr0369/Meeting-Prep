from textwrap import dedent
from crewai import Task

class MeetingPrepTasks():
    def research_task(self, agent, meeting_participants, meeting_context):
        return Task(
            description = dedent(f"""\
                Conduct comprehensive research on each of the individuals and companies
                involved in the upcoming meeting. Gather recent news, achievements and 
                professional background, and any relevant business activities.
                
                Participants : {meeting_participants}
                Meeting Context : {meeting_context}
            """),
            expected_output = dedent(f"""
                A detailed report summarising key findings about each participant and company,
                highlighting information that could be relevant for the meeting.
            """),
            agent=agent,
            async_execution=True
        )
    
    def industry_analysis_task(self, agent, meeting_participants, meeting_context):
        return Task(
            description = dedent(f"""\
                Analyze the current industry trends, challenges and opportunities
                relevant to the meeting's context. Consider market reports,
                recent developments, and expert solutions to provide a 
                comprehensive overview of the industry landscape.
                                 
                Participants : {meeting_participants}
                Meeting context : {meeting_context}
            """),
            expected_output = dedent(
                f"""\
                An insightful analysis that identifies major trends, potential challenges,
                and stratergic opportunities.
                """
            ),
            agent=agent,
            async_execution=True
        )
    
    def meeting_stratergy_task(self, agent, meeting_context, meeting_objective):
        return Task(
            description = dedent(
                f"""\
                    Develop stratergic talking points, questions and discussion angles
                    for the meeting based on research and industry analysis conducted.

                    Meeting contex : {meeting_context}
                    Meeting Objective : {meeting_objective}
                """
            ), 
            expected_output=dedent(
                f"""\
                    Complete report with a list of key talking points, stratergic questions to
                    ask to help achieve the meetings objective during the meeting.
                """
            ), 
            agent=agent,
        )
    
    def summarising_and_briefing_task(self, agent, meeting_context, meeting_objective):
        return Task(
            description = dedent(
                f"""\
                    Compile all the research findings, industry analysis and stratergic talking points in concise, 
                    comprehensive briefing document for the meeting.
                    Ensure the meeting is easy to digest and equips the meeting participants with all
                    necessary information and stratergies.

                    Meeting context : {meeting_context}
                    Meeting objective : {meeting_objective}
                """
            ),
            expected_output = dedent(
                f"""\
                    A well-structured document that includes sections for participant
                    bios, industry overview, talking points and stratergic
                    recommendations.
                """
            ),
            agent=agent
        )
    