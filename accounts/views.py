from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from .forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.utils import timezone
from .models import UserProfile


@login_required
def logout(request):
    auth.logout(request)
    url = request.META.get('HTTP_REFERER')
    messages.success(request, "you logged out successfully")
    return HttpResponseRedirect(url)

def login(request):
    for k in request.GET:
        print(request.GET[k])
    redirect_to = request.GET.get('next', 'home')
    if request.method=='POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            #Authenticate the user
            user = auth.authenticate(username=request.POST.get('username'),
                                     password=request.POST.get('password'))
            # if the user is a user, and has correct password
            if user is not None:
                #Log them in
                auth.login(request, user)
                messages.success(request, "You have sucessfully logged out")
                return redirect(redirect_to)
            else:
                # say no
                form.add_error(None, "Your username or password was not recognised")
    else:
        form = UserLoginForm()
    return render(request, 'login.html', { 'form': form })

# @login_required()
# def yourprofile(request):
#     characters = CharacterProfile.objects.filter(userprofile=request.user)
#     return render(request, 'accounts/yourprofile.html', {"characters":characters})


# def profile(request, id):
#     person = get_object_or_404(User, pk=id)
#     characters = CharacterProfile.objects.filter(userprofile=person)
#     if request.user.is_authenticated:
#         if Follow.objects.filter(follower=request.user, followed=person):
#             followstatus = True
#         else:
#             followstatus = False
#     else:
#         followstatus = False
#     return render(request, 'accounts/profile.html', {"person":person, "followstatus":followstatus, "characters":characters})


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            user = auth.authenticate(username=request.POST.get('username'),
                                     password=request.POST.get('password1'))
            if user:
                auth.login(request, user)
                messages.success(request, "You have successfully registered")
                return redirect('home')
            else:
                messages.error(request, "unable to log you in at this time!")
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})



@login_required()
def remove_profile(request, id):
    profile = get_object_or_404(User, pk=id)
    if request.user.id == profile.id or request.user.is_staff:
        auth.logout(request)
        profile.delete()
    return redirect('home')

# @login_required()
# def set_main(request, id):
#     character = get_object_or_404(CharacterProfile, pk=id)
#     print(character)
#     print("Got Character")
#     if request.user == character.userprofile:
#         if request.user.uprofile:
#             profile = request.user.uprofile
#             print(profile)
#             profile.main_character = character
#             profile.save()
#         else:
#             return redirect('updateprofile')
#     print(profile.main_character)
#     return redirect("yourprofile")

# @login_required()
# def update_profile(request):
#     if request.method=="POST":
#         form = ProfileForm(request.POST)
#         if UserProfile.objects.filter(user=request.user):
#             upro = request.user.uprofile
#             upro.bio=request.POST.get('bio')
#             upro.img_profile=request.POST.get('img_profile')
#             upro.playing_game=Game(pk=request.POST.get('playing_game'))
#             upro.streamkey=request.POST.get('streamkey')
#             upro.save()
#             return redirect("yourprofile")
#         if form.is_valid:
#             upro = form.save(commit=False)
#             upro.user = request.user
#             upro.last_online = timezone.now()
#             upro.img_profile=request.POST.get('img_profile')
#             upro.save()
#             return render(request, "accounts/update.html", {"form":form})

#     if UserProfile.objects.filter(user=request.user):
#         form = ProfileForm(instance=request.user.uprofile)
#     else:
#         form = ProfileForm()
#     return render(request, "accounts/update.html", {"form":form})

# def update_character(request, id):
#     character = get_object_or_404(CharacterProfile, pk=id)
#     game = character.game
#     ranks = updategetrank(game)
#     attributes = Attributes.objects.filter(game=game)
#     if character.userprofile == request.user:
#         if request.method=="POST":
#             character.rank = request.POST.get("rank")
#             character.save()
#             for r in attributes:
#                 result = AttributeChoices.objects.filter(name__attribute=r, character=character)
#                 if result:
#                     result = AttributeChoices.objects.get(name__attribute=r, character=character)
#                     print("got and saving")
#                     result.name = AttributeValue(pk=int(request.POST.get(r.name)))
#                 else:
#                     print("not and saving")
#                     result = AttributeChoices()
#                     result.name = AttributeValue(pk=int(request.POST.get(r.name)))
#                     result.character=character
#                 result.save()

#             return redirect('yourprofile')
#         return render(request, "accounts/updatecharacter.html", {"character":character, "attributes":attributes, "ranks":ranks})
#     else:
#         return redirect('home')

# @login_required()
# def create_character(request):
#     if request.method=="POST":
#         form = CharacterProfileForm(request.POST)
#         char = form.save(commit=False)
#         char.userprofile = request.user
#         char.save()
#         return redirect("yourprofile")
#     else:
#         form = CharacterProfileForm()
#         return render(request, "accounts/createcharacter.html", {"form":form})