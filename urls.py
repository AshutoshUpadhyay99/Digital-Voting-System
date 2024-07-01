from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .import views

urlpatterns = [
				path('',views.Home,name="Home"),
				path('Admin_Login/',views.Admin_Login,name="Admin_Login"),
				path('Logout/',views.Logout,name="Logout"),
				path('login/',views.login,name="login"),
				path('manage_elections/',views.manage_elections,name="manage_elections"),
				path('Add_Elections/',views.Add_Elections,name="Add_Elections"),
				path('View_elections/',views.View_elections,name="View_elections"),
				path('Update_elections/',views.Update_elections,name="Update_elections"),
				path('delete_elections/<int:id>',views.delete_elections,name="delete_elections"),
				path('Add_Candidates/',views.Add_Candidates,name="Add_Candidates"),
				path('manage_candidates/',views.manage_candidates,name="manage_candidates"),
				path('View_candidates/',views.View_candidates,name="View_candidates"),
				path('Update_candidates/',views.Update_candidates,name="Update_candidates"),
				path('delete_candidates/<int:id>',views.delete_candidates,name="delete_candidates"),
				path('manage_voters/',views.manage_voters,name="manage_voters"),
				path('View_Voters/',views.View_Voters,name="View_Voters"),
				path('Update_Voters/',views.Update_Voters,name="Update_Voters"),
				path('delete_voters/<int:id>',views.delete_voters,name="delete_voters"),
				path('Verification/',views.Verification,name="Verification"),
				path('Add_voter/',views.Add_voter,name="Add_voter"),
				path('change_password/', views.change_password, name='change_password'),
				path('view_voters/',views.view_voters,name='view_voters'),
				path('profile_update/',views.profile_update,name='profile_update'),
				path('view_elections/',views.view_elections,name='view_elections'),
				path('view_candidate/<str:election_name>',views.view_candidate,name='view_candidate'),
				path('add_vote/<int:id>',views.add_vote,name='add_vote'),
				path('voters_list/<int:id>',views.voters_list,name='voters_list'),
				path('View_Voters/',views.View_Voters,name="View_Voters"),
				path('voter_details/<int:voter_id>',views.voter_details,name="voter_details"),
				path('Participated/',views.Participated,name="Participated"),
				path('get_winner/',views.get_winner,name="get_winner"),
				path('Winner/',views.Winner,name="Winner"),
				path('ViewCandidates_Winner/<str:election_name>',views.ViewCandidates_Winner,name="ViewCandidates_Winner"),
				path('voter_participation/',views.voter_participation,name="voter_participation"),
				
				




]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)