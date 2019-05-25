from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
import datetime


from .models import puzzle, wrong_page, hint_password, Answer
from users.models import User


# Create your views here.
# @login_required
def last_puzzle(request):
    if not request.user.is_authenticated:
        print("NOT AUTHED")
        return redirect('/')

    user = User.objects.get(username=request.user.username)

    user_last_puzzle = puzzle.objects.filter(puzzle_solved_by=user).order_by('pk').last()
    puzzle_title = user_last_puzzle.puzzle_title
    puzzle_image = user_last_puzzle.puzzle_image
    puzzle_audio = user.last_solved_puzzle.puzzle_audio
    puzzle_image_width_height = user.last_solved_puzzle.puzzle_image_width_height
    print("TYPE: ", type(puzzle_audio.name))
    # print("IMAGE: ", str(settings.MEDIA_ROOT) + puzzle_image)
    puzzle_description = str(user_last_puzzle.puzzle_description)
    if puzzle_audio.name == '':
        print("IS NONE")
        return render(request, 'puzzle.html',
                      {'puzzle_title': puzzle_title, 'puzzle_image': puzzle_image.url,
                       'puzzle_image_width_height': puzzle_image_width_height,
                       'puzzle_description': puzzle_description})
    else:
        print("IS NOT NONE")
        return render(request, 'puzzle.html',
                      {'puzzle_title': puzzle_title, 'puzzle_image': puzzle_image.url, 'puzzle_audio': puzzle_audio.url,
                       'puzzle_image_width_height': puzzle_image_width_height,
                       'puzzle_description': puzzle_description})


@login_required
def pass_level(request):
    user = User.objects.get(username=request.user.username)
    l_puzzle = puzzle.objects.filter(puzzle_solved_by=user).order_by('pk').last()
    # print(l_puzzle)
    # print("**********", request.method)
    if request.method == 'POST':
        # print(request.META.get('HTTP_REFERER'))
        password = request.POST['password']
        ans = Answer.objects.create(answer_content=password, answer_created_by=user,
                                    answer_created_time=datetime.datetime.now())

        if password == l_puzzle.puzzle_password:
            # print(user.last_solved_puzzle)
            user.last_solved_puzzle = l_puzzle.next_puzzle
            # print(user.last_solved_puzzle)
            user.save()
            return redirect('/')

        else:
            print(l_puzzle.puzzle_hinted_password.all())
            if len(l_puzzle.puzzle_hinted_password.all()) > 0:
                for hint in l_puzzle.puzzle_hinted_password.all():
                    print("in for")
                    print(hint, password)
                    if password.encode('utf-8') == str(hint).encode('utf-8'):
                        print("IN IF")
                        w_page = hint.hinted_page
                        return render(request, 'wrong.html', {'wrong_page_title': w_page.wrong_page_title,
                                                              'wrong_page_image': w_page.wrong_page_image,
                                                              'wrong_page_description': w_page.wrong_page_description})

            w_page = wrong_page.objects.filter(wrong_page_title='نه', wrong_page_description='').first()
            return render(request, 'wrong.html', {'wrong_page_title': w_page.wrong_page_title,
                                                  'wrong_page_image': w_page.wrong_page_image,
                                                  'wrong_page_description': w_page.wrong_page_description})
