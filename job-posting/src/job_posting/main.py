import sys
from .crew import JobPostingCrew
#from job_posting.crew import JobPostingCrew


def run():
    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    inputs = {
        'company_domain':'https://atos.net/',
        'company_description': "Atos is an IT company. It offering Network, security and cloud services and support for mmanny big customers. Lot of different skilled engineers, managers and atchitect are working there.",
        'hiring_needs': 'There is new project for elektomonility company to migrate their DC to Azure cloud',
        'specific_benefits':'Monthly Pay, ambicius project, healthcare, good working atmosphere',
    }
    JobPostingCrew().crew().kickoff(inputs=inputs)



def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'company_domain':'https://atos.net/',
        'company_description': "Atos is an IT company. It offering Network, security and cloud services and support for mmanny big customers. Lot of different skilled engineers, managers and atchitect are working there.",
        'hiring_needs': 'There is new project for elektomonility company to migrate their DC to Azure cloud',
        'specific_benefits':'Monthly Pay, ambicius project, healthcare, good working atmosphere',
    }
    try:
        JobPostingCrew().crew().train(n_iterations=int(sys.argv[1]), inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")
