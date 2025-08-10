from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.admin.views.decorators import staff_member_required

User = get_user_model()

# Create your views here.
@login_required
def profile_detail_view(request, username=None, *args, **kwargs):
    page_title = 'Profile'
    html_template = 'protected/profile.html'
    
    current_user = request.user
    user_groups = current_user.groups.all()
    print(f"User Groups: {user_groups}")

    # if user_groups.filter(name__icontains='AJK').exists():
    #     return HttpResponse("You are AJK.")
    is_me = current_user
    context = {
        "owner": is_me,
        "page_title": page_title,
    }
    return render(request, html_template, context)
