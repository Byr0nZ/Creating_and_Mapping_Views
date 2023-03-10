from django.shortcuts import render
from django.http import HttpResponse

def CCMSMission(request):
    return HttpResponse("The College of Computing and Multimedia Studies shall produce competent and innovative professionals or Technopreneurs in the Information and Communication Technology (ICT) industry adequately prepared in the practice of their profession supportive of national development goals and standards of global excellence.")
def CCMSVision(request):
    return HttpResponse("The College of Computing and Multimedia Studies shall be a center of excellence in delivering Computing and Multimedia education.")
def CCMSObjectives(request):
    return HttpResponse("Be employes and demonstrate professionalism, competence and passion in solving contemporary comuting problems by developing or utilizing innovative IT solutions. Embark in lifelong learning or research to attune to the continuous innovation in the IT industry in order to adapt to the changing demands of the global market.Exhibit leadership and teamwork, and commitment to their respective local or global organizations.")
   