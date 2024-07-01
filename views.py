from django.shortcuts import render,redirect
from django.views import View
from django.contrib import messages
from django.contrib.sessions.models import Session
from .models import*
from django.http import JsonResponse
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
import datetime
from django.db.models import Count
import json
from django.http import JsonResponse
from django.core.serializers import serialize
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers
from django.db.models import Count
from django.db.models import Sum
import hashlib
import datetime
from datetime import date
from django.db.models import Count, Max, Subquery, OuterRef
from django.core.files import File
from django.core.files.base import ContentFile
from django.core.files.temp import NamedTemporaryFile
import os
from .models import*
import numpy as np
import face_recognition
from datetime import datetime
import cv2
# Create your views here.

def Home(request):
	return render(request,"Home.html",{})

def Admin_Login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        if AdminDetails.objects.filter(username = username,password = password).exists():
            ad = AdminDetails.objects.get(username=username, password=password)
            print('d')
            messages.info(request,'Admin login is Sucessfull')
            request.session['type_id'] = 'Admin'
            request.session['UserType'] = 'Admin'
            request.session['login'] = "Yes"
            return redirect("/")
        else:
            print('y')
            messages.error(request, 'Error wrong username/password')
            return render(request, "admin_login.html", {})
    else:
        return render(request, "admin_login.html", {})



def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        print('username',username)
        print('password',password)
        if voter_register.objects.all().filter(username=username,password=password).exists():
            Data = voter_register.objects.all().filter(username=username,password=password)
            messages.info(request,"Voter Logged In")
            for i in Data:
                User_id = i.id
            # print('login')
            request.session['User_ID'] = Data[0].id
            request.session['type_id'] = 'User'
            request.session['UserType'] = username
            request.session['login'] = "Yes"
            return redirect('/')
        else:
            print("Please Register first")
            return redirect('/')
    return render(request,'voter_login.html',{})

def manage_elections(request):
    details = election_detail.objects.all()
    return render(request, "manage_elections.html", {'details': details})

def Add_Elections(request):
    if request.method == "POST":
        election_name = request.POST['election_name']
        election_category = request.POST['election_category']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        election_commission = request.POST['election_commission']
        state = request.POST['state']
        date = datetime.strptime(start_date, "%Y-%m-%d").strftime("%d-%m-%Y")
        print(date)
        obj = election_detail(
                         election_name = election_name
                        ,election_category  = election_category
                        ,start_date = date
                        ,end_date = end_date
                        ,election_commission = election_commission
                        ,state = state
                    )
        obj.save()
        messages.info(request,"Election Detials Succesfully Added")
        return redirect("/manage_elections/")
    else:
        return render(request,"Add_Elections.html",{})

def View_elections(request):
    details = election_detail.objects.all()
    return render(request, "manage_elections.html", {'details': details})

def Update_elections(request):
    if request.method =="POST":
        election_detail_ID = request.POST['1updateid']
        election_name=request.POST['1updatename']
        election_category=request.POST['1updatecategory']
        election_commission = request.POST['1updatecommission']
        state=request.POST['1updatestate']
        election_detail.objects.filter(id = election_detail_ID).update(
                                                        election_name = election_name
                                                        ,election_category  = election_category
                                                        ,election_commission = election_commission
                                                        ,state = state)
        messages.info(request,"Election Details Updated")
        return redirect('/manage_elections/')
    else:
        return render(request,"manage_elections.html",{})


def delete_elections(request,id):
    election_detail.objects.filter(id=id).delete()
    return redirect('/manage_elections/')


def manage_candidates(request):
    details = candidate_detail.objects.all()
    data = election_detail.objects.order_by().values('election_name').distinct()
    print(data)
    return render(request, "manage_candidates.html", {'details': details,'data':data})



def Add_Candidates(request):
    if request.method == "POST":
        candidate_name = request.POST['candidate_name']
        age = request.POST['age']
        gender = request.POST['gender']
        political_party = request.POST['political_party']
        caste = request.POST['caste']
        Address = request.POST['Address']
        election_name = request.POST['subject']
        obj = candidate_detail(
                        candidate_name = candidate_name
                        ,age  = age
                        ,gender = gender
                        ,political_party = political_party
                        ,caste = caste
                        ,Address = Address
                        ,election_name = election_name
                    )
        obj.save()
        messages.info(request,"Candidate Detials Succesfully Added")
        return redirect("/manage_candidates/")
    else:
        data = election_detail.objects.order_by().values('election_name').distinct()
        return render(request,"Add_Candidates.html",{'data':data})

def View_candidates(request):
    details = candidate_detail.objects.all()
    return render(request, "manage_candidates.html", {'details': details})

def Update_candidates(request):
    if request.method =="POST":
        candidate_detail_ID = request.POST['1updateid']
        candidate_name = request.POST['1updatecandidate_name']
        age = request.POST['1updateage']
        gender = request.POST['1updategender']
        political_party = request.POST['1updatepolitical_party']
        caste = request.POST['1updatecaste']
        Address = request.POST['1updateAddress']
        election_name = request.POST['1update_e_name']
        candidate_detail.objects.filter(id = candidate_detail_ID).update(
                                                        candidate_name = candidate_name
                                                        ,age  = age
                                                        ,gender = gender
                                                        ,political_party = political_party
                                                        ,caste = caste
                                                        ,Address = Address
                                                        ,election_name = election_name)
        messages.info(request,"Candidate Details Updated")
        return redirect('/manage_candidates/')
    else:
        data = election_detail.objects.order_by().values('election_name').distinct()
        return render(request,"manage_candidates.html",{'data':data})


def delete_candidates(request,id):
    candidate_detail.objects.filter(id=id).delete()
    return redirect('/manage_candidates/')

def manage_voters(request):
    details = voter_register.objects.all()
    return render(request, "manage_voters.html", {'details': details})

def View_Voters(request):
    details = voter_register.objects.all()
    return render(request, "manage_voters.html", {'details': details})

def Update_Voters(request):
    if request.method =="POST":
        voter_detail_ID = request.POST['1updateid']
        voter_name = request.POST['1updatevoter_name']
        Age = request.POST['1updateAge']
        Gender = request.POST['1updateGender']
        Address = request.POST['1updateAddress']
        username = request.POST['1updateusername']
        password = request.POST['1updatepassword']
        confirm_password = request.POST['1updateconfirm_password']
        voter_register.objects.filter(id = voter_detail_ID).update(
                                                        voter_name = voter_name
                                                        ,Age  = Age
                                                        ,Gender = Gender
                                                        ,Address = Address
                                                        ,username = username
                                                        ,password = password
                                                        ,confirm_password = confirm_password)
        messages.info(request,"Voter Details Updated")
        return redirect('/manage_voters/')
    else:
        return render(request,"manage_voters.html",{})

def delete_voters(request,id):
    voter_register.objects.filter(id=id).delete()
    return redirect('/manage_voters/')

def Verification(request):
    aadhar_no = request.POST.get('aadhar_no')
    print(aadhar_no)
    if master_table.objects.all().filter(aadhar_card_no=aadhar_no).exists():
        sentence = 'exists1'
        data = {
        'respond': sentence 
        }
        return JsonResponse(data)
    else:
        sentence = ' does not exists'
        data = {
        'respond': sentence 
        }
        return JsonResponse(data)

# def Add_voter(request):
#     # data = login.objects.all().filter(email=email,password=password)
#     if request.method == "POST":
#         voter_name = request.POST['voter_name']
#         Age = request.POST['Age']
#         Gender = request.POST['Gender']
#         Address = request.POST['Address']
#         username = request.POST['username']
#         password = request.POST['password']
#         confirm_password = request.POST['confirm_password']
#         print('voter_name', voter_name)
#         print('Age',Age)
#         print('Gender',Gender)
#         print('Address',Address)
#         print('username',username)
#         print('password',password)
#         print('confirm_password',confirm_password)
#         Data = voter_register(voter_name=voter_name,Age=Age,Gender=Gender,Address=Address,username=username,password=password,confirm_password=confirm_password)
#         Data.save()
#         return redirect("/")
#     else:
#         return redirect("/Add_voter/")


def Add_voter(request):
    if request.method =="POST":
        username = request.POST['username']
        voter_name = request.POST['voter_name']
        Age = request.POST['Age']
        Gender = request.POST['Gender']
        Address = request.POST['Address']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        print(username)
        if voter_register.objects.filter(username=username).exists():
            messages.info(request,'Username Already Exists')
            return redirect('/manage_voters/')
        else:
            cam = cv2.VideoCapture(0)

            # title of the app
            # cv2.namedWindow('python webcam screenshot app')

            # let's assume the number of images gotten is 0
            img_counter = 0
            username = username

            Data = voter_register(voter_name=voter_name,Age=Age,Gender=Gender,Address=Address,username=username,password=password,confirm_password=confirm_password)
            Data.save()

            # while loop
            while True:
                # intializing the frame, ret
                ret, frame = cam.read()
                # if statement
                if not ret:
                    print('failed to grab frame')
                    break
                # the frame will show with the title of test
                cv2.imshow('test', frame)
                #to get continuous live video feed from my laptops webcam
                k  = cv2.waitKey(1)
                # if the escape key is been pressed, the app will stop
                if k%256 == 27:
                    print('escape hit, closing the app')
                    break
                # if the spacebar key is been pressed
                # screenshots will be taken
                elif k%256  == 32:
                    # the format for storing the images scrreenshotted
                    img_name = f'{username}'
                    #path to the folder where the screenshit will be saved
                    path = 'C:/workspace/Digital_Voting_System/Project/media/user_images'
                    # saves the image as a png file
                    cv2.imwrite(os.path.join(path,img_name +".jpg"), frame)
                    #path1 = 'C:/PythonProjects/Facial_Recognition_Attendance/media/'+ img_name + '.jpg'
                    #print(path1)
                    print('screenshot taken')
                    # the number of images automaticallly increases by 1
                    img_counter += 1
            # release the camera
            cam.release()
            # stops the camera window
            cv2.destroyAllWindows()
            return redirect('/manage_voters/')



def view_voters(request):
    details = voter_register.objects.all()
    return render(request,"view_voters.html",{'details':details})

def profile_update(request):
    if request.method == "POST":
        voter_detail_ID = request.POST['updateid']
        voter_name = request.POST['updatevoter_name']
        Age = request.POST['updateAge']
        Gender = request.POST['updateGender']
        Address = request.POST['updateAddress']
        voter_register.objects.filter(id = voter_detail_ID).update(  
                                                        voter_name = voter_name
                                                        ,Age  = Age
                                                        ,Gender = Gender
                                                        ,Address = Address
                                                        )
        messages.info(request,"Voter Details Updated")
        return redirect('/profile_update/')
    else:
        user_id=request.session['User_ID']
        details = voter_register.objects.all().filter(id=user_id)
        print(details)
        return render(request,"profile_update.html",{'details':details})

def change_password(request):
    if request.method == 'POST':
        voter_detail_ID = request.POST['updateid']
        password = request.POST['updatepassword']
        confirm_password = request.POST['updateconfirm_password']
        voter_register.objects.filter(id = voter_detail_ID).update(
                                                                password = password
                                                                ,confirm_password = confirm_password)
        messages.info(request,"password Changed Succesfully")
        return redirect('/')
    else:
        user_id=request.session['User_ID']
        return render(request,"change_password.html",{'user_id':user_id})

def view_elections(request):
    if request.method == 'POST':
        data1 = request.POST['data']
        print(data1)
        response_data = {'message': 'Data received'}
        return JsonResponse(response_data)
        details = election_detail.objects.all()
        return render(request, "view_elections.html", {'details': details})
    else:
        details = election_detail.objects.all()
        return render(request, "view_elections.html", {'details': details})






def view_candidate(request,election_name):
    details = candidate_detail.objects.filter(election_name=election_name)
    print(election_name)
    return render(request, "view_candidate.html",{'details': details,'election_name':election_name})


def Participated(request):
    details = election_detail.objects.all()
    voter_id = request.session['User_ID']
    for i in details:
        election_id =i.id
        data = vote.objects.all().filter(voter_id=voter_id,election_id=election_id).values()
    print(data)
    return render(request,'pending_participated.html',{'details':details})

def voters_list(request,id):
    print(id)
    details = vote.objects.filter(election_id=id)
    return render(request,"voters_list.html",{'details':details,'id':id})

# def elections_list(request):
#     details = election_detail.objects.all()
#     return render(request,"elections_list.html",{'details':details})

def View_Voters(request):
    details= voter_register.objects.all()
    E_details = election_detail.objects.all()
    return render(request,"View_Votes.html",{'details':details,'E_details':E_details})

def voter_details(request,voter_id):
    details = voter_register.objects.filter(id=voter_id)
    return render(request,"voter_details.html",{'details':details})

def get_winner(request):
    if request.method == 'POST':
        # Get the votes for the specified election
        votes = vote.objects.filter(election_name=election_name)

        # Calculate the vote counts for each candidate
        vote_counts = votes.values('candidate_name').annotate(count=Count('candidate_id'))

        # Determine the winner based on the maximum vote count
        winner = max(vote_counts, key=lambda x: x['count'])
        print(winner)

        # Return the winner as a JSON response
        response_data = {
            'winner': winner['candidate_name'],
            'votes': winner['count']
        }
        return JsonResponse(response_data)
    else:
        return render(request,"view_winner.html")







    


# def count_election_winner(election_id):
#     # Get all the votes for the given election
#     votes = Vote.objects.filter(election_id=election_id)

#     # Count the votes for each candidate
#     vote_counts = votes.values('candidate_id').annotate(count=Count('candidate_id'))

#     # Find the candidate with the most votes
#     winner = None
#     max_votes = 0
#     for vote_count in vote_counts:
#         if vote_count['count'] > max_votes:
#             max_votes = vote_count['count']
#             winner = vote_count['candidate_id']

#     # Return the ID of the winning candidate
#     print(winner)
#     return winner



def Logout(request):
    Session.objects.all().delete()
    return redirect("/")

'''if master_table.objects.areturnll().filter(aadhar_no=aadhar_no).exists():
                                    Data= master_table.objects.all().filter(aadhar_no=aadhar_no)
                                    messages.info(request,"Voter is valid")
                                    return redirect('/login/')
                                else:
                                    print("Voter is not valid")
                                     redirect('/')'''


def Winner(request):
    details = election_detail.objects.all()
    print(details)
    return render(request, "Winner.html", {'details': details})


def ViewCandidates_Winner(request,election_name):
    details = candidate_detail.objects.filter(election_name=election_name)
    data = election_detail.objects.filter(election_name=election_name)
    for a in data:
        end_date=data[0].end_date
        print("Endate :"+str(end_date))
    today = date.today()
    today=str(today) 
    print(str(today))
    counts = {}
    max_vote_id = None
    for i in details:
        candidate_id = i.id
        info = vote.objects.all().filter(election_name=election_name,candidate_id=candidate_id)
        votes_num = len(info)
        print(votes_num)
        candidate_detail.objects.filter(id=candidate_id).update(Vote=votes_num)
        # count = info.count()
        # counts[candidate_id] = count
    candidate_with_max_vote = candidate_detail.objects.all().filter(election_name=election_name).order_by('-Vote').first()
    print("candidate_with_max_vote"+str(candidate_with_max_vote))
    try:
        max_vote_id = candidate_with_max_vote.id
        print("Max:"+str(max_vote_id))
    except:
        messages.info(request,f"There are no candidates in {election_name}")
    winner = candidate_detail.objects.filter(id =max_vote_id,election_name=election_name)
    return render(request,"ViewCandidates_Winner.html",{'details':details,'winner':winner,'election_name':election_name,'end_date':end_date,'today':today})



def voter_participation(request):
    voter_id = request.session['User_ID']
    participated_elections = vote.objects.filter(voter_id=voter_id).values_list('election_name', flat=True).distinct()
    pending_elections = election_detail.objects.exclude(election_name__in=participated_elections).values_list('election_name', flat=True)
    participated_elections=participated_elections.values()
    pending_elections=pending_elections.values()
    context = {
        'participated_elections': participated_elections,
        'pending_elections': pending_elections
    }
    return render(request, 'voter_participation.html', context)






# max_votes=''
#     for i in election:
#         election_id = i.id
#         ename = i.election_name
#         max_votes = vote.objects.filter(election_id=election_id).values('candidate_id').annotate(Max('id')).order_by('-id__max')[:1]
#         max_candidate_ids = [vote['candidate_id'] for vote in max_votes]
#         max_candidates = vote.objects.filter(election_id=election_id, candidate_id__in=max_candidate_ids).annotate(vote_count=Count('id')).order_by('candidate_id')
        
#         print("max_votes :"+str((max_votes).values()))
#         print("max_candidate_ids :"+str(max_candidate_ids))
#         print("max_candidates :"+str(max_candidates.values('candidate_id', 'candidate_name', 'political_party', 'vote_count')))
#         #return max_candidates.values('candidate_id', 'candidate_name', 'political_party', 'vote_count')








    
def capture(request):
    if request.method =="POST":
        username = request.POST['username']
        print(username)
        if userDetails.objects.filter(username=username).exists():
            messages.info(request,'Username Already Exists')
            return redirect('/Registeration2')
        else:
            cam = cv2.VideoCapture(0)

            # title of the app
            # cv2.namedWindow('python webcam screenshot app')

            # let's assume the number of images gotten is 0
            img_counter = 0
            username = username

            # while loop
            while True:
                # intializing the frame, ret
                ret, frame = cam.read()
                # if statement
                if not ret:
                    print('failed to grab frame')
                    break
                # the frame will show with the title of test
                cv2.imshow('test', frame)
                #to get continuous live video feed from my laptops webcam
                k  = cv2.waitKey(1)
                # if the escape key is been pressed, the app will stop
                if k%256 == 27:
                    print('escape hit, closing the app')
                    break
                # if the spacebar key is been pressed
                # screenshots will be taken
                elif k%256  == 32:
                    # the format for storing the images scrreenshotted
                    img_name = f'{username}'
                    #path to the folder where the screenshit will be saved
                    path = 'C:/workspace/Digital_Voting_System/Project/media/user_images'
                    # saves the image as a png file
                    cv2.imwrite(os.path.join(path,img_name +".jpg"), frame)
                    #path1 = 'C:/PythonProjects/Facial_Recognition_Attendance/media/'+ img_name + '.jpg'
                    #print(path1)
                    print('screenshot taken')
                    # the number of images automaticallly increases by 1
                    img_counter += 1
            # release the camera
            cam.release()
            # stops the camera window
            cv2.destroyAllWindows()
            return render(request,"Registeration.html",{})
    else:
        return render(request,"Registeration.html",{})









def add_vote(request,id):
    path = 'media/user_images'
    images = []
    personName = []
    myList = os.listdir(path)
    print(myList)
    #To split or to extract the username 
    for img in myList:
        #Reading our images from the folder
        current_img = cv2.imread(f'{path}/{img}')
        #Insering images inside images list 
        images.append(current_img)
        #splitting Username and extention
        personName.append(os.path.splitext(img)[0])
    print(personName)
    def faceEncodings(images):
        encodeList = []
        for img in images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encode = face_recognition.face_encodings(img)[0]
            encodeList.append(encode)
        return encodeList
    encodeListKnown = faceEncodings(images)
    print("Encoding Complete")

    name = ""
    cap = cv2.VideoCapture(0)

    while True:
        ret,frame = cap.read()
        faces = cv2.resize(frame,(0,0),None,0.25,0.25)
        faces = cv2.cvtColor(faces,cv2.COLOR_BGR2RGB)

        facesCurrentFrame = face_recognition.face_locations(faces)
        encodesCurrentFrame = face_recognition.face_encodings(faces,facesCurrentFrame)

        for encodeFace,faceLoc in zip(encodesCurrentFrame,facesCurrentFrame):
            matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown,encodeFace)

            matchIndex = np.argmin(faceDis)

            if matches[matchIndex]:
                name = personName[matchIndex].upper()
                # print(name)
                y1,x2,y2,x1 = faceLoc
                y1,x2,y2,x1 = y1*4,y2*4,x2*4,x1*4
                cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
                cv2.rectangle(frame, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(frame, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                time_now = datetime.now()
                dStr = time_now.strftime('%d/%m/%Y')
                
                time_now = datetime.now()
                tStr = time_now.strftime('%H:%M:%S')
                dStr = time_now.strftime('%d/%m/%Y')
        print("out of for loop")            
        cv2.imshow("Camera",frame)

        if cv2.waitKey(10) == 13:#if enter key is pressed
            break
    print("out of while")
    cap.release()
    cv2.destroyAllWindows()
    if name:
        print(name)
    userid = request.session['User_ID']
    data = voter_register.objects.filter(id=userid)
    for i in data:
        username = data[0].username
        print(username.upper())
    if name and name.strip() == username.upper().strip():
        print("Can_Id" + str(id))
        Candidate_Id = id
        print(Candidate_Id)
        voter_Id = request.session['User_ID']
        details = candidate_detail.objects.filter(id =id)
        for i in details:
            election_name = details[0].election_name
            print(election_name)
            candidate_name=  details[0].candidate_name
            political_party = details[0].political_party
        data = election_detail.objects.filter(election_name=election_name)
        from django.db.models import Max
        users = vote.objects.all()
        #might be possible model has no records so make sure to handle None
        next_id = users.aggregate(Max('id'))['id__max'] + 1 if users else 1
        print("next_id" + str(next_id))
        today = date.today() 
        for i in data:
            election_id = data[0].id
            print(election_id)
        if vote.objects.filter(voter_id=voter_Id,election_id=election_id).exists():
            messages.info(request,"your have already voted ")
            return redirect('/view_candidate/'+election_name)
        else:
            obj = vote(voter_id=voter_Id
                    ,election_id=election_id
                    ,candidate_id=id
                    ,candidate_name=candidate_name
                    ,political_party=political_party
                    ,election_name=election_name
                    ,Date=today)
            obj.save()
            messages.info(request,"Your vote is registered")
            return redirect('/view_candidate/'+election_name)
    else:
        messages.info(request, "Does not match with logged in face id")
        print("Can_Id" + str(id))
        Candidate_Id = id
        print(Candidate_Id)
        voter_Id = request.session['User_ID']
        details = candidate_detail.objects.filter(id =id)
        for i in details:
            election_name = details[0].election_name
            print(election_name)
            candidate_name=  details[0].candidate_name
            political_party = details[0].political_party
        data = election_detail.objects.filter(election_name=election_name)
        from django.db.models import Max
        users = vote.objects.all()
        #might be possible model has no records so make sure to handle None
        next_id = users.aggregate(Max('id'))['id__max'] + 1 if users else 1
        print("next_id" + str(next_id))
        today = date.today() 
        for i in data:
            election_id = data[0].id
            print(election_id)
        return redirect('/view_candidate/'+election_name)




